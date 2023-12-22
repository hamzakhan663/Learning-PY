#Extract users username from url

import re
url = input('URL: ').strip()
# regex pattern - Substitute the beginning of the string containing https or http followed by '://' (optional) then followed by www. (optional)and lastly followed by 'instagram.com' WITH an empty string. If pattern is not matched, it returns a copy of the original string.
username=re.sub(r'^(https?://)?(www\.)?instagram\.com/', '', url)
print (f"Username: {username}.")


url = input('URL: ').strip()
# regex pattern - search for the beginning of the string containing https or http followed by '://'  (optional and non capturing) . Followed by www. (optional and non capturing). Followed by 'instagram.com'. Followed by '/' then followed by one or more alphanumeric characters (no input after the pattern). Walrus operator in if statement used to initialize the variable and set a condition to it.
if match := re.search(r'^(?:https?://)?(?:www\.)?instagram\.com/(\w+)$', url, re.IGNORECASE):
    #print the first group in match - users username
    print (f"Username: {match.group(1)}")