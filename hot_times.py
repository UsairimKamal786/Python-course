# Ask the user to enter the temperature
temperature = int(input("Enter the temperature in degrees Celsius: "))

# Use conditional statements to decide what to wear
if temperature >= 25:
    print("It's warm! You can wear light clothes.")
elif temperature >= 15:
    print("It's a bit cool. Maybe wear a light jacket.")
elif temperature >= 5:
    print("It's cold! Better wear warm clothes like a jacket or pullover.")
else:
    print("It's really cold! Wear a heavy jacket, sweater, gloves, and a cap.")
