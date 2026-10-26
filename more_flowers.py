p = "index.html"
s = open(p, encoding="utf-8").read()

def rep(old, new):
    global s
    n = s.count(old)
    print(("OK " if n == 1 else f"WARNING ({n} matches) ") + old[:55])
    s = s.replace(old, new)

rep('const max = ph ? 42 : 96;', 'const max = ph ? 80 : 170;')
rep('Math.max(80, Math.min(W, H) / 3.8)', 'Math.max(64, Math.min(W, H) / 3.2)')
rep('Math.max(80, Math.min(W, H) / 3.4)', 'Math.max(64, Math.min(W, H) / 3)')
rep('if (Math.random() < (ph ? .35 : .55)) {', 'if (Math.random() < (ph ? .6 : .85)) {')
rep('if (!inside(ox, oy)) items.push({ ox, oy, size: cell * rand(.95, 1.25), z: 2, small: false });',
    'if (!inside(ox, oy)) items.push({ ox, oy, size: cell * rand(.95, 1.25), z: 2, small: false });\n      if (!inside(ox + rand(-.5, .5) * cell, oy + rand(-.5, .5) * cell) && Math.random() < .6) items.push({ ox: ox + rand(-.5, .5) * cell, oy: oy + rand(-.5, .5) * cell, size: cell * rand(.8, 1.1), z: 2, small: false });')

open(p, "w", encoding="utf-8").write(s)
print("Saved index.html")
