BAND="T"
SUMSER=0
I=2
while (I<=1800):
    SUMSER+=I
    print(I)
    if BAND=="T":
        BAND="F" 
        I+=3
    else:
        BAND="T"
        I+=2
print(SUMSER)
