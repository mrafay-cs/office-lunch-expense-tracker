days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
expenses = {}

print("office lunch expense tracker")
print("----------------------------")

for day in days:
    while True:
        try:
            cost = float(input(f"Enter lunch cost for {day}: $"))
            if cost < 0:
                print("Please enter a cost of 0 or more.")
            else:
                expenses[day] = cost
                break
        except ValueError:
            print("Please enter a valid number.")

while True:
    try:
        weekly_budget = float(input("Enter your weekly lunch budget: $"))
        if weekly_budget < 0:
            print("Please enter a budget of 0 or more.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

total_spent = sum(expenses.values())

paid_days = {day: cost for day, cost in expenses.items() if cost > 0}

if paid_days:
    average_spend = total_spent / len(paid_days)
    most_expensive_day = max(paid_days, key=paid_days.get)
    cheapest_paid_day = min(paid_days, key=paid_days.get)
else:
    average_spend = 0
    most_expensive_day = "None"
    cheapest_paid_day = "None"

monthly_estimate = total_spent * 4
yearly_estimate = total_spent * 48

print()
print("weekly lunch summary")
print("--------------------")
print(f"Total spent: ${total_spent:.2f}")
print(f"Average per paid office day: ${average_spend:.2f}")

if paid_days:
    print(f"Most expensive day: {most_expensive_day} (${expenses[most_expensive_day]:.2f})")
    print(f"Cheapest paid day: {cheapest_paid_day} (${expenses[cheapest_paid_day]:.2f})")
else:
    print("Most expensive day: None")
    print("Cheapest paid day: None")

print(f"Monthly estimate: ${monthly_estimate:.2f}")
print(f"Yearly estimate: ${yearly_estimate:.2f}")

print()
if total_spent > weekly_budget:
    difference = total_spent - weekly_budget
    print(f"Budget status: Over budget by ${difference:.2f}")
elif total_spent < weekly_budget:
    difference = weekly_budget - total_spent
    print(f"Budget status: Under budget by ${difference:.2f}")
else:
    print("Budget status: Exactly on budget")