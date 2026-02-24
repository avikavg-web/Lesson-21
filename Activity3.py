a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 90]
sum = 0
for i in a:
    sum = sum + i

avg = sum/len(a)
print("The sum is", sum)
print("The average is", avg)

print(a.sort())
print(max(a))
print(min(a))