#2.1
f = open('kttekst.txt','r+')
p = f.read() 
words = p.split()
sõnadearv = len(words)
print("Sõnade arv failis on:")
print(sõnadearv)

#2.2
print('Nii paljudes sõnades on vähem kui 5 tähte:')
for item in words:
        if len(item) > 4:
          
