# LIST TASK 1
name = int(input('Введите размер списка '))
list = []
for i in range(name):
    a = int(input('Введите число '))
    list.append(a)
print(list)
print(max(list))


# FIND A WORD IN A LIST
list = ["Windows", "Macos", "ios", "android", "linux"]
user_input = input("Введите слов ")
for i in range(len(list)):
     if list[i] == user_input:
        print('Слово найдено')
     else:
        print('Слово не найдено')

# FIND A WORD IN A LIST 2
list = ["Windows", "Macos", "ios", "android", "ada"]
user_input = input("Введите слов ")
for i in range(0,4):
    if list[0] == user_input or list[1] == user_input or list[2] == user_input or list[3] == user_input:
        print('Слово найдено')
    else:
        print('Слово не найдено')


# COUNTER AND LIST TASK
list = [-3, 20, 0, -9, 100]
result = 0
for i in list:
    if i > 0:
     result +=i
print(result)


# COUNTER AND LIST TASK 2
list = [100, 90, 80, 70, 60, 50,55,75,66]
number_input = int(input('Введите цифра '))
result = 'Цифра не найдено'
for i in range(len(list)):
    if number_input == list[i]:
        result = 'Цифра найдено'
print(result)


# LIST AND CYCLE TASK 1
list = [-3, 20, 0, -9, 100, -9]
for i in list:
    if i < 0:
     index = list.index(i)
     list[index] = 0
print()


# LIST AND CYCLE TASK 2
list=[7, -3,9, -11,18,99,2,11]
a = 0
b = 0
for i in list:
    if i > a:
        a = i

    if i < b:
        b = i
print(a)
print(b)


# LIST AND CYCLE TASK 3
list=[7, -3,9, -11,18,99,2,11]
list1=[]
list2=[]
a=len(list)
for i in range(0,a):
    if list[i]>0:
        list1.append(list[i])
print('Оң сандар: ',len(list1))
for i in range(0,a):
    if list[i]<0:
        list2.append(list[i])
print('Теріс сандар: ',len(list2))


# LIST AND CYCLE TASK 4
list=[7, -3,9, -11,18,99,2,11]
for i in range(1,len(list), 2):
    print(i)

# lIST AND SET TASK 1
list_number = [1, 2, 2, 3, 4, 5, 2]
unique_list = list(set(list_number))
print(unique_list)


