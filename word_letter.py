import re
p = "index.html"
s = open(p, encoding="utf-8").read()

NEW_FN = """function buildLetter() {
  const b = $('letterBody');
  b.innerHTML = '';
  let k = 0;
  const WD = 0.03;
  CONFIG.letter.forEach(t => {
    const p = document.createElement('p');
    p.className = 'para';
    t.split(/(\\s+)/).forEach(tok => {
      if (tok === '' || /^\\s+$/.test(tok)) { p.appendChild(document.createTextNode(tok)); return; }
      const sp = document.createElement('span');
      sp.className = 'w';
      sp.textContent = tok;
      sp.style.setProperty('--wd', (0.3 + k * WD).toFixed(2) + 's');
      k++;
      p.appendChild(sp);
    });
    b.appendChild(p);
  });
  $('sig').style.setProperty('--d', (0.3 + k * WD + 0.4).toFixed(2) + 's');
}
"""

n = len(re.findall(r"function buildLetter\(\) \{.*?\n\}\n", s, flags=re.S))
print("buildLetter found" if n == 1 else f"WARNING: buildLetter matches = {n}")
s = re.sub(r"function buildLetter\(\) \{.*?\n\}\n", lambda m: NEW_FN, s, count=1, flags=re.S)

CSS = """/* Word-by-word letter text */
.para{opacity:1;animation:none}
.w{display:inline-block;opacity:0;transform:translateY(8px);animation:wordIn .5s ease forwards;animation-delay:var(--wd,0s)}
@keyframes wordIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
"""
if s.count("/* Music */") == 1:
    s = s.replace("/* Music */", CSS + "\n/* Music */", 1)
    print("CSS added")
else:
    print("WARNING: music comment not found, CSS not added")

open(p, "w", encoding="utf-8").write(s)
print("Saved index.html")
