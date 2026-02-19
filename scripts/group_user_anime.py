import json
from pathlib import Path

import pandas as pd

INPUT = Path("networks/user_anime_ids.csv")
OUTPUT = Path("networks/user_anime_list.csv")

if not INPUT.exists():
    raise FileNotFoundError(f"Input not found: {INPUT}")

# Read CSV
df = pd.read_csv(INPUT)
cols = df.columns.tolist()
user_col = next((c for c in cols if "user" in c.lower()), None)
anime_col = next((c for c in cols if "anime" in c.lower()), None)
if user_col is None or anime_col is None:
    raise ValueError(f"Could not detect user/anime columns in {INPUT}; columns: {cols}")

# Group anime IDs into unique sorted lists per user
grouped = df.groupby(user_col)[anime_col].apply(lambda s: sorted(pd.unique(s))).reset_index(name="anime_ids")

# Create sequential new user IDs (0..N-1)
grouped = grouped.sort_values(user_col).reset_index(drop=True)
grouped["new_user_id"] = range(len(grouped))

# Reorder and write out; store anime_ids as JSON strings so lists are preserved
out = grouped[["new_user_id", user_col, "anime_ids"]].rename(columns={user_col: "orig_user_id"})
out["anime_ids"] = out["anime_ids"].apply(lambda lst: json.dumps([int(x) for x in lst]))
out.to_csv(OUTPUT, index=False)

print(f"Wrote {len(out)} users to {OUTPUT}")
