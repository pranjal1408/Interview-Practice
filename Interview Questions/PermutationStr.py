def isPermutation(str,str2):
    if len(str)!= len(str2):
        return False
    count1={}
    count2={}
    for char in str:
        if char in count1.keys():
            count1[char] += 1
        else:
            count1[char]=1
    for char1 in str2:
        if char1 in count2.keys():
            count2[char1] += 1
        else:
            count2[char1]=1

    for i in count1.keys():
        if i not in count2.keys():
            return False
        elif count1[i]!=count2[i]:
            return False
        else:
            return True

x=isPermutation("abc","aac")
print x
