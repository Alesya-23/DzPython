print("1 часть ДЗ")
x=0
while x < 100:
    x+=1
    if x%3==0 :
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    elif x%3==0 & x%5==0:
        print('FizzBuzz')
    else:
        print(x)


print("2часть ДЗ")
dict={b:b**3 for b in range(50)}
print("Cловарь старый вариант\n", dict, "\n")
dict2={}
for i in dict.keys():
	o={dict[i]:i}
	dict2.update(o)
dict=dict2
print("Новый словарь", dict2)


print("3 часть ДЗ")
m=[1,2,1,2,3,4,5]
l=[]
for i in m:
    if i not in l:
        l.append(i)
print(l)

