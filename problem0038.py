largest = 918273645

for i in range(9000, 10000):
    num2 = i * 2

    pan_set = set(str(i)) | set(str(num2))

    if not "0" in pan_set and len(pan_set) == 9:
        if int(str(i) + str(num2)) > i:
            largest = int(str(i) + str(num2))

print(largest)