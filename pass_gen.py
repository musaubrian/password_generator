import time
import random

# password generator
print("""
    |--------------------|
    |    y = yes         |
    |    n = no          |
    |--------------------|
""")

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "1234567890"
symbols = " *&%$#@!+~:-<|?/ >"

sym = input("Would you like to use symbols? ")
print()
lower = input("Would you like to use lowercase letters? ")
print()
nums = input("Would you like to use numbers? ")
print()

# use of symbols
if sym == "y":
    syms = True
else:
    syms = False

# use of lowercase letters
if lower == "y":
    lower = True
else:
    lower = False

# use of numbers
if nums == "y":
    nums = True
else:
    nums = False

# uses uppercase letters no matter what
upper = True

# empty string where the random values are joined to
empty_pass = ""

if upper:
    empty_pass += uppercase

if lower:
    empty_pass += lowercase

if nums:
    empty_pass += digits

if syms:
    empty_pass += symbols

length = 15
amount = 7

print("%"*50)
print()
time.sleep(0.9)

print(">>>", "Generating password")
time.sleep(0.5)
for p in range(amount):
    final_pass = "".join(random.sample(empty_pass, length))
    print("[~]", final_pass)
    time.sleep(0.5)

leave = input("Leave terminal? ")
if (leave == "y"):
    print("~"*50)
    time.sleep(1)
    SystemExit()
else:
    time.sleep(1)
    SystemExit()
