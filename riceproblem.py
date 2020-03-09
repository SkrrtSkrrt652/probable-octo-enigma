import math

rememberedStuff = {}

#big mod for numbers with exponents that are a power of 2
def bigModb2(base, exp, m):
    if(exp == 1):
        return base % m
    else:
        if ((base, exp) in rememberedStuff):
            return rememberedStuff[(base,exp)]
        else:
            answer = (pow(bigModb2(base,exp/2,m),2))%m
            rememberedStuff[(base,exp)] = answer
            return answer

def bigMod(base,exp,m):
    expList = []
    while exp > 0:
        expList.append(pow(2,math.floor(math.log(exp,2))))
        exp -= expList[len(expList)-1]
    modNum = 1
    print(expList)
    for thing in expList:
        modNum *= bigModb2(base,thing,m)
    return modNum % m


# special modulo function that returns (1+r+r^2+r^3....+r^(n-1))%m
def sMod(R, N, M):
    modsum = 0
    for i in range(N):
        modsum += bigMod(R,i,M)
    return modsum % M

f = open("input-riceboard-8544.txt")
g = open("output.txt", "w")
T = int(f.readline())
for t in range(T):
    rememberedStuff = {}
    [R, N, M] = f.readline().split()
    R = int(R)
    N = int(N)
    M = int(M)
    print("Case #" + str(t+1) + ": " +str(sMod(R,N*N,M)))
    g.write("Case #" + str(t+1) + ": " +str(sMod(R,N*N,M)) + "\n")
print("done!")