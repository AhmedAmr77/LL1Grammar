import itertools

d={'S':'ABc','A':['bA',''],'B':'c'}
#print d.get('A')[1]
lB=['c']
lA=[['b','A'],[]]
lS=[lA,lB,'c']
l=[lS,lA[0],lA[1],lB]
ll=[['S', 'ABc'], ['A', 'bA'], ['A', ''], ['B', 'c']]
BDW=[]
BW=[]
sym=[]
First=[]
FHS=[]
FDB=[]
DEO=[]
EO=[]
FB=[]

FOL=[]
SEL=[]
print ll

#S1
x=0
for i in l:
    x=x+1
    if not i:
        nullRule=x
        nullNonTer=ll[x-1]
print nullNonTer,nullRule

#S2
for i in ll:
    non=i[0]
    ter=i[1]
    if len(ter)>=1:
        ter=ter[0]
    else :
        continue
    BDW.append(non+'  BDW  '+ter)

    if ter == nullNonTer[0]:    #if ter is nullable nonTer
        if len(i[1])>1:
            ter=i[1][1]
            BDW.append(non+'  BDW  '+ter)
print BDW

#S3
for i in BDW:
    bw=str(i)
    bw=bw.replace('BDW','BW')
    BW.append(bw)

for i,j in itertools.combinations(BW,2):
    bw1=str(i)
    bw2=str(j)
    ch1=bw1[-1]
    ch2=bw2[0]
    if ch1==ch2:
        BW.append(bw1[0]+'  BW  '+bw2[-1])

for i in ll:
    for j in i:
        if j == '':
            continue
        ch=j[0]
        bw=ch+'  BW  '+ch
        if bw not in BW:
            BW.append(ch+'  BW  '+ch)
            sym.append(ch)
print BW

#S4
for i in ll:
    if not i[1]:
        continue
    frs=str(i[1])
    ch=frs[0]
    if ch.islower():
        First.append('First('+i[0]+') = {'+frs[0]+'}')
    else :
        for j in ll:
            if not j[1]:
                continue
            fr=str(j[0])
            if fr[0]==ch:
                new=str(j[1])
                char=new[0]
                First.append('First('+i[0]+') = {'+'b,c'+'}')
for i in sym:
    ch=str(i)
    if ch.islower():
        First.append('First('+ch+') = {'+ch+'}')
print First

#S5
for i in ll:
    rs=str(i[1])
    if not rs:
        FHS.append("First(E) = {}")
    else :
        if rs[0].islower():
            FHS.append('First('+rs+') = {'+rs[0]+'}')
        else :
            FHS.append('First(ABc) = {b,c}')
print FHS

#S6
for i in ll:
    fdb=str(i[1])
    for j in range(len(fdb)):
        if j+1==len(fdb):
            continue
        if fdb[j].isupper():
            FDB.append(fdb[j]+'  FDB  '+fdb[j+1])
print FDB

#S7
for i in ll:
    deo1=str(i[0])
    deo2=str(i[1])
    if not deo2:
        continue
    DEO.append(deo2[-1]+'  DEO  '+deo1)
    if deo2[-1]==nullNonTer[0]:
        DEO.append(deo2[-2]+'  DEO  '+deo1)
print DEO

#S8
for i in DEO:
    bw=str(i)
    bw=bw.replace('DEO','EO')
    EO.append(bw)

for i,j in itertools.combinations(EO,2):
    bw1=str(i)
    bw2=str(j)
    ch1=bw1[-1]
    ch2=bw2[0]
    if ch1==ch2:
        EO.append(bw1[0]+'  EO  '+bw2[-1])

for i in ll:
    for j in i:
        if j == '':
            continue
        ch=j[0]
        bw=ch+'  EO  '+ch
        if bw not in EO:
            EO.append(ch+'  EO  '+ch)
print EO

#S9
for i in EO:
    eo=str(i)
    for j in FDB:
        fd=str(j)
        if eo[-1]==fd[0]:
            for k in BW:
                bw=str(k)
                if fd[-1]==bw[0]:
                    FB.append(eo[0]+'  FB  '+bw[-1])
print FB

#S10
for i in EO:
    ex=str(i)
    if ex[0].isupper():
        if ex[-1]=='S':
            FB.append(ex[0]+'  EO  <-|')
print FB

#S11
for i in FB:
    fb=str(i)
    if fb[0]==nullNonTer[0]:
        if fb[-1].islower():
            FOL.append('Fol('+fb[0]+')={'+fb[-1]+'}')
print FOL

#S12
n=0
for i in FHS:
    sel=str(i)
    n=n+1
    nn=str(n)
    if n==nullRule:
        f=str(FOL[0])
        SEL.append('sel('+nn+')='+sel+' U '+f+'={'+f[-2]+'}')
        continue
    SEL.append('sel('+nn+')='+sel)
print SEL
