places = ['Ohio', 'Northern Mariana Islands', 'Maine', 'Florida']
mystery = ['a', 'b']

mystery[0] = places[0][1:3]
mystery[1] = places[1][3:7]
places.pop()
mystery[1] = mystery[1] + places[2][-1]

for x in mystery:
    print(x)

dict = {
    "0": "Blue",
    "1": "Gold",
    "2": "Red"
}

dict_2 = dict.copy()
dict_2.update({"0": "Green"})
dict_2.popitem()
for x in dict_2:
    print(dict_2[x])   

nums = {1, 2, 3, 4, 5}
nums_2 = {10}

nums.clear()
nums.add(20)
nums.add(25)
nums.add(30)
nums.update(nums_2)
nums.remove(25)

for num in nums:
    print(num) 

    s1 = {1, 2, 3, 4}
s2 = {'a', 'b', 'c'}
s3 = {3}
s4 = s1.union(s2)
s5 = s3.intersection(s4)
s6 = s1.difference(s3)
s7 = s3.union(s6)

if s3.issubset(s4):
    print(s7)
else:
    print(s3)

tup = ('Spring', 'Summer', 'Fall', '?')
lis = list(tup)
lis[3] = 'Winter'
tup = tuple(lis)
print('| ', end='')
for item in tup:
    print(item, end=' | ')
print()

nums = (5, 10) + (15, 20)
if 3 in nums:
    print ("Spring")
elif max(nums) > 50:
    print ("Summer")
elif sum(nums) > 100:
    print ("Fall")
elif (min(nums) + 5) > 15:
    print ("Winter")
elif nums.count(5) < 3:
    print ("Spring")