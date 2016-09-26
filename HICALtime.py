def Hi_cal(l):
    #[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    #[(2,4),(1,5)]
    start=l[0][0]
    stop=l[0][1]
    i=1
    while i<len(l):
        if l[i][0]>=start and l[i][0]<=stop and l[i][1]>=stop:
            stop=l[i][1]
            l.remove(l[i-1])
            l[i-1]=(start,stop)
            i=i-1
        elif l[i][0]>=start and l[i][0]<=stop and l[i][1]<stop:
            l.remove(l[i-1])
            l[i-1]=(start,stop)
            i=i-1
        elif l[i]>=start and l[i][0]>stop:
            start=l[i][0]
            stop=l[i][1]
        elif l[i][0]<start:
            l[i-1],l[i]=l[i],l[i-1]
            start=l[i-1][0]
            stop=l[i-1][1]
            if l[i][0]>=start and l[i][0]<=stop and l[i][1]>=stop:
                stop=l[i][1]
                l.remove(l[i-1])
                l[i-1]=(start,stop)
                i=i-1
            elif l[i][0]>=start and l[i][0]<=stop and l[i][1]<stop:
                l.remove(l[i-1])
                l[i-1]=(start,stop)
                i=i-1
            elif l[i]>=start and l[i][0]>stop:
                start=l[i][0]
                stop=l[i][1]
        i=i+1
    return l
