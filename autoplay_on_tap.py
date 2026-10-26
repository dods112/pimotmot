p = "index.html"
s = open(p, encoding="utf-8").read()
old = "$('gift').addEventListener('click', openGift);"
new = """$('gift').addEventListener('click', () => {
  const bgm = $('bgm');
  if (CONFIG.music && CONFIG.music.src && bgm.paused) {
    bgm.play().catch(() => {});
  }
  openGift();
});"""
print("updated" if s.count(old) == 1 else "WARNING: line not found")
s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
