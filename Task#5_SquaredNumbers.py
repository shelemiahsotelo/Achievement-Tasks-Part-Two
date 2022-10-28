# Task #5 - Squared Numbers
# Shelemiah Sotelo 8823190

# Instructed to get the cubed result of numbers 1-10 using dictionary.

numBase = {}                # Empty dictionary.
for key in range(1,11):     # Range is set to 1-11 
  value = key ** 3          # Formula for getting ^cube
  numBase[key] = value
print(numBase)
