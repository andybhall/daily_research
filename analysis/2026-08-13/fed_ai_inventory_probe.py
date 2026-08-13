# Federal AI Use Case Inventory live probe — Dataset Hunt 2026-08-13 (frontier 5, institutional records; AI focus)
# 2024 consolidated CSV (62 cols), from OMB's repo:
# https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/main/data/2024_consolidated_ai_inventory_raw.csv
# Each row = one agency-reported AI use case: name, agency, topic, dev_stage, impact_type
# (Rights/Safety-Impacting/Neither/Both), commercial-vs-custom, PII, ATO, appeal process, etc.
import csv
from collections import Counter
rows=list(csv.DictReader(open('inv2024.csv',encoding='utf-8-sig')))
def col(r,k):
    for c in r:
        if c.lstrip('﻿')==k: return (r[c] or '').strip()
    return ''
print("use cases:",len(rows),"agencies:",len(set(col(r,'3_agency') for r in rows)))
print("impact:",Counter(col(r,'17_impact_type') for r in rows).most_common())
print("dev_stage:",Counter(col(r,'16_dev_stage') for r in rows).most_common())
