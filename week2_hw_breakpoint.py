myNumbers =  [
[66, 28, 97, 28, 6, 16, 45, 7, 71, 47], 
[43, 13, 9, 43, 18, 5, 80, 32, 100, 86],
[73, 20, 19, 72, 95, 70, 70, 61, 98, 96],
[11, 45, 4, 45, 25, 45, 9, 99, 98, 90],
[28, 48, 85, 26, 59, 46, 12, 66, 78, 47],
[62, 47, 16, 77, 68, 31, 37, 96, 11, 59],
[12, 53, 6, 61, 87, 80, 8, 48, 38, 15],
[68, 82, 29, 95, 64, 76, 82, 88, 37, 90],
[57, 18, 27, 15, 69, 79, 46, 83, 29, 80], 
[10, 79, 75, 58, 26, 29, 88, 30, 91, 78]
]

max = myNumbers[0][0]
min = myNumbers[0][0]
total = 0
length = 0

for i in myNumbers:
    for j in i:
        if j > max:
            max = j
        if j < min:
             min = j
        total += j
        length += 1

print(f"The highest number is {max}")
print(f"The lowest number is {min}")
print(f"The range is {max-min}")
print(f"The sum is {total}")
print(f"The average is {total/length}")
