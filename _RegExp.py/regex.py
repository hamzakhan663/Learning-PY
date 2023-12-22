import re
# x = "Get me 2 apples, 5 bananas, 1 watermelon and 15 oranges."
# y = re.findall('[0-9]+',x) # regex pattern - matches one or more digits
# print(y)

# x = "Sulaimon Hamza; Jibril Ahmad; Abdullah Abdulwaahid"
# y = re.findall('^S.+?;', x) # regex pattern - finds a string beginning with S followed by one or more characters ending with non greedily;
# print(y)

# x = "Sulaimon Hamza Omotayo;Jibril Ahmad Nasirudeen"
# y = re.findall('\S+;\S+', x) # regex pattern - finds one or more non space characters before and after ;
# print(y)

# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s) # regex pattern - finds occurrences of one or more non space characters before and after @
# print(lst)

# s = "The book is #4000 Naira in total"
# t = re.findall('\#[0-9]+ \S+', s) # regex pattern - finds an occurrence of # sign followed by one or more digits then a whitespace character followed by one or more non space characters
# print(t)

s = "Hamza,Sulaimon,18"
t = re.findall('S\S+(?=,)', s) # regex pattern - finds S letter followed by one or more non whitespace characters and stops when it sees a comma but does not print it.(lookahead assertion)
print(t)