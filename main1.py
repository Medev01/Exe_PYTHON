import re 
description = """
    Hi, I'm Mohamed Ouahlou, I'm 22-year-old a programming 
    and tech wizard with a passion for data and analytics.
    From Morocco, I'm currently studying for my Master in IPS 
    (Intelligence Processing systems ) and developing my skills 
    as a Machine Learning  Developer, Python Developer,
    Web Scraper & Data Analyst. hungering for knowledge, Ready to make an impact!
    eamil medoart949@gamil.com and my number phone is +212 639 618 017 """

namereg = re.compile(r'mohamed ouahlou',re.I)
education = re.compile(r'Master .*',re.I)
age = re.compile(r'(\d{2})')
mail = re.compile(r'''
   [a-zA-Z0-9._%+-]+
   @
   [a-zA-Z0-9.-]+   # domain name
   (\.[a-zA-Z]{2,4})                              
''', re.VERBOSE)
number = re.compile(r'(\+\d{3}) (\d{3}) (\d{3}) (\d{3})')

f = open('infos.txt', 'w')
myregex = [namereg, education,age,mail]
for regex in myregex: 
    var = regex.search(description)
    f.write(f'{var}\n')
f.close()



