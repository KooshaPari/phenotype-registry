import json
for lbl,fl in [('Eidolon','_tmp_eidolon.json'),('PhenoSpecs','_tmp_phenospecs.json'),('phenocompose','_tmp_pc.json')]:
    d=json.load(open(fl,encoding='utf-8'))
    print(f'{lbl}: {d["score"]}/14 grade={d["grade"]}')
    for p in d['pillars']:
        if p['score'] < p['max']:
            print(f'  P{p["id"]}: {p["score"]}/{p["max"]} FAIL: {p["detail"][:400]}')
