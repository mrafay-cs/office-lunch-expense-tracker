Office Lunch Expense Tracker
Had some free time during a train ride and started wondering how much money I spent last week at work just on lunches.

Then I thought about how people who earn more probably end up spending more on food without even realising 😂

Trying to manually calculate the weekly total, average spend, most expensive day, cheapest day, and all that jazz felt a bit tedious, so I decided to make a simple Python script for it.

This little program lets users enter their lunch costs for each workday through the terminal, then it gives them a weekly spending summary.

What It Does
Takes lunch costs from Monday to Friday
Calculates total weekly lunch spending
Calculates average spending per paid office day
Shows the most expensive lunch day
Shows the cheapest paid lunch day
Estimates monthly and yearly lunch spending
Compares the total against a weekly budget
Tech Used
Python
How to Run
Clone the repo or download the files, then run:

python lunch_tracker.py

or:

python3 lunch_tracker.py


Example

office lunch expense tracker
----------------------------
Enter lunch cost for Monday: $14.50
Enter lunch cost for Tuesday: $12
Enter lunch cost for Wednesday: $18.90
Enter lunch cost for Thursday: $0
Enter lunch cost for Friday: $16.20
Enter your weekly lunch budget: $60

weekly lunch summary
--------------------
Total spent: $61.60
Average per paid office day: $15.40
Most expensive day: Wednesday ($18.90)
Cheapest paid day: Tuesday ($12.00)
Monthly estimate: $246.40
Yearly estimate: $2956.80

Budget status: Over budget by $1.60
