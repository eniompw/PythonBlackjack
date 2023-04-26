import random

def blackjack():
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    
    def hand_total(hand):
        total = 0
        aces = 0
        for card in hand:
            if card == 'J' or card == 'Q' or card == 'K':
                total += 10
            elif card == 'A':
                aces += 1
            else:
                total += card
        total += aces
        while total + 10 <= 21 and aces > 0:
            total += 10
            aces -= 1
        return total
    
    while True:
        print(f"Player hand: {player_hand} Total: {hand_total(player_hand)}")
        print(f"Dealer hand: [{dealer_hand[0]}, X]")
        if hand_total(player_hand) > 21:
            print("Player busts! Dealer wins!")
            break
        elif hand_total(player_hand) == 21:
            print("Blackjack! Player wins!")
            break
        choice = input("Hit or Stand? (h/s): ")
        if choice.lower() == 'h':
            player_hand.append(deck.pop())
        else:
            while hand_total(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            print(f"Dealer hand: {dealer_hand} Total: {hand_total(dealer_hand)}")
            if hand_total(dealer_hand) > 21:
                print("Dealer busts! Player wins!")
            elif hand_total(player_hand) > hand_total(dealer_hand):
                print("Player wins!")
            elif hand_total(player_hand) < hand_total(dealer_hand):
                print("Dealer wins!")
            else:
                print("It's a tie!")
            break

blackjack()
