l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = []

carry = 0

for i in range(len(l1)):
    total = l1[i] + l2[i] + carry
    digit = total % 10
    carry = total // 10
    l3.append(digit)

if carry:
    l3.append(carry)

print(l3)













