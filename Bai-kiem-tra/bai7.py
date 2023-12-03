numbers = [5, 1, 8, 92, -1, 30]
length = len(numbers)

def sap_xep_lon_den_be(numbers):
    for i in range(0, length - 1):
        for j in range(i + 1, length - 1):
            if numbers[i] > numbers[j]:
                num = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = num
    return numbers
print(sap_xep_lon_den_be(numbers))

