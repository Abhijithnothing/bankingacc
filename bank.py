
initial_bal = float(input("Enter the initial balance in your bank account: "))
deposit = float(input("Enter the amount to be deposited: "))
print(f"\nInitial Balance: {initial_bal:.2f}")
new_bal = initial_bal + deposit
print(f"New Balance after deposit of {deposit:.2f}: {new_bal:.2f}")
withdraw = float(input("\nEnter the amount to withdraw: "))
if withdraw > new_bal:
    print("Insufficient balance! Withdrawal not possible.")
else:
    new_bal -= withdraw
    print(f"New Balance after withdrawing {withdraw:.2f}: {new_bal:.2f}")

print("\nFinal Balance:", f"{new_bal:.2f}")
