"""Verify manuscript: word count, citation-reference match, claims vs results."""
import re, json

md = open('manuscript/manuscript.md').read()

# 1. word count (main text only: strip YAML-less md, count words; report all)
words_all = len(md.split())
# main text: between '## 1. Introduction' and '## Declarations'
m = re.search(r'## 1\. Introduction(.*?)## Declarations', md, re.S)
main = m.group(1) if m else ''
# strip headings, table rows, code
main_clean = re.sub(r'\|.*\|', '', main)
main_clean = re.sub(r'#+ .*', '', main_clean)
words_main = len(main_clean.split())
print("words total:", words_all, "| words main text:", words_main)

# 2. in-text citations vs reference list
refs_section = md.split('## References')[1] if '## References' in md else ''
in_text = set()
for match in re.findall(r'\(([A-Z][A-Za-zÀ-ÿ\'’\-]+(?: et al\.)?(?:,| &| and)?[^()]*)\)', md.split('## References')[0]):
    first = match.split(',')[0].split(' et al.')[0].strip()
    if first and not first.startswith('e.g'):
        in_text.add(first)
ref_first = set()
for line in refs_section.split('\n'):
    line = line.strip()
    if line and not line.startswith('#'):
        m2 = re.match(r'^([A-ZÀ-ÿ][^,]*?),', line)
        if m2:
            ref_first.add(m2.group(1).strip())
# names like 'World Bank', 'World Travel...' etc
missing_ref = sorted(n for n in in_text if n not in ref_first and len(n) > 2)
print("\nin-text author tokens:", len(in_text))
print("reference entries:", len(ref_first))
print("in-text without apparent ref entry:", missing_ref)

# 3. DOI presence check for each reference line
no_doi = [l[:70] for l in refs_section.split('\n') if l.strip() and not l.startswith('#') and 'doi.org' not in l and 'http' not in l and len(l) > 40]
print("\nreference lines without DOI/URL:", no_doi)

# 4. check key numbers cited in abstract/intro appear in results
checks = [
 ('-0.30', 'r gdp'),
 ('-0.36', 'r usage index'),
 ('+0.17', 'r travel exports'),
 ('0.66', 'min tour intensity (TUN)'),
 ('2.87', 'max tour intensity (KGZ)'),
 ('1.05', 'mean tour intensity'),
]
for num, label in checks:
    print(f"{'OK ' if num in md else 'MISSING'} {num} ({label})")
