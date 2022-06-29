from copy import deepcopy
T = int(input())

for _ in range(T):
    n = int(input())
    inputs = input()
    if len(inputs) == 1:
        print(inputs, inputs)
    else:
        numbers = map(int, inputs.split())
        
        print(min(deepcopy(numbers)), max(numbers))