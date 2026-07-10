from PIL import Image, ImageDraw

def make_icon(size, filename, padding_ratio=0.22, maskable=False):
    img = Image.new('RGBA', (size, size), (0,0,0,0))

    bg = Image.new('RGBA', (size, size), (0,0,0,0))
    bgdraw = ImageDraw.Draw(bg)
    top = (31, 58, 46, 255)   # #1f3a2e
    bottom = (22, 40, 31, 255) # #16281f
    for y in range(size):
        t = y/size
        r = int(top[0]*(1-t) + bottom[0]*t)
        g = int(top[1]*(1-t) + bottom[1]*t)
        b = int(top[2]*(1-t) + bottom[2]*t)
        bgdraw.line([(0,y),(size,y)], fill=(r,g,b,255))

    mask = Image.new('L', (size,size), 0)
    mdraw = ImageDraw.Draw(mask)
    if maskable:
        mdraw.rectangle([0,0,size,size], fill=255)
    else:
        mdraw.rounded_rectangle([0,0,size,size], radius=int(size*0.22), fill=255)
    bg.putalpha(mask)
    img = Image.alpha_composite(img, bg)
    draw = ImageDraw.Draw(img)

    pad = size*padding_ratio
    usable = size - 2*pad
    cx, cy = size/2, size/2

    # paper airplane silhouette, pointed up-right, gold color
    gold = (217,164,65,255)
    gold_dim = (169,126,47,255)

    # main body triangle (nose to tail)
    p_nose = (cx + usable*0.42, cy - usable*0.40)
    p_tailL = (cx - usable*0.42, cy + usable*0.10)
    p_tailR = (cx - usable*0.06, cy + usable*0.42)
    p_center = (cx - usable*0.06, cy - usable*0.02)

    # left wing
    draw.polygon([p_nose, p_tailL, p_center], fill=gold)
    # right/bottom wing (slightly darker for depth)
    draw.polygon([p_nose, p_center, p_tailR], fill=gold_dim)

    # fold line
    draw.line([p_nose, p_center], fill=(22,40,31,180), width=max(2,int(size*0.012)))

    img.save(filename)
    print('saved', filename, size)

make_icon(192, '/home/claude/runway/icons/icon-192.png')
make_icon(512, '/home/claude/runway/icons/icon-512.png')
make_icon(512, '/home/claude/runway/icons/icon-512-maskable.png', padding_ratio=0.30, maskable=True)
make_icon(180, '/home/claude/runway/icons/apple-touch-icon.png')
make_icon(32, '/home/claude/runway/icons/favicon-32.png', padding_ratio=0.14)
