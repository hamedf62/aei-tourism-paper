import pandas as pd
# scan whole 2025-11 file for any 'soc' mention in facet names (streaming, low memory)
found = set()
for chunk in pd.read_csv('data/raw/history/aei_2025-11.csv', engine='c', chunksize=1_000_000,
                         usecols=['facet'], on_bad_lines='skip', low_memory=False):
    f = chunk.facet.dropna().unique()
    for x in f:
        if 'soc' in str(x).lower() or 'occup' in str(x).lower():
            found.add(x)
print("soc-like facets:", found if found else "NONE")
# list all facets
allf = set()
for chunk in pd.read_csv('data/raw/history/aei_2025-11.csv', engine='c', chunksize=1_000_000,
                         usecols=['facet'], on_bad_lines='skip', low_memory=False):
    allf.update(chunk.facet.dropna().unique())
print("\nall facets:", sorted(allf))
