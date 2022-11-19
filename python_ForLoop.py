#write program from 1 to 10
for num in range(1,11):
    print(num)

#write program from 1 to 10 using 2 step
for num in range(1,11,2):
    print(num)

#write program from 10 to 1 using 2 step
for num in range(10,0,-1):
    print(num)

# Write a program to calculate the sum of given list elements using for loop
# output = 25
int_list = [4,8,-2,10,5]
list_sum = 0
for num in int_list:
    list_sum = list_sum + num
print("Total sum of elements = ",list_sum)
