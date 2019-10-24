PRI=0
SEG=1
I=3
for v in range (2,180,I):
    SIG=PRI+SEG
    PRI=SEG
    SEG=SIG
    I+=1
print(SIG)
