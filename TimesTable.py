import time
x = int(input("Type in number representing which times table you want: "))
time.sleep(1)
print ("Below is the " + str(x) + " times table")
for i in range(1,13):
    product = x * i
    print(f"{x} x {i} = {product}")