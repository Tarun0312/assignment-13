# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
# "Javascript", "Python"]

thisList=["Java","SQL",'C','Reactnative','Javascript','Python']

print(thisList)
i=0
while(i<len(thisList)):
    if(thisList[i]=='SQL'):
        thisList[i]="NOSQL"
    if(thisList[i]=="Reactnative"):
        thisList[i]='Flutter'
    i+=1        

print(thisList)