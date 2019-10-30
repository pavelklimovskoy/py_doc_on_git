from PIL import Image
im = Image.open('sad.png')
n, p, k = 0, 0, 0
m=5
while k < (360 / m):
    k = k + 1
    p = p + m
    n = n + 1 
    s = str(n) + '.png'
    out = im.rotate(p)
    out.save(s)
    print(k)
