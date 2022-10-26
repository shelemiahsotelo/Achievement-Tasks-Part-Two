def tempConversion(tempVal, tempCF):
   if tempCF.upper() == 'C':
      fahr = (tempVal * 1.8) + 32
      result = '%.2f degree Celsius is equal to: %.2f Fahrenheit' %(tempVal, fahr)
      return result
   
   elif tempCF.upper() == 'F':
      cels = (tempVal - 32) * 5/9
      result = '%.2f degree Fahrenheit is equal to: %.2f Celsius' %(tempVal, cels)
      return result

   else:
      return "Invalid! C/F only."
 
def speedConversion(speedVal, speedUnit):
   if speedUnit.upper() == 'KMH':
      mph = (speedVal * 0.6214)
      result = '%.2f KMH is equal to: %.2f MPH' %(speedVal, mph)
      return result
   
   elif speedUnit.upper() == 'MPH':
      kmh = (speedVal * 1.60934)
      result = '%.2f MPH is equal to: %.2f KMH' %(speedVal, kmh)
      return result

   else:
      return "Invalid! KMH/MPH only."

print("Unit Converter\nWhat do you want to convert?: \n1. Temparature \n2. Speed" )
choice = input().strip()
choice = int(choice)

if choice == 1:
   print("Please enter temperature value:")
   tempNum = input().strip()
   tempNum = float(tempNum)

   print("Please enter unit: (C/F)")
   tempUnit = input().strip()

   tempResult = tempConversion(tempNum, tempUnit)

   print(tempResult)


elif choice == 2:
   print("Please enter speed value:")
   speedNum = input().strip()
   speedNum = float(speedNum)

   print("Please speed unit: (KMH/MPH)")
   speedUnit = input().strip()

   speedResult = speedConversion(speedNum, speedUnit)

   print(speedResult)
