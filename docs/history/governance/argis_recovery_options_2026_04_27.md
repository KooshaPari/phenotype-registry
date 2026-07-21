# Argis‑extensions – Recovery Options (2026‑04‑27)

The `argis‑extensions` repository currently has diverging histories:

* **Local branch** – 24 recent commits that migrate the Bifrost API.  
* **Upstream (`origin/main`)** – 11 commits that consist of:
  * 6 Dependabot version bumps
  * 4 governance‑related changes
  * 1 initial commit for the new module

There is **no common merge‑base** (the two histories are unrelated) and a direct merge produced **34 conflicts**, so a manual reconciliation is required.

Below are three non‑destructive recovery strategies, the Git commands you would run for each, and an overall recommendation.

---

## 1️⃣ Option A – Use `git replace --graft` to create an artificial merge‑base  

Create a graft that tells Git to treat a chosen commit from the upstream as the parent of the first local commit, thereby stitching the two lineages together.

### Pros
* Keeps **both** histories intact – no rewriting of existing SHA‑1s.
* No need to re‑apply any changes; the graft is purely metadata.

### Cons
* The graft lives only in your local repository (or in a shared refs/replace if you push it explicitly).  
* Other contributors must import the replace ref; otherwise they will see the two histories as unrelated again.  
* Not suitable for a public‑facing branch unless you distribute the replace ref.

### Sample Commands
```bash
# 1. Identify the first local commit (oldest of the 24)
FIRST_LOCAL=$(git rev-list --max-parents=0 HEAD)

# 2. Identify a suitable upstream commit to graft onto
UPSTREAM_BASE=$(git rev-parse origin/main)   # e.g., the tip of upstream

# 3. Create the graft (make UPSTREAM_BASE the parent of FIRST_LOCAL)
git replace --graft $FIRST_LOCAL $UPSTREAM_BASE

# 4. Verify the new history
git log --oneline --graph --decorate --all

# 5. (Optional) Export the replace ref for sharing
git push origin refs/replace/*:refs/replace/*
```

---

## 2️⃣ Option B – Cherry‑pick the 24 local commits onto a fresh copy of upstream  

Reset to the upstream tip, then replay the local work as a linear series of new commits.

### Pros
* Produces a **clean, linear history** that is easy to understand and to push.  
* Works with standard Git workflows; no special metadata needed.  
* Both sets of changes (upstream & local) end up in the same branch.

### Cons
* Rewrites the 24 commit SHA‑1s, so any references to the original commits become stale.  
* Requires a **force‑push** (or a new branch) because the rewritten history diverges from the original local branch.

### Sample Commands
```bash
# 1. Fetch the latest upstream
git fetch origin

# 2. Create a new branch based on upstream
git checkout -b recovery/from-upstream origin/main

# 3. Obtain the list of local commits (oldest → newest)
git rev-list --reverse $(git merge-base HEAD origin/main)..HEAD > /tmp/local-commits.txt

# 4. Cherry‑pick each commit in order
while read COMMIT; do
    git cherry-pick $COMMIT
done < /tmp/local-commits.txt

# 5. Verify the result
git log --oneline --graph --decorate

# 6. Push (force required if you replace the original branch)
git push origin recovery/from-upstream:main --force-with-lease
#    or keep it as a separate branch and open a PR
```

---

## 3️⃣ Option C – Force‑push the local branch over upstream (drop upstream commits)  

Simply overwrite `origin/main` with the current local branch, discarding the 11 upstream commits.

### Pros
* Fast and trivial – no rebasing or cherry‑picking.  
* Guarantees that **all 24 Bifrost migration commits** are preserved exactly as written.

### Cons
* **Loses** the 6 Dependabot bumps, 4 governance commits, and the init commit. Those changes would need to be re‑applied manually later.  
* May upset other collaborators who rely on those upstream commits.  
* Potentially violates project policy about overwriting shared history.

### Sample Commands
```bash
# 1. Ensure you are on the local branch with the 24 commits
git checkout main   # (or whatever your local branch is)

# 2. Verify you are ahead of upstream
git log @{u}..HEAD   # should list the 24 commits

# 3. Force‑push to overwrite remote
git push origin main --force-with-lease
```

---

## 📌 Recommendation – **Option B (Cherry‑pick onto fresh upstream)**  

Option B offers the best compromise:

* **Preserves** both the valuable Bifrost migration work **and** the upstream Dependabot/governance updates.  
* Results in a **single, linear history** that is easy for reviewers and CI pipelines to handle.  
* Requires only a force‑push (or a new PR) but avoids the metadata‑sharing pitfalls of grafts and the data loss of a raw overwrite.

Proceed with the cherry‑pick workflow, test the resulting build, and open a pull request (or fast‑track merge) to replace the stale remote branch. If the repository policy disallows force‑pushes on `main`, push the recovered branch under a temporary name (e.g., `recovery/2026‑04‑27`) and create a PR for merge.

> Source: dispatch-worker output 2026-04-27 (may be truncated)
