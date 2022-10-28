# Task #4 - Unit Converter
# Shelemiah Sotelo - 8823190




def tempConversion(tempVal, tempCF):               # Function for temparature conversion.
   if tempCF.upper() == 'C':
      fahr = (tempVal * 1.8) + 32                  # Formula for Celsius to Fahrenheit conversion
      result = '%.2f degree Celsius is equal to: %.2f Fahrenheit' %(tempVal, fahr)
      return result
   
   elif tempCF.upper() == 'F':
      cels = (tempVal - 32) * 5/9                  # Formula for Fahrenheit to Celsius conversion
      result = '%.2f degree Fahrenheit is equal to: %.2f Celsius' %(tempVal, cels)
      return result

   else:
      return "Invalid! C/F only."
 
def speedConversion(speedVal, speedUnit):          # Function for speed conversion.
   if speedUnit.upper() == 'KMH':
      mph = (speedVal * 0.6214)                    # Formula for KMH to MPH conversion
      result = '%.2f KMH is equal to: %.2f MPH' %(speedVal, mph)
      return result
   
   elif speedUnit.upper() == 'MPH':
      kmh = (speedVal * 1.60934)                   # Formula for MPH to KMH conversion
      result = '%.2f MPH is equal to: %.2f KMH' %(speedVal, kmh)
      return result

   else:
      return "Invalid! KMH/MPH only."

print("Unit Converter\nWhat do you want to convert?: \n1. Temparature \n2. Speed" )      # Ask user what they want to convert (temparature/speed).
choice = input().strip()
choice = int(choice)                               # Convert input in to an integer

if choice == 1:
   print("Please enter temperature value:")
   tempNum = input().strip()                 # Remove white spaces from the input
   tempNum = float(tempNum)                  # Convert to the input into float 

   print("Please enter unit: (C/F)")
   tempUnit = input().strip()

   tempResult = tempConversion(tempNum, tempUnit)        # Call the function

   print(tempResult)


elif choice == 2:
   print("Please enter speed value:")
   speedNum = input().strip()                # Remove white spaces from the input
   speedNum = float(speedNum)                # Convert to the input into float 

   print("Please speed unit: (KMH/MPH)")
   speedUnit = input().strip()

   speedResult = speedConversion(speedNum, speedUnit)    # Call the function

   print(speedResult)
