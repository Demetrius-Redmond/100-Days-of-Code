import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over = False
hand = []
computer_hand = []
blackjack = False

first_card  = random.choice(cards)
hand.append(first_card)
second_card = random.choice(cards)
hand.append(second_card)
your_score = first_card + second_card
computer_first_card = random.choice(cards)
computer_hand.append(computer_first_card)
computer_second_card = random.choice(cards)
computer_hand.append(computer_second_card)
computer_score = computer_first_card + computer_second_card
if your_score == 21:
    blackjack = True
    print("Blackjack! You win!!!")
    
if computer_score == 21: 
    print("Blackjack! House wins!!!")
    blackjack = True   
print(f"    Your cards: {hand}, current score: {your_score}")
print(f"    Computer's first card: {computer_hand}, final score: {computer_score}")
y_or_n = input("Type 'y' to get another card, type 'n' to pass: ")
if y_or_n == "y":
    another_card = random.choice(cards)
    your_score += another_card
    hand.append(another_card)
    if your_score == 21:
        print("Blackjack! You win!!!")
        blackjack = True
    print(f"    Your final hand: {hand}, final score: {your_score}")
    if your_score > 21:
        print("You went over. You lose.")
    computer_third_card = random.choice(cards)    
    computer_hand.append(computer_third_card)
    computer_score += computer_third_card
    if computer_score == 21: 
        print("Blackjack! House wins!!!")
        blackjack = True 
    print(f"    Computer's final hand: {computer_hand}, final score: {computer_score}")
    if your_score > computer_score and your_score < 21:
        print("You win!")
    elif your_score < 21 and computer_score > 21:
        print("You win!")
    elif computer_score > your_score and computer_score < 21:
        print("You lose.")   
else:
    computer_second_card = random.choice(cards)
    computer_hand.append(computer_second_card)
    computer_score += computer_second_card
    if computer_score == 21: 
        print("Blackjack! House wins!!!")
        blackjack = True 
    print(f"    Your final hand: {hand}, final score: {your_score}")
    print(f"    Computer's final hand: {computer_hand}, final score: {computer_score}")
    if your_score > computer_score and your_score < 21:
        print("You win!")
    elif your_score < 21 and computer_score > 21:
        print("You win!")
    elif computer_score > your_score and computer_score < 21:
        print("You lose.")
    
