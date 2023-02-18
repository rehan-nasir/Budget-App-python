# A brief example showing how the category class works. 
import Budget
from Budget import create_spend_chart
food = Budget.Category("Food")
clothing = Budget.Category("Clothing")
auto = Budget.Category("Auto")
clothing.deposit(3000, "initial")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
clothing.transfer(50, food)
print(food)
print(clothing)
print()
print(create_spend_chart([food, clothing, auto]))
