'''
my_list = ['Anas','Sheikh',18,'Chris','Hemsworth',35]
print(my_list)

l=[1,4,4,5,4,45,2,3,32,45,4,6,6,3,23,5,67,3,]
#print(my_list[:4])
l.sort()
print(l)

c = l.count(4)
print(c)

l.sort(reverse=True)
print(l)

#indexing
print(l[1])

for item in my_list:
    if item == 'Chris':
        continue
    print(item)
    '''

new_l =[1,2,3,4,5,6,7,8,9,"a","b","c","d",10,11,12,13,14,15,16,17,18,19,20]
b= [item for item in new_l if isinstance(item,str)]
print(b)
print('\n\n')
matrix =[
    [1,2],[2,3],
    [4,5],[3,6]
]

for row in matrix:
    print(row)

t_sum = 0
for row in matrix:
    t_sum+=sum(row)

print(t_sum)

#flattern

print('\n')

k = [item for n in matrix for item in n]
print(k)
r=k[::-1]
print(r)
print('\n')

f1 = input("1")
f2 = input("1")
f3 = input("1")
f4 = input("1")

l1 = [f1,f2,f3,f4]
l1.sort()
print(l1)
