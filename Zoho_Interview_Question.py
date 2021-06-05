#input :a4d5f7
#output: aaaadddddfffffff

#code:
def result(n=[],*args):
    for i in range(len(n)):
        if n[i].isalpha():
            print(n[i]*int(n[i+1]),end="")
        


m=list(input().strip())
result(m)
