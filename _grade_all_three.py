import json, subprocess, re

audits = [
    ("Eidolon", "Eidolon-2026-06-25.md"),
    ("PhenoSpecs", "PhenoSpecs-2026-06-25.md"),
    ("phenocompose", "phenocompose-2026-06-23.md"),
]

for name, fname in audits:
    result = subprocess.run(
        ["C:\\Windows\\System32\\bash.exe", "-c",
         f"bash registry/audit-absorption-justification/grade.sh audits/absorption-justifications/{fname}"],
        capture_output=True, text=True, timeout=30,
        cwd="C:\\Users\\koosh\\phenotype-registry"
    )
    try:
        clean = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', result.stdout)
        d = json.loads(clean)
        print(f"{name}: {d['score']}/14 grade={d['grade']}")
        for p in d['pillars']:
            print(f"  P{p['id']}: {p['score']}/{p['max']} {p['status']}: {p['detail'][:200]}")
    except Exception as e:
        print(f"{name}: PARSE ERROR — {e}")
        print(f"  stderr: {result.stderr[-200:]}")
        print(f"  stdout (first 300): {result.stdout[:300]}")
