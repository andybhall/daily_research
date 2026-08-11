# Snap Political Ads live probe — Dataset Hunt 2026-08-11 (frontier 3, optimized persuasion text)
# Yearly ZIPs: https://storage.googleapis.com/ad-manager-political-ads-dump/political/<YEAR>/PoliticalAds.zip
# Each row = one political ad: CreativeUrl + Spend + Impressions + StartDate/EndDate + PayingAdvertiserName
# + ~20 targeting columns (geo, interests, segments, age/gender, advanced demographics).
import csv
from collections import Counter
def load(p): return list(csv.DictReader(open(p,encoding='utf-8',errors='replace')))
for yr in ("2024","2026"):
    rows=load(f"y{yr}/PoliticalAds.csv"); n=len(rows)
    usd=sum(float(r['Spend'] or 0) for r in rows if (r.get('Currency Code') or '').strip()=='USD')
    micro=['Regions (Included)','Electoral Districts (Included)','Metros (Included)',
           'Postal Codes (Included)','Interests','Segments','AdvancedDemographics']
    t=sum(1 for r in rows if any((r.get(k) or '').strip() for k in micro))
    print(yr,"ads",n,"USD$%.0f"%usd,"microtargeted %d%%"%(100*t/n))
