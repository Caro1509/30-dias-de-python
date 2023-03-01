space = ""
print(space)
print(len(space))
word1 = "Thirty"
print(word1)
print(len(word1))
word2 = "Days"
print(word2)
print(len(word2))
word3 = "of"
print(word3)
print(len(word3))
word4 = "Phyton"
print(word4)
print(len(word4))
multiline_string1 = """thirty days of python"""
print(multiline_string1)

space = " "
print(space)
print(len(space))
word5 = "Coding" 
print(word5)
print(len(word5))
word6 =  "For"
print(word6)
print(len(word6))
word7 = "All"
multiline_string2 = """Coding For All"""

company = multiline_string2
print(company)
print(len(company))

company.upper()
company.lower()

company = "coding for all"
print(company.capitalize()) # "Coding for all"
company = "Coding for all"
print(company.tittle()) # "Coding For All"
company = "Coding For All"
print(company.swapcase()) # "CODING FOR ALL"
company = "Coding For All"
print(company.swapcase()) # "cODING fOR aLL"

company = "Coding For All"
print(company.slice(word1)) # "For All"


print(multiline_string2.count('coding'))
print(multiline_string2.replace('coding' , 'python'))
print(multiline_string2.replace('all' , 'everyone'))
print(multiline_string2.split())

multiline_string3 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(multiline_string3.split(', '))

print(multiline_string2.index)
print(multiline_string2.rindex)
print(multiline_string2.index(10))

multiline_string4 = """Python For Everyone"""
print(multiline_string4)

palabra1 = 'Phyton'
print(len(palabra1))
palabra2 = 'For'
print(len(palabra2))
palabra3 = 'Everyone'
print(len(palabra3))

primera_letra = palabra1[0]
print(primera_letra) #P
segunda_letra = palabra2[0]
print(segunda_letra) #F
tercera_letra = palabra3[0]
print(tercera_letra) #E

print(f"{primera_letra}{segunda_letra}{tercera_letra}")

palabra4 = 'Coding'
print(len(palabra4))
palabra5 = 'For'
print(len(palabra5))
palabra6 = 'All'
print(len(palabra5))

primera_letra2 = palabra4[0]
print(len(primera_letra2)) #C
segunda_letra2 = palabra5[0]
print(len(segunda_letra2)) #F
tercera_letra2 = palabra6[0]
print(len(tercera_letra2)) #A

print(multiline_string2.index) #0

print(multiline_string2.index) #8

print(multiline_string2.rfind('i'))
print(multiline_string2.rfind('a'))

multiline_string5 = 'Coding For All People'
print(multiline_string5.rfind('l'))

multiline_string6 = 'You cannot end a sentence with because because because is a conjunction'
print(multiline_string6.index('because'))
print(multiline_string6.rindex('because'))







