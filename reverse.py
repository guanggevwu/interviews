# asumme the input is '\b' '\n' instead of '\\b', '\\n', i.e., x = '' instead of r''

x="the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"

pageslist = []
pages = x.split('\b')[:-1]
for p in pages:
    lines = p.split('\n')[:-1]
    lineslist = []
    for l in lines:
        words = l.split(' ')
        words.reverse()
        aline_txt = ' '.join(words)
        lineslist.append(aline_txt)
    lineslist.reverse()
    apage_txt = '\n'.join(lineslist) + '\n'
    pageslist.append(apage_txt)
pageslist.reverse()
full_txt = '\b'.join(pageslist) + '\b'
print(full_txt)

