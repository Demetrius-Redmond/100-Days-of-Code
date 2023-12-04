from gavel_art import logo
print(logo)
print("Welcome to the secret auction program.")
bid_list = {} 
winner = {}
yes_no = ""
def find_highest_bidder(bid_list):
    for bidder in bid_list:
     if bid_list[bidder] > bid_list[name]:
          winner[bid_list]=bidder
           
while yes_no == "yes":
     name = input("What is your name? ")
     bid = int(input("What is your bid? $ "))
     bid_list["name"] = bid
     yes_no = input("Are there any other bidders? Type 'yes' or 'no'. ").lower
     if yes_no == "no":
          find_highest_bidder(bid_list)
print(winner)
     

 

 

