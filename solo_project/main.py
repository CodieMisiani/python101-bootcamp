# personal details
user_name = "Nimrod"
monthly_budget = 50000  # in KES
is_tracking_enabled = True
currency = "KES"

#16/07/25

this_month_expenses = 488000

#if this_month_expenses > monthly_budget:
   # print("⚠️ Budget exceeded!")
#elif this_month_expenses == monthly_budget:
   # print("✅ You used exactly your budget.")
#else:
    #print("🎉 You're within budget. Great job!")

#Functions lesson
def check_budget(expense,budget):
    if this_month_expenses > monthly_budget:
        return"⚠️ Budget exceeded!"
    elif this_month_expenses == monthly_budget:
        return"✅ You used exactly your budget."
    else:
        return"🎉 You're within budget. Great job!"

message = check_budget(this_month_expenses, monthly_budget)
print(message)

#LOOPS
expenses = [1200, 3000, 450, 800, 2000]
total = 0

for item in expenses:
    total += item

print("Your total expenses are:", total)

#Optional with While loop
#We’re starting with the first index of the list.
i = 0
#This is where we'll store the sum as we add the expenses.
total = 0

while i < len(expenses):
    total += expenses[i]
    i += 1

print("Total using while loop:", total)
# total += expenses[i]
# This means:

# python
# Copy
# Edit
# total = total + expenses[i]
# We’re adding the value at position i in the list to our running total.

# If the list is:

# python
# Copy
# Edit
# expenses = [100, 200, 300]
# Then:

# i = 0 → expenses[0] = 100

# total = 0 + 100 = 100

# Next loop:

# i = 1 → expenses[1] = 200

# total = 100 + 200 = 300

# And so on...
# print intro message
# print("Welcome,", user_name)
# print("Your budget this month is:", monthly_budget)
# print("Your budget this month is:", monthly_budget,f"You're using {currency} as your currency.")
# print("Your budget this month is:", monthly_budget,f" {currency}.")
# print("Tracking expenses:", is_tracking_enabled)
# print(f"You're using {currency} as your currency.")

