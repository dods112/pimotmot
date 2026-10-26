p = "index.html"
s = open(p, encoding="utf-8").read()

def rep(old, new):
    global s
    n = s.count(old)
    print(("OK " if n == 1 else f"WARNING ({n} matches) ") + old[:60].replace("\n", " "))
    s = s.replace(old, new)

# 1. The card becomes a clickable envelope
rep('<div class="card rv" style="--d:.9s">',
    '<div class="card rv envCard" id="envCard" role="button" tabindex="0" aria-label="Open the letter" style="--d:.9s">')
rep('<p class="msg" id="cardMsg"></p>',
    '<p class="msg" id="cardMsg"></p>\n      <p class="tapHint">Tap to open</p>')

# 2. Styles for the envelope flap
rep('/* Music */',
'''/* Card envelope */
.envCard{cursor:pointer;overflow:visible}
.envCard::before{content:"";position:absolute;left:0;right:0;top:0;height:46%;background:linear-gradient(#f0dcaa,#e2c48a);clip-path:polygon(0 0,100% 0,50% 100%);border-radius:6px 6px 0 0;transform-origin:top center;transition:transform .8s ease;z-index:2;pointer-events:none}
.envCard.open::before{transform:rotateX(180deg)}
.envCard:focus-visible{outline:2px solid var(--gold);outline-offset:4px}
.tapHint{margin-top:.8rem;font-style:italic;font-size:.95rem;color:#8a4a58;letter-spacing:.06em}

/* Music */''')

# 3. Tapping the card opens the letter and its envelope
rep('// ===== Boot =====',
'''// ===== Card envelope opens the letter =====
function openFromCard() {
  const c = $('envCard');
  c.classList.add('open');
  $('envelope').classList.remove('open', 'gone');
  $('sheet').classList.remove('show');
  openOverlay('letter');
  setTimeout(openEnvelope, 700);
}
$('envCard').addEventListener('click', e => {
  if (e.target.closest('.heartBtn')) return;
  openFromCard();
});
$('envCard').addEventListener('keydown', e => {
  if ((e.key === 'Enter' || e.key === ' ') && !e.target.closest('.heartBtn')) { e.preventDefault(); openFromCard(); }
});

// ===== Boot =====''')

open(p, "w", encoding="utf-8").write(s)
print("Saved index.html")
