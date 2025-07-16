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

# print intro message
# print("Welcome,", user_name)
# print("Your budget this month is:", monthly_budget)
# print("Your budget this month is:", monthly_budget,f"You're using {currency} as your currency.")
# print("Your budget this month is:", monthly_budget,f" {currency}.")
# print("Tracking expenses:", is_tracking_enabled)
# print(f"You're using {currency} as your currency.")

