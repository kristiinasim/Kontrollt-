print('Siin on list nr.1:')
first_list = (11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24)
print(first_list)
print('Siin on list nr. 2:')
second_list = (5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7)
print(second_list)

##3.1
print('Sarnasused on:')

new_list = []
for element in first_list:
    if element in second_list:
        new_list.append(element)
print(new_list)
      

##3.2
maxoftwo = max(max(first_list), max(second_list))
print('Suurim number kahest listist on:')
print(maxoftwo)

##3.3
minoftwo = min(min(first_list), min(second_list))
print('Väikseim number kahest listist on:')
print(minoftwo)

##3.4
print('Esimese listi keskmine on:')
a = sum(first_list)/len(first_list)
print(a)


print('Teise listi keskmine on:')
b = sum(second_list)/len(second_list)
print(b)

##3.5

print('Kahe listi keskmine on kokku:')
x = (first_list)+(second_list)
y = (first_list)+(second_list)
c = sum(x)/len(y)
print(c)
