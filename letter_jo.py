import re
p = "index.html"
s = open(p, encoding="utf-8").read()

paragraphs = [
    "Happy 23th monthsary Jo hehe. Iloveyou so much Jo hehe.",
    "Sorry kaayu Jo kani sa akong ma hatag og ma provide saimo nga greetings Jo, sensya kaayu hehe. Saon taman walang wala man kayko sensya kayo Jo. And also sorry for everything sab Jo, kanang usahay burden kos imoha. Sensya kaayu unta napa japon ka hangtod sa mo lambo ta antos lang sa ron Jo ha. Lisod paman jud kayko, I know. Nakay mga gusto nga pampaliton, di nako halos ma hatag. Sensya kaayu unta naka sabot kas situation namo hehe. Sorry sab sakong mga kakulangan Jo, pero promise og paburan kos Ginoo, bawi kog daghan saimo untag paboran jud.",
    "And also sorry sab Jo og nay time nga dili ko vocal saimo when it comes sa mga away away or unsa ba hehe. Sensya kaayu. Pero thank you sa tanan tanan Jo. Thank you kay kauban japon tika hangtod ron maskig ga struggles mi sa akong fam. Thank you sa mga sacrifices nga imong gi hatag og gi buhat Jo. Thank you kaayu, na appreciate jud nako tanan Jo.",
    "And i love you always Jo hehe. Thank you thank you jud kaayu Jo. Stay pretty Jo. Iloveyouu, narako diri always ha. Mwaaa. Iloveyou so much......",
]

# Build the new letter block, escaping for a JavaScript string
def js(t):
    return '"' + t.replace('\\', '\\\\').replace('"', '\\"') + '"'
block = "letter: [\n    " + ",\n    ".join(js(t) for t in paragraphs) + "\n  ],\n  signature"

new_s, n = re.subn(r"letter: \[.*?\],\n  signature", block, s, count=1, flags=re.S)
print("Letter replaced" if n == 1 else "WARNING: letter block not found")
open(p, "w", encoding="utf-8").write(new_s)
