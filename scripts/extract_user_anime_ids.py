#!/usr/bin/env python3
import csv
import os
import sys

SRC = os.path.join("networks", "user_anime.csv")
OUT = os.path.join("networks", "user_anime_ids.csv")

def find_keys(fieldnames):
    user_key = None
    anime_key = None
    for k in fieldnames:
        lk = k.strip().lower()
        if lk in ("user_id", "userid", "user id", "user"):
            user_key = k
        if lk in ("anime_id", "animeid", "anime id", "anime"):
            anime_key = k
    return user_key, anime_key

def main():
    if not os.path.exists(SRC):
        print(f"Source file not found: {SRC}")
        sys.exit(2)

    with open(SRC, newline='', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        user_key, anime_key = find_keys(reader.fieldnames or [])
        if user_key is None or anime_key is None:
            print("Could not detect `user_id` and `anime_id` columns. Available columns:", reader.fieldnames)
            sys.exit(3)

        with open(OUT, 'w', newline='', encoding='utf-8') as fout:
            writer = csv.writer(fout)
            writer.writerow(['user_id', 'anime_id'])
            for row in reader:
                writer.writerow([row.get(user_key, ''), row.get(anime_key, '')])

    print(f"Wrote {OUT}")

if __name__ == '__main__':
    main()
