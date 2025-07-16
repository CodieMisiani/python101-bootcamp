# 📌 Practice Exercises (Add to basics/loops.py):
# Print numbers from 1 to 10 using a for loop
numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0

for number in numbers:
    total += number

print("Total", total)

#Option 2 
for number in range (1,11):
    print(number)
# Print even numbers between 1 and 20
def is_even(n):
    return n % 2 == 0

for number in range(1, 21):
    if is_even(number):
        print(number)
#Option 2 with for loop
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# Use a while loop to count down from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1  # decrease i by 1 each time
    
# Loop through a list of prices [300, 500, 150, 1200] and print only the prices above 500
prices = [300, 500, 150, 1200]


for price in prices:
    if price > 500:
        print(price)
