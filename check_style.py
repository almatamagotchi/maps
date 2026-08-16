import re
src = open('index.html').read()
sources = set(re.findall(r"addSource\(\s*'([^']+)'", src))
print('addSource calls:', sorted(sources))
refs = set(re.findall(r"source:\s*'([^']+)'", src))
print('layer source refs:', sorted(refs))
missing = refs - sources
print('refs without addSource:', missing or 'none')
glyphs = re.findall(r"glyphs:\s*'([^']+)'", src)
print('glyphs decl:', glyphs)
fonts = re.findall(r"text-font:\s*\[([^\]]+)\]", src)
print('text-font layers:', len(fonts))
# find any layer using text-field without the style having glyphs
tf = re.findall(r"text-field", src)
print('text-field occurrences:', len(tf))
