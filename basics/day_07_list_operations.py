# Day 07: List operations and slicing

numbers = [10, 20, 30, 40, 50, 60]

print("Original list:", numbers)

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Middle section:", numbers[2:5])

numbers.append(70)
numbers.remove(30)

print("After append and remove:", numbers)

numbers[0] = 99
print("After update:", numbers)
