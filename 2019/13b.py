from vm import Computer
from PIL import Image, ImageDraw, ImageFont

comp = Computer(input(), False)
comp.ins[0] = 2
comp.mod(0, 75, 2)
comp.mod(1, 18*38+639+1, 36)
comp.start()
c = {}
paddle = None
i = 0
score = 0
while True:
    q0 = comp.outq.get()
    if q0 == None: break
    q1 = comp.outq.get()
    q2 = comp.outq.get()
    if q0 == -1 and q1 == 0: score = q2
    else:
        if q2 == 0: c[(q0,q1)] = " "
        if q2 == 1: c[(q0,q1)] = "#"
        if q2 == 2: c[(q0,q1)] = "="
        if q2 == 3: c[(q0,q1)] = "_"
        if q2 == 4: c[(q0,q1)] = "o"

    if False:
        txt = Image.new('RGB', (38*8,20*8), (0,0,0))
        fnt = ImageFont.truetype('lucon.ttf', 10)
        d = ImageDraw.Draw(txt)
        for y in range(20):
            for x in range(38):
                if (x,y) in c:
                    if c[(x,y)] == "#":
                        d.rectangle([(x*8,y*8), (x*8+8,y*8+8)], fill=(60,60,60), outline=(70,70,70))
                    elif c[(x,y)] == "=":
                        d.rectangle([(x*8,y*8), (x*8+8,y*8+8)], fill=(200-10*y,20,20), outline=(90,10,10))
                    elif c[(x,y)] == "o":
                        d.ellipse([(x*8,y*8), (x*8+8,y*8+8)], fill=(30,140,30), outline=(10,90,10))
                    elif c[(x,y)] == "_":
                        d.rectangle([(x*8,y*8), x*8+8,y*8+3], fill=(50,50,170), outline=(30,30,150))
        d.text((1,0), "Score: "+str(score), font=fnt, fill=(255,255,255))
        txt.save("frames/advent13_"+str(i).zfill(5)+".png", "PNG")
        i += 1

print(score)
