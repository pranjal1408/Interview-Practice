def unique(str):
    x=set()
    for i in str:
        if i in x:
            return False
        x.add(i)
    return True

x=unique("abc")
print x