use proptest::prelude::*;
use std::collections::{HashMap, HashSet};

/// Generate an arbitrary DAG of task names [0, n-1] with edges that only
/// go from lower-numbered names to higher-numbered names (guarantees acyclicity).
fn dag_strategy(max_nodes: usize) -> impl Strategy<Value = HashMap<String, Vec<String>>> {
    let n = 1..=max_nodes;
    n.prop_flat_map(|node_count| {
        let tasks: Vec<String> = (0..node_count).map(|i| i.to_string()).collect();
        let dep_lists: Vec<Vec<String>> = (0..node_count)
            .map(|i| {
                // Dependencies must be earlier indices to keep it acyclic
                let possible_deps: Vec<String> = (0..i).map(|j| j.to_string()).collect();
                let max_deps = possible_deps.len();
                proptest::collection::vec(
                    proptest::sample::select(possible_deps.clone()),
                    0..=max_deps,
                )
                .prop_map(|deps| {
                    // Deduplicate in case select picks the same element twice
                    let mut seen = HashSet::new();
                    deps.into_iter().filter(|d| seen.insert(d.clone())).collect()
                })
            })
            .collect::<Vec<_>>();
        dep_lists.prop_map(move |deps| {
            let mut map = HashMap::new();
            for (i, deps) in deps.into_iter().enumerate() {
                map.insert(tasks[i].clone(), deps);
            }
            map
        })
    })
}

proptest! {
    /// For any acyclic task graph, resolve() must produce a valid
    /// topological ordering: every dependency appears before its dependent.
    #[test]
    fn topological_sort_roundtrip(graph in dag_strategy(10)) {
        let mut tg = phenotype_forge::core::TaskGraph::new();
        for (name, deps) in &graph {
            tg.add_task(name, deps.clone());
        }

        let order = match tg.resolve() {
            Ok(o) => o,
            Err(_) => return Err(TestCaseError::fail("expected valid DAG to resolve")),
        };

        // Every task appears exactly once
        assert_eq!(order.len(), graph.len(), "all tasks must appear");
        let all_present: HashSet<_> = order.iter().collect();
        for name in graph.keys() {
            assert!(all_present.contains(name), "task {name} must be in order");
        }

        // For each task, all its dependencies come before it in the order
        let pos: HashMap<&str, usize> = order.iter().enumerate().map(|(i, n)| (n.as_str(), i)).collect();
        for (name, deps) in &graph {
            let name_pos = pos[name.as_str()];
            for dep in deps {
                let dep_pos = pos[dep.as_str()];
                assert!(
                    dep_pos < name_pos,
                    "dependency '{dep}' must be before '{name}' but was after"
                );
            }
        }
    }
}
