import re
p = "index.html"
s = open(p, encoding="utf-8").read()

# 1. Remove the button from the main page
n1 = s.count('<button class="btn ghost" id="btnReasons">Why I love you</button>')
s = s.replace('<button class="btn ghost" id="btnReasons">Why I love you</button>\n', '')
s = s.replace('<button class="btn ghost" id="btnReasons">Why I love you</button>', '')
print("button removed" if n1 else "WARNING: button not found")

# 2. Remove the "Why I love you" panel
s, n2 = re.subn(r'<div id="reasons" class="overlay".*?</div>\n  </div>\n</div>\n', '', s, count=1, flags=re.S)
print("panel removed" if n2 else "WARNING: panel not found")

# 3. Remove its click wiring
s = s.replace("$('btnReasons').addEventListener('click', () => openOverlay('reasons'));\n", '')
s = s.replace("buildReasons();\n", '')

open(p, "w", encoding="utf-8").write(s)
print("Saved index.html")
