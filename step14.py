'''
#143
a = int(input("Enter the num: "))
if(a%2 == 0):
    print("even num")
else:
    print("odd num")
''' 
'''
#144
b = input("enter the num")
num = 118 - int(b[0:2])
if(65<=num):
    print("old")
'''
'''
#145
num = 13
if(num%2 == 0) or (num%3 == 0):
    print(True)
else:
    print(False)
'''
'''
#148
year = int(input("year : "))
if(year % 4 == 0):
    if(year % 400 == 0):
        print("윤년")
    elif(year % 100 == 0):
        print("평년")
    else:
        print("윤년")
else:
    print("평년")
'''
'''
#149-2
a,b,c=input("3 num").split()
a= int(a)
b= int(b)
c=int(c)

max = max(a,b,c)
min = min(a,b,c)

for i in a,b,c:
    if i != max and i != min:
        mid = i
        break

print(max * min - mid)
'''
'''
#150 (50,40) (50,80), (100,40),(100,80) x = 100~50, y = 80~40
a,b = input("x,y: ").split()
a=int(a)
b=int(b)

if(a>50 and a<100)and(b>40 and b<80):
    print("in")
'''
'''
#151
a= input("")

if a[0] in 'aeiou':
    print("good")
else:
    print("bad")
'''
#153
a= int(input("1st num: "))
b = int(input("2nd num: "))

print("Nice" if a + b >= 0.5*a*b else "Bad")