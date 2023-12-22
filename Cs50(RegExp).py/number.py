import re
no_of_inputs = int(input())
for _ in range(no_of_inputs):
    number = input()
    match = re.search(r'^[789]\d{9}$', number)
    if match:
        print("YES")
    else:
        print('NO')
    