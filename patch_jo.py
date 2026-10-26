import re
p = "index.html"
s = open(p, encoding="utf-8").read()

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        print(f"WARNING: expected {count} match(es), found {n}: {old[:60]}")
    s = s.replace(old, new)

# Your details
rep('herName: "[HER NAME]",', 'herName: "Jo",\n  callSign: "Jo",')
rep('monthsaryDate: "[OUR MONTHSARY DATE]",', 'monthsaryDate: "29th",')
rep('monthsCount: "[NUMBER] months",', 'monthsCount: "23 months",\n  totalMonths: 23,')
rep('startDate: "2025-01-01",', 'startDate: "",')

# Counter: 23 months shown as 1 year and 11 months
s = re.sub(r"  \$\('counter'\)\.textContent = .*\n",
    "  const tm = CONFIG.totalMonths || 0, yy = Math.floor(tm / 12), mm = tm % 12;\n"
    "  $('counter').textContent = yy + (yy === 1 ? ' year' : ' years') + ' \u00b7 ' + mm + (mm === 1 ? ' month' : ' months');\n", s, count=1)
s = re.sub(r"  \$\('counterDays'\)\.textContent = .*\n",
    "  $('counterDays').textContent = CONFIG.startDate ? Math.max(0, Math.floor((n - s) / 864e5)).toLocaleString() + ' days together' : '';\n", s, count=1)

# More flowers, still keeping the center open
rep('const max = ph ? 26 : 54;', 'const max = ph ? 42 : 96;')
rep('Math.max(100, Math.min(W, H) / 5.2)', 'Math.max(80, Math.min(W, H) / 3.8)')
rep('Math.max(90, Math.min(W, H) / 4)', 'Math.max(80, Math.min(W, H) / 3.4)')
rep('if (Math.random() < (ph ? .15 : .3)) {', 'if (Math.random() < (ph ? .35 : .55)) {')

open(p, "w", encoding="utf-8").write(s)
print("Patched index.html")
