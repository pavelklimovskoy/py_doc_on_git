from PIL import Image
im = Image.open('sad.png')
n=0
m=5
p=0
k=0
while k<(360/m) :
    k=k+1
    p=p+m
    n=n+1
    s= str(n) + '.png'
    out = im.rotate(p)
    out.save(s)
    print(k)
