def due_amount(total_amount,amount_paid):
    print(amount_paid-total_amount)

total_amount=int(input("Please enter the total amount"))
amount_paid=int(input("Please enter the total amount"))

print(due_amount(total_amount,amount_paid))
    