friends_list=["Rolf", "Jay", "Jonah", "Ayden", "Eric"]

friends_list = sorted(friends_list)
print(friends_list)
print(friends_list[-1])
print(friends_list[2:4])
friends_list.remove("Eric")
friends_list.remove("Jonah")
friends_list.append("David")
friends_list.insert(0, "Marry")
print(friends_list)

for friend in friends_list:
    print("Hi, ",friend)

nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[-1])
print(nums[-3:])
sum=0
for num in nums:
    sum=sum+num
print("sum is: ", sum)

s = "Python is fun"
print(s.split(" "))
s_list = s.split(" ")
for word in s_list:
    print(word.upper())
