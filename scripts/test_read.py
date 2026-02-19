from pathlib import Path
p = Path('networks/user_anime_ids.csv')
print('exists:', p.exists())
try:
    stat = p.stat()
    print('size:', stat.st_size)
except Exception as e:
    print('stat error', e)

print('\nFirst 10 lines:')
with p.open('r', encoding='utf-8', errors='replace') as f:
    for i, line in enumerate(f):
        if i>=10:
            break
        print(f'{i+1}: {line.strip()}')
