num = int(input(""))

if num > 100 or num < 1:
    quit()

winner_amount = 0
winner = ""

for _ in range(num):
    name = input("")
    bidder = int(input())

    if bidder >= 2000:
        quit()

    if bidder > winner_amount:
        winner_amount = bidder
        winner = name

print("winner:2")
print(winner)
print("with:")
print(winner_amount)
