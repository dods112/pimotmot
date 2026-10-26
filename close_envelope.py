p = "index.html"
s = open(p, encoding="utf-8").read()
old = "if (id === 'letter') { $('sheet').classList.remove('show'); $('envelope').classList.remove('open', 'gone'); }"
new = "if (id === 'letter') { $('sheet').classList.remove('show'); $('envelope').classList.remove('open', 'gone'); $('envCard').classList.remove('open'); }"
print("updated" if s.count(old) == 1 else "WARNING: line not found")
s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
