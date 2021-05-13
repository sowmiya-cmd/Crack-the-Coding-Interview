//To print the High Scoring batsman name 

//Sample input:
    sowmiya,90
    hariharan,56
    giridharan,78
    gokul,34
    
//Sample Output :
    sowmiya

CODE:
    
n=int(input())

batsman={}

for i in range(n):
    
    batsman[i]={}
    t=input().split(',')
    batsman[i]['name']=t[0]
    batsman[i]['score']=int(t[1])
    
temp={'name':batsman[0]['name'],'score':batsman[0]['score']}


for i in batsman:
    if(batsman[i]['score']>=temp['score']):
        temp['name']=batsman[i]['name']
        temp['score']=batsman[i]['score']
print(temp['name'])
