// SPDX-License-Identifier: MIT OR Apache-2.0
//
// Copyright (c) 2026 Phenotype-Enterprise
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//! Phenotype library
//!
//! See the project README for the full overview:
//! <https://github.com/Phenotype-Enterprise/phenotype-forge#readme>
//!
//! Note: the README is intentionally NOT embedded via `include_str!` here.
//! It contains forward-looking example code that uses custom proc-macro
//! attributes (`#[task]`, `#[deps(...)]`) which are not yet defined in this
//! crate. Embedding it as inner doc would cause `cargo test --doc` to attempt
//! to compile those examples as doctests and fail.

pub mod core {
    //! Core module for task graph definition and resolution.

    use std::collections::{HashMap, VecDeque};

    /// A directed acyclic graph of tasks with dependency relationships.
    ///
    /// `TaskGraph` stores named tasks and their declared dependencies,
    /// and provides topological sorting to determine a valid execution order.
    ///
    /// # Example
    ///
    /// ```
    /// use phenotype_forge::core::TaskGraph;
    ///
    /// let mut g = TaskGraph::new();
    /// g.add_task("build", Vec::<String>::new());
    /// g.add_task("test", vec!["build".into()]);
    /// g.add_task("deploy", vec!["test".into()]);
    ///
    /// let order = g.resolve().expect("valid DAG");
    /// // build must come before test, test before deploy
    /// let pos = |name: &str| order.iter().position(|t| t == name).unwrap();
    /// assert!(pos("build") < pos("test"));
    /// assert!(pos("test") < pos("deploy"));
    /// ```
    #[derive(Debug, Clone)]
    pub struct TaskGraph {
        tasks: HashMap<String, Vec<String>>,
    }

    impl TaskGraph {
        /// Create a new empty `TaskGraph`.
        pub fn new() -> Self {
            Self {
                tasks: HashMap::new(),
            }
        }

        /// Add a task with its dependency names.
        ///
        /// Dependencies must have been added already; if an unknown dependency
        /// is referenced, it will be treated as a missing node and cause
        /// [`resolve`](Self::resolve) to return an error.
        pub fn add_task(&mut self, name: &str, deps: Vec<String>) {
            self.tasks.insert(name.to_string(), deps);
        }

        /// Resolve a valid execution order via topological sort (Kahn's algorithm).
        ///
        /// Returns `Ok(ordered_names)` on success, or `Err` describing the cycle
        /// if the graph contains one.
        ///
        /// # Errors
        ///
        /// Returns an error if a dependency references a task that has not been
        /// added, or if the graph contains a cycle.
        pub fn resolve(&self) -> Result<Vec<String>, String> {
            // Verify all referenced dependencies exist as tasks.
            for (name, deps) in &self.tasks {
                for dep in deps {
                    if !self.tasks.contains_key(dep.as_str()) {
                        return Err(format!(
                            "task '{name}' depends on unknown task '{dep}'"
                        ));
                    }
                }
            }

            // Build outgoing adjacency list: dependency -> dependents
            let mut adj: HashMap<&str, Vec<&str>> = HashMap::new();
            for name in self.tasks.keys() {
                adj.entry(name.as_str()).or_default();
            }
            for (name, deps) in &self.tasks {
                for dep in deps {
                    // edge dep -> name: dep must run before name
                    adj.entry(dep.as_str()).or_default().push(name.as_str());
                }
            }

            // Compute in-degrees (incoming edges = number of dependencies)
            let mut in_degree: HashMap<&str, usize> = HashMap::new();
            for name in self.tasks.keys() {
                in_degree.entry(name.as_str()).or_insert(0);
            }
            for (name, deps) in &self.tasks {
                if !deps.is_empty() {
                    *in_degree.entry(name.as_str()).or_insert(0) += deps.len();
                }
            }

            // Kahn's algorithm: start with zero-in-degree nodes
            let mut queue: VecDeque<&str> = in_degree
                .iter()
                .filter(|(_, &deg)| deg == 0)
                .map(|(&name, _)| name)
                .collect();

            let mut order = Vec::with_capacity(self.tasks.len());
            while let Some(name) = queue.pop_front() {
                order.push(name.to_string());
                if let Some(neighbors) = adj.get(name) {
                    for &next in neighbors {
                        if let Some(deg) = in_degree.get_mut(next) {
                            *deg -= 1;
                            if *deg == 0 {
                                queue.push_back(next);
                            }
                        }
                    }
                }
            }

            if order.len() != self.tasks.len() {
                return Err("cycle detected in task dependency graph".into());
            }

            Ok(order)
        }
    }

    impl Default for TaskGraph {
        fn default() -> Self {
            Self::new()
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn empty_graph_resolves_to_empty_order() {
            let g = TaskGraph::new();
            let order = g.resolve().unwrap();
            assert!(order.is_empty());
        }

        #[test]
        fn single_task_no_deps() {
            let mut g = TaskGraph::new();
            g.add_task("build", vec![]);
            let order = g.resolve().unwrap();
            assert_eq!(order, vec!["build"]);
        }

        #[test]
        fn linear_chain() {
            let mut g = TaskGraph::new();
            g.add_task("a", vec![]);
            g.add_task("b", vec!["a".into()]);
            g.add_task("c", vec!["b".into()]);
            let order = g.resolve().unwrap();
            let idx = |n: &str| order.iter().position(|t| t == n).unwrap();
            assert!(idx("a") < idx("b"));
            assert!(idx("b") < idx("c"));
        }

        #[test]
        fn diamond_dag() {
            let mut g = TaskGraph::new();
            g.add_task("root", vec![]);
            g.add_task("left", vec!["root".into()]);
            g.add_task("right", vec!["root".into()]);
            g.add_task("leaf", vec!["left".into(), "right".into()]);
            let order = g.resolve().unwrap();
            let idx = |n: &str| order.iter().position(|t| t == n).unwrap();
            assert!(idx("root") < idx("left"));
            assert!(idx("root") < idx("right"));
            assert!(idx("left") < idx("leaf"));
            assert!(idx("right") < idx("leaf"));
        }

        #[test]
        fn cycle_detection() {
            let mut g = TaskGraph::new();
            g.add_task("a", vec!["b".into()]);
            g.add_task("b", vec!["a".into()]);
            assert!(g.resolve().is_err());
        }

        #[test]
        fn self_cycle() {
            let mut g = TaskGraph::new();
            g.add_task("a", vec!["a".into()]);
            assert!(g.resolve().is_err());
        }

        #[test]
        fn unknown_dependency() {
            let mut g = TaskGraph::new();
            g.add_task("build", vec!["nonexistent".into()]);
            assert!(g.resolve().is_err());
        }

        #[test]
        fn resolve_is_deterministic() {
            let mut g = TaskGraph::new();
            g.add_task("a", vec![]);
            g.add_task("b", vec!["a".into()]);
            g.add_task("c", vec!["a".into()]);
            let order1 = g.resolve().unwrap();
            let order2 = g.resolve().unwrap();
            assert_eq!(order1, order2);
        }
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
