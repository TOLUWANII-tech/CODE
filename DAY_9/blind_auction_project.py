
auction_continues = True

bidders_profile = {
    'names': [],
    'prices': [],
}

while auction_continues:
    bidder_name = input("What is your name?  \n")
    bidder_price = int(input('How much do you want to bid? \n'))
    bidders_profile['names'].append(bidder_name)
    bidders_profile['prices'].append(bidder_price)


    more_bidders = input("Is there anyone else bidding? \nType 'y' for yes and 'n' for no.\n")
    if more_bidders == 'n':
        auction_continues=False



max_bid = max(bidders_profile['prices'])
position_for_max_bid = bidders_profile['prices'].index(max_bid)
max_bidder = bidders_profile['names'][position_for_max_bid]
print(f'The winner is {max_bidder} with a bid of #{max_bid}')


