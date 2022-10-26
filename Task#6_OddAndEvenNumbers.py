def isPrime(number):
   count = 0

   for i in range(2, (number//2 + 1)):
      if(number % i == 0):
         count = count +1
         break
   
   if (count == 0 and number != 1):
      return True
   else:
      return False


print("Enter numbers: ") # explanation for the program
numbers = input()
numList = numbers.split(",")

prime = []

nonPrime = []

for x in numList:
   num = int(x)
   if isPrime(num):
      prime.append(x)

   else:
      nonPrime.append(x)


print("Prime numbers are", ",".join(prime))
print("Non-prime numbers are", ",".join(nonPrime))
