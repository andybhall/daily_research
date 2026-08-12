# Hugging Face Hub live probe — Dataset Hunt 2026-08-12 (frontier 4, platform/API exhaust; AI focus)
# Public API, no auth: https://huggingface.co/api/models?sort=downloads&direction=-1&limit=1000&full=true
# Each record: id, author, downloads, likes, gated, createdAt, lastModified, library_name,
#              pipeline_tag, tags[] (incl. license:*), siblings[]  -> the AI model supply side.
import json, datetime
from collections import Counter
top=json.load(open('models_top.json')); rec=json.load(open('models_recent.json'))
print("records:",len(top),"| example:",top[0]['id'],top[0]['downloads'],"downloads")
print("tasks:",Counter(m.get('pipeline_tag') for m in top).most_common(6))
print("authors>1 model:",sum(1 for a,c in Counter(m.get('author') for m in top).items() if c>1))
