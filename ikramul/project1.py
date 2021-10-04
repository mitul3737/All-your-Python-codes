import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

user_lst = []
dealer_lst = []
user_sum = 0
dealer_sum = 0
flag = True
super_flag = True
while super_flag:
    print(logo)
    user_lst = []
    dealer_lst = []
    user_sum = 0
    dealer_sum = 0
    flag = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(2):
        user_lst.append(random.choice(cards))
        dealer_lst.append(random.choice(cards))
    print("Dealer got",dealer_lst[0])
    print("Your deck is:",user_lst)
    
    if sum(dealer_lst) ==21:
        print("Dealers deck",dealer_lst)
        print("You lose")
        super_flag = False
        flag = False
        
        
    elif sum(user_lst) == 21:
        print("Dealers deck",dealer_lst)
        print("You won")
        flag = False
        super_flag = False
        
    choice = "n"
    if flag:
        choice = input("Input y to hit or press n to stand: ")
    while sum(dealer_lst) < 17:
        dealer_lst.append(random.choice(cards))
    while choice == "y":
        user_lst.append(random.choice(cards))
        #while sum(dealer_lst) < 17:
            #dealer_lst.append(random.choice(cards))
        if sum(user_lst) > 21:
            if 11 in user_lst:
                k = user_lst.index(11)
                user_lst[k] = 1
            else:
                #print("step1")
                print("Dealers deck",dealer_lst)
                print("Your deck is:",user_lst)
                print("You lose!")
                super_flag = False
                flag = False
                break
        if sum(user_lst) == 21:
            print("Dealers deck",dealer_lst)
            print("Your deck is:",user_lst)
            print("You won!")
            super_flag = False
            flag = False
            break
        else:
            print("Dealers deck",dealer_lst[:-1])
            print("Your deck is:",user_lst)
        #while sum(dealer_lst) < 16:
            #dealer_lst.append(random.choice(cards))
        choice = input("Input y to hit or press n to stand: ")
    if flag:
        if sum(dealer_lst)> 21:
            if 11 in dealer_lst:
                k = dealer_lst.index(11)
                dealer_lst[k] = 1
                while sum(dealer_lst) < 17:
                    dealer_lst.append(random.choice(cards))
            else:
                #print("step2")
                print("Dealers deck",dealer_lst)
                print("Your deck is:",user_lst)
                print("You won!")
                super_flag = False
                flag = False
                
        if sum(dealer_lst)> 21 and flag:
            #print("step7")
            print("Dealers deck",dealer_lst)
            print("Your deck is:",user_lst)
            print("You won!")
            super_flag = False
            flag = False
            break
        if sum(user_lst) > sum(dealer_lst) and flag:
            #print("step3")
            print("Dealers deck",dealer_lst)
            print("Your deck is:",user_lst)
            print("You won!")
            super_flag = False
            flag = False
            
            
        elif sum(user_lst) == sum(dealer_lst) and flag:
            #print("step4")
            print("Dealers deck",dealer_lst)
            print("Your deck is:",user_lst)
            print("Draw!")
            flag = False
            super_flag = False
            
        elif sum(user_lst) < sum(dealer_lst) and flag:
            #print("step5")
            print("Dealers deck",dealer_lst)
            print("Your deck is:",user_lst)
            print("You lost!")
            flag = False
            super_flag = False
            
    again = input("Do you wanna play again? press y to play or press n to stop playing: ")   
    if again =="n":
        print("Thanks for playing!")
        break
    else:
        super_flag = True    
