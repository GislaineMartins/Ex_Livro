import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)'),
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Esse código aparesenta erro quando roda. Porém, se rodar no shell interativo ele funciona')



