#Задача 1
number = int("".join(input() for _ in range(8)))
print(number)

#Задача 2
n = int(input())
names = []
for i in range(n):
    names.append(input())
for i in range(n):
    print(i+1, names[i])

#Задача 3
import datetime
t = datetime.date.today()
m,n=5,13
t = datetime.date(t.year, t.month, n)
k=int((31-n)/m)+1
for i in range(k) : print ((t+datetime.timedelta(days=i*m)).day, end =" ")

#Задача 4
a, count, max_count = input(), 0, 0
for _ in range(int(input())):
    if input() == a:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
else:
    if count > max_count:
        max_count = count
print(max_count)

#Задача 5
num = int(input())
summ = 0
for i in range(1, num):
    if num % i == 0:
        summ += i
print(summ)

#Задача 6
vowels = 'аяоёэеуюыи'
line = input()
v = k = z = 0
n = 1
for w in line:
    if w in vowels :
        if  n :
            z += 1
        k += 1
        n = 0
    elif w == ' ' :
        n = 1
        if k :
            v += k
            k = 0
print(v - z + k)

#Задача 7
vowels = 'aeiuy'
word,n = (input("Введите слово: ")),int((input("Введите число: ")))
for i in range(1,n + 1): print((word + ' ') * i)

#Задача 8
a=input('Введите номер телефона:')
b='+1234567890'
c=0
for i in a:
 if i in b:
  c+=1
if c!=len(a):
 print('Неправильный номер телефона!')

#Задача 9
word = input( 'палоль: ' )
print( ''.join( [ '0' if x in 'аеёиоуыэюя' else '1' for x in word ] ) )

#Задача 10
message =  '''ППррииввеетт!! ККаакк ддееллаа?? ССееггоодднняя ттааккааяя ххоорроошшааяя ппооггооддаа, ммоожжеетт ппооггуулляяеемм??'''
for i in range(len(message)):
   if message[i] == ' ' or i % 2 == 0:
       print(message[i], sep='', end='')