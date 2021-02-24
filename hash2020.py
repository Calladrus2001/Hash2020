# IMP: need to add remarks in the actual competition.
b,l,d = map(int,input().split())
s = list(map(int,input().split()))
lib = dict()
time = []
for x in range(l):
    nb,ts,maxb = map(int,input().split())
    ids = list(map(int,input().split()))
    lib[x] = [[nb,ts,maxb],ids]
    time.append([x,ts]) # GOT THE REQ INPUT 

# THE MECHANISM FOR SIGNING UP, SCANNING ETC STARTS HERE
sign = False
scan = False
count = 0
score = 0
d1 = 0 # this is current day
while d1 <= d:
    if sign == True:
        if scan == False:
            if count == 0:
                pass # only for the zeroeth lib. basically only for the first ever case
        elif scan == True:
            # scanning process continues. add score
            pass # temp
    elif sign == False:
        # enter code for selecting the next library where signing up takes min days.
        sign = True
        lib[x][ts] = lib[x][ts] - 1
        if lib[x][ts] == -1:
            #enter code to start scanning process. add score
            pass # temp
        else:
            pass
        if scan == True:
            # continue scanning process
            pass  # temp
        elif scan == False:
            # two possibilities here, (a) there is a signed up lib with books remianing to be scanned .
            # (b) no books remaining to be scanned, meaning that from a recently signed up lib, all books scanned.

    d1+=1    
# how to choose which books to scan from which lib ?