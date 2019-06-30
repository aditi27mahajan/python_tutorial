#Write a Python program to convert temperatures to and from celsius, fahrenheit

# get user input
temp = input("\nthe temperature you like to convert?:-\t")
degree = int(temp[:-1])
convention = temp[-1]

# condision
if convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  convention = "Fahrenheit"
elif convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in",convention, "is", result, "degrees.")



