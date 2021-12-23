s1 = 'ravi'
s2 = 'tejaghgh'

first = len(s1)
second = len(s2)

result = ''

i = 0
j = 0

if first>second:
    while i<second:
        result = result + s1[i]+s2[i]
        i+=1
    result = result+s1[second::]
else:
    while i<first:
        result = result + s1[i]+s2[i]
        i+=1
    result = result+s2[first::]
print(result)    


