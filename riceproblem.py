import math

rememberedStuff = {0: 1}

def bigMod(base,exp,m):
    rememberedStuff[exp] = (base%m*rememberedStuff[exp-1])%m
    del rememberedStuff[exp-1]
    return rememberedStuff[exp]

# special modulo function that returns (1+r+r^2+r^3....+r^(n-1))%m
def sMod(R, N, M):
    modsum = 1
    for i in range(1, N):
        modsum += bigMod(R,i,M)
    return modsum % M

f = open("input-riceboard-2b51.txt")
g = open("output.txt", "w")
T = int(f.readline())
for t in range(T):
    rememberedStuff = {0:1}
    [R, N, M] = f.readline().split()
    R = int(R)
    N = int(N)
    M = int(M)
    ans = sMod(R,N*N,M)
    print("Case #" + str(t+1) + ": " +str(ans))
    g.write("Case #" + str(t+1) + ": " +str(ans) + "\n")
print("done!")