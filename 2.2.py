f = open('kttekst.txt','r+')
p = f.read() 
words = p.split()
print('Neis sõnades on vähem kui 5 tähte:')
for each in words:
     if len(each) < 5:
         print(each)
