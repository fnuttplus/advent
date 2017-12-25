from hashlib import md5

def doors(h,p):
    x,y = p
    if y-1 >= 0 and h[0] in "bcdef": yield 'U',(x,y-1)
    if y+1 <= 3 and h[1] in "bcdef": yield 'D',(x,y+1)
    if x-1 >= 0 and h[2] in "bcdef": yield 'L',(x-1,y)
    if x+1 <= 3 and h[3] in "bcdef": yield 'R',(x+1,y)

def bfs():
    global longest
    s = [('',(0,0))]
    while s:
        ns = []
        for path,pos in s:
            if pos == (3,3): #return path
                longest = len(path)
                continue
            h = md5(("gdjjyniy"+path).encode()).hexdigest()
            for d,p in doors(h,pos): ns.append((path+d, p))
        s = ns

def dfs(path,pos):
    global longest
    if pos == (3,3):
        if len(path) > longest: longest = len(path)
        return
    h = md5(("gdjjyniy"+path).encode()).hexdigest()
    for d,p in doors(h,pos): dfs(path+d, p)

longest = 0
print(bfs())
dfs('',(0,0))
print(longest)
