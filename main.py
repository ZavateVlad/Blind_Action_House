from replit import clear
#HINT: You can call clear() to clear the output in the console.

action_list = []
new_bidder = True
highest_bid = 0
entry = {}
winner = ''

def action(person_name, person_bid):
  entry["Person"] = str(person_name)
  entry["Bid"] = int(person_bid)
  action_list.append(entry)

while new_bidder:
  print("Welcome to the secret action program. ")
  name = input("What is your name? ")
  bid = input("What's your bid?: $")
  action(name, bid)
  for person in action_list:
    if person['Bid'] > highest_bid:
      highest_bid = person['Bid']
  winner = person['Person']  
 # print(person['Person'])
  new = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if new == 'no':
    new_bidder = False
    print(f'The person who wins is {winner} with a bid of: ${highest_bid}')
  else:
    clear()
    


  
  
  
  