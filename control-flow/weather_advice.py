# weather_advice.py

# Prompt the user for weather input and convert to lowercase for easy comparison
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Use conditional statements (if, elif, else) to provide clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Default case for any input that doesn't match the predefined options
    print("Sorry, I don't have recommendations for this weather.")