class Bidder:
    def __init__(self, num_users:int, num_rounds:int)->None:
       
        '''an initializer with the definition def __init__(self, num_users, num_rounds) , in which
        num_users contains the number of User objects in the game, and num_rounds contains the
        total number of rounds to be played. The Bidder might want to use this info to help plan its
        strategy.'''
        pass
    def bid(self, user_id):
        '''a bid method with the definition def bid(self, user_id) , which returns a non-negative
            amount of money, in dollars round to three (3) decimal places.
            
            10% - Your performance in the competition against all other submissions across the class.
            The highest scoring students will earn a full 10 percentage points, dropping to 0 for the
            bottom scoring students.'''
    
        NotImplementedError()

    def notify(self, auction_winner, price, clicked):

        '''a notify method with the definition def notify(self, auction_winner, price,
    clicked) , which is used to send information about what happened in a round back to the
    Bidder . Here, auction_winner is a boolean to represent whether the given Bidder won
    the auction ( True ) or not ( False ). price is the amount of the second bid, which the winner
    pays. If the given Bidder won the auction, clicked will contain a boolean value to
    represent whether the user clicked on the ad. If the given Bidder did not win the auction,
    clicked will always contain None .'''
        
    pass


    def __repr__(self):
        pass

    def __str__(self):
        pass


