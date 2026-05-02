def support(arr: list):

    print("These elements are present in support set:")

    for i in arr:
        if i > 0:
            print(i)


A1: list = []

n: int = int(input("Enter number of elements: "))

for i in range(n):

    value: float = float(input("Enter value: "))
    A1.append(value)


support(A1)