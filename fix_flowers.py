import os
from PIL import Image
from rembg import remove

SRC = "flowers"
DST = os.path.join("assets", "flowers")
PREV = os.path.join(DST, "preview")
os.makedirs(PREV, exist_ok=True)

def clean_neutral(im):
    # Fallback for a checkerboard baked into an opaque image: remove gray/white
    # pixels connected to the outer edge. Colored petals are never touched.
    W, H = im.size
    px = im.load()
    def is_bg(x, y):
        r, g, b, a = px[x, y]
        return min(r, g, b) > 200 and max(r, g, b) - min(r, g, b) < 22
    seen = set()
    stack = [(x, y) for x in range(W) for y in (0, H - 1)] + [(x, y) for y in range(H) for x in (0, W - 1)]
    while stack:
        x, y = stack.pop()
        if x < 0 or y < 0 or x >= W or y >= H or (x, y) in seen:
            continue
        seen.add((x, y))
        if not is_bg(x, y):
            continue
        r, g, b, a = px[x, y]
        px[x, y] = (r, g, b, 0)
        stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return im

for n in range(1, 7):
    src = os.path.join(SRC, f"flower{n}.webp")
    if not os.path.exists(src):
        print(f"flower{n}.webp not found, skipped")
        continue
    original = Image.open(src).convert("RGBA")
    out = remove(original).convert("RGBA")
    total = out.width * out.height
    transparent = sum(1 for v in out.getchannel("A").getdata() if v < 10) / total
    if transparent < 0.05:
        print(f"flower{n}: AI removal left a background, using edge cleanup")
        out = clean_neutral(original.copy())
        transparent = sum(1 for v in out.getchannel("A").getdata() if v < 10) / total
    box = out.getbbox()
    if box:
        out = out.crop(box)
    out.thumbnail((900, 900), Image.LANCZOS)
    out.save(os.path.join(DST, f"flower{n}.png"), optimize=True)
    preview = Image.new("RGBA", out.size, (59, 7, 16, 255))
    preview.alpha_composite(out)
    preview.convert("RGB").save(os.path.join(PREV, f"preview{n}.png"))
    print(f"flower{n}: saved, about {transparent:.0%} transparent")
print("Done. Check the images in assets\\flowers\\preview")
