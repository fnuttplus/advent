from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

#ll = stdin.read().splitlines()
ll = get_data(day=10).splitlines()

s = 0
c = 0
x = 1

def cycle1():
    global c,x,s
    c += 1
    if c%40==20:
        print(c,x)
        s += c*x

r = 0
p = []
def cycle2():
    global c,x,r
    print('#' if abs(c-x) < 2 else '.', end='')
    #if abs(c-x) < 2: p.append((c,r))
    #image = Image.new('L', (40, 6))
    #if 0 <= x-1 < 40: image.putpixel((x-1,r),150)
    #if 0 <= x+1 < 40: image.putpixel((x+1,r),150)
    #if 0 <= x < 40: image.putpixel((x,r),150)
    #for pc,pr in p: image.putpixel((pc,pr),250)
    c += 1
    if c == 40:
        c = 0
    #    r += 1
        print()
    #image.putpixel((c,r),50)
    #image = image.resize((40*35,6*50), Image.Resampling.NEAREST)
    #image.save("frames/10_"+str(r*40+c)+".png")

for l in ll:
    if l == 'noop':
        cycle2()
    else:
        v = int(l.split(' ')[1])
        cycle2()
        cycle2()
        x += v

#print(s)
#ZCBAJFJZ
