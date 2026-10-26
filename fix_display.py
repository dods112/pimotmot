p = "index.html"
s = open(p, encoding="utf-8").read()

old1 = 'cardMessage: "[A short personal message about why she is special to you.]",'
new1 = 'cardMessage: "Happy 23 months, Jo. I love you always.",'
print("card message OK" if s.count(old1) == 1 else "card message NOT FOUND")
s = s.replace(old1, new1)

old2 = 'const rx = (ph ? 0.46 : 0.34) * W, ry = (ph ? 0.38 : 0.40) * H;'
new2 = 'const rx = (ph ? 0.48 : 0.34) * W, ry = (ph ? 0.52 : 0.40) * H;'
print("open zone OK" if s.count(old2) == 1 else "open zone NOT FOUND")
s = s.replace(old2, new2)

open(p, "w", encoding="utf-8").write(s)
print("Saved")
