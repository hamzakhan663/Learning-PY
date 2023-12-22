#Progressive Regex Patterns

import re
# email = input("What's your email address: ").strip()
# if re.search(r".+@.+\.com", email): # regex pattern - finds one or more characters before @ and one or more characters after @ then ends with .com
#     print("Valid.")       
# else:
#     print("Invalid")



# email = input("What's your email address: ").strip()
# if re.search(r"^.+@.+\.com$", email): # regex pattern - finds the start of one or more characters before @ and one or more characters after @ then ends with .com (nothing else after)
#     print("Valid.")       
# else:
#     print("Invalid")



# email = input("What's your email address: ").strip()
# if re.search(r"^[^@]+@[^@]+\.com$", email): # regex pattern - finds the start of one or more characters (except '@') before @ and one or more characters (except @) after @ then ends with .com (nothing else after)
#     print("Valid.")       
# else:
#     print("Invalid")
    
# email = input("What's your email address: ").strip()
# if re.search(r"^[a-zA-Z0-9_]+@[a-z]+\.com$", email): # regex pattern - finds the start of one or more characters (ranging from all alphabets in lower and uppercase, numbers and underscore) before @ and one or more characters (ranging from all alphabets in lowercase) after @ then ends with .com (nothing else after)
#     print("Valid.")       
# else:
#     print("Invalid")
    
# email = input("What's your email address: ").strip()
# if re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE): # regex pattern - finds the start of one or more alphanumeric character before @ and one or more alphanumeric character after @ then ends with .com (nothing else after)
#     print("Valid.")       
# else:
#     print("Invalid")
    
email = input("What's your email address: ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE): # regex pattern - finds the start of one or more alphanumeric characters before @ then zero or more repetitions of a sub domain name after @ then one or more alphanumeric character then ends with .com (nothing else after)
    print("Valid.")       
else:
    print("Invalid")