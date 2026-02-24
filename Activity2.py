a = ["121", "cbc", "abc", "123", "242"]
b = []
count = 0

for i in a:
    if i[0] == i[-1]:
        count = count + 1
        b.append(i)
print("The list where the first and last things are the same are", b)
print("The number of words which has the same last and first are", count)

    
