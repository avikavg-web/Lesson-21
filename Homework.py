import math
start = int(input("Enter begininng of range: "))
end = int(input("Enter end of range: "))

evenroot = []
oddroots = []

for num in range (start, end + 1):
    root = math.sqrt(num)
    
    if root.is_integer():
        root_int = int(root)
        if root_int % 2 == 0:
            evenroot.append(root_int)
        else:
            oddroots.append(root_int)



print("Even:", evenroot)
print("Odd:", oddroots)