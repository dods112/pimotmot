p = "index.html"
s = open(p, encoding="utf-8").read()

NEW_JS = """
// ===== Flowers that pop up gently around the edges over time =====
let popTimer = null;
function popFlower() {
  if (!revealed || reduced || !sprites.length) return;
  const W = innerWidth, H = innerHeight, ph = phone();
  const cx = W / 2, cy = H / 2;
  const rx = (ph ? 0.48 : 0.34) * W, ry = (ph ? 0.52 : 0.40) * H;
  let x, y, tries = 0;
  do {
    x = rand(-0.05, 1.05) * W;
    y = rand(-0.05, 1.05) * H;
    tries++;
  } while (((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 < 1 && tries < 20);
  const size = (ph ? 70 : 110) * rand(0.8, 1.3);
  const w = document.createElement('div');
  w.className = 'flower';
  w.style.cssText = `left:${x - size / 2}px;top:${y - size / 2}px;width:${size}px;height:${size}px;z-index:2`;
  const im = document.createElement('img');
  im.src = pick(); im.alt = ''; im.draggable = false;
  im.onerror = () => { im.src = petalSVG('#e8557a'); };
  w.appendChild(im);
  $('garden').appendChild(w);
  const a = w.animate([
    { opacity: 0, transform: 'scale(.5) rotate(' + rand(-40, 40).toFixed(0) + 'deg)' },
    { opacity: 1, transform: 'scale(1) rotate(' + rand(-8, 8).toFixed(0) + 'deg)', offset: 0.35 },
    { opacity: 1, transform: 'scale(1.02)', offset: 0.8 },
    { opacity: 0, transform: 'scale(.9)' }
  ], { duration: rand(9000, 13000), easing: 'ease-in-out', fill: 'forwards' });
  a.onfinish = () => w.remove();
}
function startPopFlowers() {
  if (popTimer || reduced) return;
  popTimer = setInterval(() => {
    if ($('garden').children.length > (phone() ? 60 : 120)) return;
    popFlower();
  }, phone() ? 1400 : 900);
}
"""

old = "// ===== Boot ====="
if s.count(old) == 1:
    s = s.replace(old, NEW_JS + "\n" + old)
    print("pop-up flowers added")
else:
    print("WARNING: boot marker not found")

old2 = "  document.body.classList.add('revealed');\n  revealed = true;\n  busy = false;\n}"
if s.count(old2) == 1:
    s = s.replace(old2, "  document.body.classList.add('revealed');\n  revealed = true;\n  busy = false;\n  startPopFlowers();\n}")
    print("hooked into reveal")
else:
    print("WARNING: reveal function not found")

open(p, "w", encoding="utf-8").write(s)
print("Saved index.html")
