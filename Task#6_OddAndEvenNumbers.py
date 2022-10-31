# Achievement Task #6 - Odd and Even Numbers
# Shelemiah Sotelo - 8823190
# This is to determine and separate prime and non-prime numbers.


# Function for determining prime numbers.
def isPrime(number):
   count = 0

   for i in range(2, (number//2 + 1)):
      if(number % i == 0):
         count = count + 1
         break
   
   if (count == 0 and number != 1):
      return True                   # Return True if the number is prime.
   else:
      return False                  # Return False if the number in non-prime.


print("Please enter any numbers. This program will distinguish what numbers are prime and non-prime. ") # explanation for the program
numbers = input()
numList = numbers.split(",")       # Numbers are separated by comma. 

prime = []                         # Empty list for prime numbers.

nonPrime = []                      # Empty list for non-prime numbers.

for x in numList:
   num = int(x)                    # Convert into integer
   if isPrime(num):
      prime.append(x)              # Add number to the prime list.

   else:
      nonPrime.append(x)           # Add number to the non-prime list.


print("Prime numbers are", ",".join(prime))
print("Non-prime numbers are", ",".join(nonPrime))
