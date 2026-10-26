import re
p = "index.html"
s = open(p, encoding="utf-8").read()
new = 'music: { src: "music/song.mp3", title: "Best Part", artist: "H.E.R. ft. Daniel Caesar" },'
s, n = re.subn(r'music: \{[^\n]*\},', new, s, count=1)
print("music updated" if n else "WARNING: music line not found")
open(p, "w", encoding="utf-8").write(s)
