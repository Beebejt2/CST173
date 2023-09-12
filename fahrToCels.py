# CST 173 - Delta College
# This program prompts for a temperature in Fahrenheit and
# returns the equivalent in Celsius

# Input
degF = float(input("Enter Fehrenheit temperature: "))

# Processing
degC = (5.0/9.0) * (degF - 32.0)

# Output
print (degC,"degrees C =",degF,"degrees F")
