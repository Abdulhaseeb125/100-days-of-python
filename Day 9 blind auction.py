def Max_bid(n_dict):
    highest_bid = 0
    bidder_name = ""
    for key in n_dict:
        bid = n_dict[key]
        if bid > highest_bid:
            highest_bid = bid
            bidder_name = key
    print(f"The winner is {bidder_name} and bid amount is ${highest_bid}")


name_dict = {}
Again = True
while Again:
   Name = input("Enter Name:")
   Bid = int(input("Enter Amount: $"))
   name_dict[Name] = Bid

   again = input("Is there anyone else:y/n")
   if again == 'n':
       break
   elif again == 'y':
       continue
   else:
       print("Invalid Command.")
       exit()

Max_bid(name_dict)
