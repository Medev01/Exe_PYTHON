import re 

PhoneRegex = re.compile(r'''(
         (\d{3} |\(\d{3}\))?    #area code
         (\s|-|\.)   # separator
         (\d{3})      # first Three digits
         (\s|-|\.)  
         (\d{4})     # LAST FOUR DIGITS  ''',re.VERBOSE)

mailRegex =  re.compile(r'''(   
        [a-zA-Z0-9._%+-]+ # username
        @ # @ symbol
        [a-zA-Z0-9.-]+   # domain name
        (\.[a-zA-Z]{2,4})   # dot-something
 )''', re.VERBOSE)
