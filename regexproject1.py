import re

'''
Matching One or More with the Plus  +
Matching Zero or More with the Plus *
Matching One or Zero with the Plus ?

'''
txt = 'The number of My crush is  bebebe'
get_name = re.compile(r'(be){2,4}')
mo = get_name.search(txt)
if mo== None:
    print('Not Found !!')
else:
    print(mo.group())


# findall()

str1 = '''
  my phone 345-356-123
  my boss"s phone number is 567-345-678
  my friend "s Number ohone is 789-456-123
'''

regex_Phone = re.compile(r'\d{3}-\d{3}-\d{3}')
numbers = regex_Phone.findall(str1)

print(numbers)

"""
\d ===> 0 to 9
\D ====> any thing except 0 to 9

\w ===> any letter, digit and underscore Chars
\W ===> contre \w

\s ====> space, tab newline 
\S ====>  contre \S

"""

t = "Java is most popular progamming language in the world "
RegexT = re.compile(r'Java')
new_txt = RegexT.sub('Python',t)
print(new_txt)


