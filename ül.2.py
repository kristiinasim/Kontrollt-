#2.1
f = open('kttekst.txt','r+')
p = f.read() 
words = p.split()
sõnadearv = len(words)
print("Sõnade arv failis on:")
print(sõnadearv)

#2.2

num_x = 0
f = open('kttekst.txt','r+')
for line in f:
    wordss = line.split()
for s in wordss:
    if len(s) < 5:
        num_x += len(s)
print("Sõnu, milles on vähem kui 5 tähte on nii palju:")
print(num_x)
                        

        
