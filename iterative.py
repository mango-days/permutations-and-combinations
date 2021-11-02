def factorial(number):
    if number!=1: return ((number)*(factorial(number-1)))
    else: return number
    
def combinations(number):
    size=len(number)
    solution_count = factorial(size)
    solution_count_copy=solution_count
    combi = []
    combi.append(number)
    solution_count-=1
    index=0
    print(combi)
    while index<size:
        if (index%2==1) and (index!=0):
            temp=number.copy()
            temp[index] = number[index-1]
            temp[index-1] = number[index]
            combi.append(temp)
            solution_count-=1
        index+=1
    index=0
    while index<size:
        if (index%2==0) and (index!=0):
            temp=number.copy()
            temp[index] = number[index-1]
            temp[index-1] = number[index]
            combi.append(temp)
            solution_count-=1
        index+=1
    #reverse collected thus far
    i=0
    stopping_condition=(solution_count_copy-solution_count)
    while i<stopping_condition:
        j=0
        temp = combi[i]
        temp_r =[]
        while j<size:
            temp_r.insert(0, (temp[j]))
            j+=1
        combi.append(temp_r)
        solution_count-=1
        i+=1
        if solution_count==0: break
    print("combinations :")
    print(combi)

    #permutations of combinations
    i=0
    while i<solution_count_copy:
        j=1
        while j<size:
            temp=combi[i].copy()
            t=temp[j]
            temp.pop(j)
            temp.insert(0, t)
            if temp not in combi: 
                combi.append(temp)
                solution_count-=1
            j+=1
        i+=1
    print("permutations :")
    print(len(combi))
    print(combi)
    
number=12345
array=[]
while number!=0:
    array.insert(0, number%10)
    number//=10
combinations(array)