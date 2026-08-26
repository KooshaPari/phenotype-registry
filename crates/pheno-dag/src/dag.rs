//! Core DAG data structure.
//!
//! A generic directed acyclic graph backed by an adjacency list.

use std::collections::{HashMap, HashSet};
use std::hash::Hash;

/// Error types for DAG operations.
#[derive(Debug, Clone, PartialEq, Eq, thiserror::Error)]
pub enum DagError {
    #[error("node `{0:?}` already exists")]
    NodeAlreadyExists(String),

    #[error("node `{0:?}` not found")]
    NodeNotFound(String),

    #[error("edge from `{0:?}` to `{1:?}` would create a cycle")]
    CycleDetected(String, String),

    #[error("internal invariant violation: {0}")]
    InternalInvariant(String),
}

/// A generic directed acyclic graph over node identifiers of type `K`.
#[derive(Debug, Clone)]
pub struct Dag<K> {
    /// All known nodes.
    nodes: HashSet<K>,
    /// Adjacency list: parent -> children (forward edges).
    children: HashMap<K, Vec<K>>,
    /// Reverse adjacency list: child -> parents (back edges).
    parents: HashMap<K, Vec<K>>,
}

// ---------------------------------------------------------------------------
// Construction
// ---------------------------------------------------------------------------

impl<K> Default for Dag<K> {
    fn default() -> Self {
        Self {
            nodes: HashSet::new(),
            children: HashMap::new(),
            parents: HashMap::new(),
        }
    }
}

impl<K> Dag<K>
where
    K: Eq + Hash + Clone + std::fmt::Debug,
{
    /// Create an empty DAG.
    pub fn new() -> Self {
        Self::default()
    }

    /// Insert a new node. Returns an error if the node already exists.
    pub fn add_node(&mut self, node: K) -> Result<(), DagError> {
        if self.nodes.contains(&node) {
            return Err(DagError::NodeAlreadyExists(format!("{:?}", node)));
        }
        self.nodes.insert(node.clone());
        self.children.entry(node.clone()).or_default();
        self.parents.entry(node).or_default();
        Ok(())
    }

    /// Insert a directed edge `from -> to`.
    ///
    /// Both endpoints must already exist.
    pub fn add_edge(&mut self, from: K, to: K) -> Result<(), DagError> {
        if !self.nodes.contains(&from) {
            return Err(DagError::NodeNotFound(format!("{:?}", from)));
        }
        if !self.nodes.contains(&to) {
            return Err(DagError::NodeNotFound(format!("{:?}", to)));
        }
        self.children
            .entry(from.clone())
            .or_default()
            .push(to.clone());
        self.parents.entry(to).or_default().push(from);
        Ok(())
    }

    // -----------------------------------------------------------------------
    // Accessors
    // -----------------------------------------------------------------------

    /// Return the set of all node identifiers.
    pub fn nodes(&self) -> &HashSet<K> {
        &self.nodes
    }

    /// Return the number of nodes.
    pub fn node_count(&self) -> usize {
        self.nodes.len()
    }

    /// Return the number of edges.
    pub fn edge_count(&self) -> usize {
        self.children.values().map(|v| v.len()).sum()
    }

    /// Return the children (direct successors) of `node`.
    pub fn children_of(&self, node: &K) -> Option<&[K]> {
        self.children.get(node).map(|v| v.as_slice())
    }

    /// Return the parents (direct predecessors) of `node`.
    pub fn parents_of(&self, node: &K) -> Option<&[K]> {
        self.parents.get(node).map(|v| v.as_slice())
    }

    /// Return `true` if the graph contains `node`.
    pub fn contains(&self, node: &K) -> bool {
        self.nodes.contains(node)
    }

    /// Iterate over all nodes.
    pub fn iter_nodes(&self) -> impl Iterator<Item = &K> {
        self.nodes.iter()
    }
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn empty_dag() {
        let dag: Dag<u32> = Dag::new();
        assert_eq!(dag.node_count(), 0);
        assert_eq!(dag.edge_count(), 0);
    }

    #[test]
    fn add_and_query_nodes() -> Result<(), DagError> {
        let mut dag = Dag::new();
        dag.add_node(1)?;
        dag.add_node(2)?;
        assert_eq!(dag.node_count(), 2);
        assert!(dag.contains(&1));
        assert!(dag.contains(&2));
        Ok(())
    }

    #[test]
    fn duplicate_node_error() -> Result<(), DagError> {
        let mut dag = Dag::new();
        dag.add_node("a")?;
        assert!(dag.add_node("a").is_err());
        Ok(())
    }

    #[test]
    fn add_edge_missing_source() -> Result<(), DagError> {
        let mut dag = Dag::<&str>::new();
        dag.add_node("b")?;
        assert!(dag.add_edge("a", "b").is_err());
        Ok(())
    }

    #[test]
    fn add_edge_missing_target() -> Result<(), DagError> {
        let mut dag = Dag::<&str>::new();
        dag.add_node("a")?;
        assert!(dag.add_edge("a", "b").is_err());
        Ok(())
    }

    #[test]
    fn simple_edge() -> Result<(), DagError> {
        let mut dag = Dag::new();
        dag.add_node("a")?;
        dag.add_node("b")?;
        dag.add_edge("a", "b")?;
        assert_eq!(dag.edge_count(), 1);
        assert_eq!(dag.children_of(&"a"), Some(&["b"][..]));
        assert_eq!(dag.parents_of(&"b"), Some(&["a"][..]));
        Ok(())
    }

    #[test]
    fn diamond_graph() -> Result<(), DagError> {
        let mut dag = Dag::new();
        for n in ["a", "b", "c", "d"] {
            dag.add_node(n)?;
        }
        dag.add_edge("a", "b")?;
        dag.add_edge("a", "c")?;
        dag.add_edge("b", "d")?;
        dag.add_edge("c", "d")?;
        assert_eq!(dag.node_count(), 4);
        assert_eq!(dag.edge_count(), 4);
        Ok(())
    }
}
