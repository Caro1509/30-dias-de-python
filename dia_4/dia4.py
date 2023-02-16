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
