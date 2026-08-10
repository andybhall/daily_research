# FARA live probe — Dataset Hunt 2026-08-10 (frontier 2, money trails)
# Pulls the DOJ FARA bulk registrant + foreign-principal tables (via the
# OpenSanctions us_fara_filings mirror, refreshed 2026-08-10) and computes
# the panel structure + foreign-principal country breakdown.
# Source files: FARA_All_Registrants.xml, FARA_All_ForeignPrincipals.xml
#   https://data.opensanctions.org/datasets/latest/us_fara_filings/
import re
from collections import Counter, defaultdict
def rows(p): return re.findall(r'<ROW>(.*?)</ROW>', open(p,encoding='utf-8',errors='replace').read(), re.S)
def field(b,t):
    m=re.search(r'<%s>(.*?)</%s>'%(t,t),b,re.S); return m.group(1).strip() if m else ''
reg=rows('FARA_All_Registrants.xml'); fp=rows('FARA_All_ForeignPrincipals.xml')
countries=Counter(); by_reg=defaultdict(set); fp_years=Counter()
for b in fp:
    countries[field(b,'Country_location_represented') or 'UNKNOWN']+=1
    rn,fpn=field(b,'Registration_number'),field(b,'Foreign_principal')
    if rn and fpn: by_reg[rn].add(fpn)
    d=field(b,'FP_registration_date')
    if d[-4:].isdigit(): fp_years[int(d[-4:])]+=1
print(f"registrants={len(reg)} fp_relationships={len(fp)} distinct_registrants={len(by_reg)}")
print("multi-principal registrants:", sum(1 for v in by_reg.values() if len(v)>1))
print("top countries:", countries.most_common(12))
