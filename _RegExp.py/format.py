import re

name = input("What is your name?: ").strip()
#walrus operator
if match := re.search(r'^(.+), *(.+)$', name): # matches the beginning of one or more characters followed by a whitespace character or not then one or more characters
# if match:
    last_name = match.group(1)
    first_name = match.group(2)
    name = f"{first_name} {last_name}"
print (f"Welcome, {name}.")