def factorial(number):
    if number!=1: return ((number)*(factorial(number-1)))
    else: return number
    
def combinations(number):
    size=len(number)
    solution_count = factorial(size)
    combi = []
    combi.append(number)
    i=0
    while i<solution_count:
        j=1
        while j<size:
            temp=combi[i].copy()
            t=temp[j]
            temp.pop(j)
            temp.insert(0, t)
            if temp not in combi: 
                combi.append(temp)
            j+=1
        i+=1
    print(combi)
    
number=12345
array=[]
while number!=0:
    array.insert(0, number%10)
    number//=10
combinations(array)
