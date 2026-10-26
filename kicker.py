import re
p = "index.html"
s = open(p, encoding="utf-8").read()
new_css = """.kicker{font-size:clamp(1rem,3.6vw,1.3rem);font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:#FFE7A8;text-shadow:0 0 10px rgba(0,0,0,.9),0 2px 6px rgba(0,0,0,.9),0 0 22px rgba(216,177,106,.45);background:rgba(40,4,12,.55);padding:.35rem .9rem;border-radius:999px;border:1px solid rgba(216,177,106,.55)}"""
s, n = re.subn(r"\.kicker\{[^}]*\}", new_css, s, count=1)
print("updated" if n == 1 else "WARNING: kicker style not found")
open(p, "w", encoding="utf-8").write(s)
