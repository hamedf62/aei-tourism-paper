"""Download all historical AEI cross-country weekly/monthly data files (claude_ai)."""
import urllib.request, os, time

FILES = {
 '2025-08': ('release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv', 26840881),
 '2025-11': ('release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv', 94086309),
 '2026-02': ('release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv', 103287181),
 '2026-04+05': ('release_2026_06_26/data/aei_claude_ai_2026-06-26.csv', 219174671),
}
os.makedirs('data/raw/history', exist_ok=True)
for tag, (path, size) in FILES.items():
    out = f'data/raw/history/aei_{tag}.csv'
    if os.path.exists(out) and abs(os.path.getsize(out) - size) < 1000:
        print('skip (exists):', out); continue
    url = f'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/{path}'
    print('downloading', tag, f'({size/1e6:.0f} MB)...')
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as r, open(out, 'wb') as f:
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk: break
                    f.write(chunk)
            got = os.path.getsize(out)
            print('  OK', got)
            if abs(got - size) > 1000:
                print('  WARN size mismatch')
            break
        except Exception as e:
            print('  attempt', attempt, 'failed:', e); time.sleep(5)
print('done')
