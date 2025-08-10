# 📌 Checkpoint Exercise (in basics/functions.py):
# Create a function called greet_user(name)
def greet_user(name):
    print(f"Hello, {name}!")

# Create a function called is_even(number) that returns True if the number is even
def is_even(number):
    return number % 2 == 0

# Create a function convert_kes_to_usd(kes_amount) assuming $1 = 140 KES
def convert_kes_to_usd(kes_amount):
    return kes_amount / 140

# 👇 Let's break down Exercise 2 (Check if a number is even)
# ❓ What do we want?
# A function that takes a number and tells us if it’s even.

# ✅ Step 1: Write the function
# python
# Copy
# Edit
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# % means "modulus" — it gives the remainder when dividing.
# If number % 2 == 0, it means the number is divisible by 2 (i.e., even).

# ✅ Step 2: Use (call) the function
# python
# Copy
# Edit
# print(is_even(4))  # Output: True
# print(is_even(7))  # Output: False
# 💡 Remember: return gives a result back to wherever you called it.
# You can save that result, print it, or use it in another calculation.

# 🔁 Now Exercise 3: Convert KES to USD
# Assume 1 USD = 140 KES

# ✅ Step 1: Write the function
# python
# Copy
# Edit
# def convert_kes_to_usd(kes_amount):
#     rate = 140  # 1 USD = 140 KES
#     usd = kes_amount / rate
#     return usd
# ✅ Step 2: Call and print result
# python
# Copy
# Edit
# amount = 7000
# usd_equivalent = convert_kes_to_usd(amount)
# print(f"{amount} KES is approximately ${usd_equivalent:.2f}")
# :.2f limits it to 2 decimal places.

# 🧠 Mini Practice (Do this right now in functions.py)
# Try writing your own:

# A function called greet_user(name) that says hello.

# A function called square(number) that returns the square.

# A function sum_three(a, b, c) that returns the total.

# 🧩 And here's how to think about return:
# Situation	Use print()	Use return
# You just want to display something	print("Hi")	❌ No result for reuse
# You want to get a result back	✅ return something	Then store or reuse it later
# You’ll use the value in another line	✅ Use return	Combine results, compare, etc.

# 🎯 Challenge Reflection Prompt:
# Write this in your reflections.md:

# “I struggled with understanding how return works in functions, but now I realize it helps me get a result back from the function so I can use it later. The difference between printing and returning is...”
# keep streak alive 1
# keep strike alive 2
# keep strike alive 3
# Keep strike alive 4