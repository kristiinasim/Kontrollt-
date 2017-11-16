num1 = int(input("Palun sisestage esimene arv:"))
num2 = int(input("Palun sisestage teine arv:"))
print ('Paarisarvud on:')
for x in range (num1, num2):
    if (x % 2) == 0:
        print(x)
