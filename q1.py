# 1. Write a python script to store multiple items in a single variable ( Items are “Java”
# ,“Python”, “SQL”, “C” ) using list

l1=["Java","Python","SQL",'C']

print(l1)
for i in l1:
    print(i,end=' ')
    
print()
j=0    
while(j<len(l1)):
    print(l1[j],end=' ')  
    j+=1  