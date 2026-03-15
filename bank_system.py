accounts = {}

file = open("accounts.txt", "r")

for line in file:
    line = line.strip()
    parts = line.split(":")
    
    account_number = parts[0].strip()
    balance = int(parts[1].strip())
    name = parts[2].strip()

    accounts[account_number] = [name, balance]

file.close()

print("Accounts loaded successfully.\n")

for account in accounts:
    name, balance = accounts[account]
    print(account, name, balance)