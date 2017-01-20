def pallperm(str):
    str=str.lower()
    counts={}
    for i in str:
        if i in counts.keys():
            counts[i]+=1
        else:
            counts[i]=1
    #print counts
    even_counts=0
    odd_counts=0
    for i in counts.keys():
        if i != " ":
            if counts[i]%2==0:
                even_counts+=1
            elif counts[i]%2==1:
                odd_counts+=1
    #print even_counts, odd_counts
    if(odd_counts>1):
        return False
    else:
        return True

x=pallperm("Tact Coa")
print x