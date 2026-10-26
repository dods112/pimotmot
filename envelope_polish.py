p = "index.html"
s = open(p, encoding="utf-8").read()

def rep(old, new):
    global s
    n = s.count(old)
    print(("OK " if n == 1 else f"WARNING ({n} matches) ") + old[:60].replace("\n", " "))
    s = s.replace(old, new)

# 1. Remove the message and the heart button from the face of the envelope
rep('<div class="card rv" style="--d:.9s">',
    '<div class="card rv envCard" id="envCard" role="button" tabindex="0" aria-label="Open the letter" style="--d:.9s">')
rep('      <p class="for" id="forLine"></p>\n      <p class="msg" id="cardMsg"></p>\n      <button class="heartBtn" id="heartBtn" aria-label="Send a burst of petals">♥</button>\n      <p class="tapHint">Tap to open</p>',
    '      <div class="envFace">\n        <span class="envWax">♥</span>\n        <p class="tapHint">Tap to open</p>\n      </div>\n      <button class="heartBtn" id="heartBtn" aria-label="Send a burst of petals">♥</button>')

# 2. New envelope styles (replaces the earlier flap styles)
import re
s = re.sub(r"/\* Card envelope \*/.*?\.tapHint\{[^}]*\}\n", "", s, flags=re.S)
ENV_CSS = """/* Envelope card */
.envCard{position:relative;width:min(88vw,460px);height:min(58vw,280px);max-height:300px;min-height:200px;padding:0;border-radius:6px;background:linear-gradient(160deg,#fbf0d8,#f1dcb0);box-shadow:0 18px 36px rgba(0,0,0,.55),inset 0 0 0 1px rgba(255,255,255,.35);cursor:pointer;overflow:visible;transition:transform .4s ease,box-shadow .4s ease}
.envCard:hover{transform:translateY(-3px)}
.envCard::before{content:"";position:absolute;inset:0;border-radius:6px;background:repeating-linear-gradient(35deg,rgba(150,110,50,.04) 0 2px,transparent 2px 6px);pointer-events:none}
.envCard::after{content:"";position:absolute;left:0;right:0;top:0;height:50%;background:linear-gradient(#f0dcaa,#dfc386);clip-path:polygon(0 0,100% 0,50% 100%);border-radius:6px 6px 0 0;transform-origin:top center;transition:transform .9s cubic-bezier(.3,.7,.3,1),z-index 0s .4s;z-index:2;pointer-events:none;box-shadow:0 2px 6px rgba(0,0,0,.12)}
.envCard.open::after{transform:rotateX(180deg);z-index:0}
.envFace{position:absolute;left:0;right:0;bottom:14%;display:flex;flex-direction:column;align-items:center;gap:.5rem;z-index:3;pointer-events:none}
.envWax{width:52px;height:52px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#d24a66,#8a1630);color:var(--ivory);display:flex;align-items:center;justify-content:center;font-size:1.2rem;box-shadow:0 4px 10px rgba(0,0,0,.35)}
.tapHint{font-style:italic;font-size:1rem;letter-spacing:.08em;color:#8a4a58}
.envCard:focus-visible{outline:2px solid var(--gold);outline-offset:5px}
.envCard .heartBtn{display:none}
"""
rep("/* Music */", ENV_CSS + "\n/* Music */")

# 3. Keep the floating heart button working on the main page, away from the envelope
rep(".heartBtn{position:absolute;right:12px;bottom:-18px;",
    ".heartBtn{position:fixed;right:14px;bottom:calc(14px + var(--sb));z-index:12;")

open(p, "w", encoding="utf-8").write(s)
print("Saved index.html")
