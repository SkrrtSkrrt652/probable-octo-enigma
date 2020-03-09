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
    for thing in expList:
        modNum *= bigModb2(base,thing,m)
        modNum = modNum % m
    return modNum % m


# special modulo function that returns (1+r+r^2+r^3....+r^(n-1))%m
# if a[n] = 1 + r + r^2 + ...... + r^(n-2) + r^(n-1)
# then a[j + k] = r^j*a[k] + a[j]
# it follows that a[2n] = (r^n+1)a[n]
#            thus a[n]  = (r^(n/2) + 1)a[n/2], if n is even 
#                 a[n]  = (r^((n+1)/2)+1)a[(n-1)/2] + r^((n-1)/2), if n is odd 
# We use this notion to recursively define a modulus operator for a geometric series below
def sMod(R, N, M):
    if(N == 1):
        return 1
    if(N%2 == 0):
        prefactor = bigMod(R,N//2,M)+1
        return ((prefactor % M)*sMod(R,N//2,M))%M
    else:
        exp = (N-1)//2
        prefactor = bigMod(R,exp+1,M)+1
        return (((prefactor % M) * sMod(R,exp,M)) % M + bigMod(R,exp,M)) % M

def main(): 
    global rememberedStuff
    f = open("input-riceboard-d973.txt")
    g = open("output.txt", "w")
    T = int(f.readline())
    for t in range(T):
        rememberedStuff = {}
        [R, N, M] = f.readline().split()
        R = int(R)
        N = int(N)
        M = int(M)
        g.write("Case #" + str(t+1) + ": " +str(sMod(R,N*N,M)) + "\n")
    print("done!")

main()
