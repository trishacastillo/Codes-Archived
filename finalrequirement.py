import random

def ChooseMode():
    print('[S]Solo Play\n[P]Player Vs AI')
    ans = input('Enter Game Mode:')
    if ans=="S":
        SoloMode();
    elif ans=="P":
        PVSAIMode();
    else:
        print('INVALID INPUT!')
    return

def SoloMode():
    target_num = random.randint(1, 20)
    tries=0
    guess_num = 0
    while target_num != guess_num and tries<3:
        tries=tries+1
        guess_num = int(input('Guess a number from 1 and 20: '))
        if guess_num>21:
            print('INVALID INPUT!')
        elif guess_num>target_num:
            print('Opps! Your Guess was too HIGH ...')
        elif guess_num<target_num:
            print('Opps! Your Guess was too LOW ...')
        elif guess_num==target_num:
            print('Congrats, You get it right ...')
    print('======================')
    if guess_num==target_num:
        print('YOU WIN !!!')
    if guess_num!=target_num:
        print('Sorry, YOU LOSE!!! \nThe number was ',target_num,'\nYou can TRY AGAIN next time :)')
    print('======================')
    return
def PVSAIMode():
    print('Tossing a Coin...\nHead[H] | Tail[T]')
    ans = input('Pick your BET:')
    coin = random.randint(1, 2)
    if coin==1:
        coin_result="H"
    else:
        coin_result="T"
    if ans==coin_result:
        print(ans," AI will guess first!")
        Playing();
    else:
        print(coin_result,"You guess first!")
        Playing();
    return
def Playing():
    print('Instruction: First who guess right number WINS!')
    target_num = random.randint(1, 20)
    guess_num = int(input('Guess a number from 1 and 20: '))
    while target_num != guess_num:
        guess_num = int(input('Guess a number from 1 and 20: '))
        ai_guess= random.randint(1, 20);
        print("AI guess is ", ai_guess)
        if ai_guess==target_num:
            guess_num=ai_guess
            print('AI get it!')
        if guess_num>21:
            print('INVALID INPUT!')
        elif guess_num>target_num:
            print('Opps! Your Guess was too HIGH ...')
        elif guess_num<target_num:
            print('Opps! Your Guess was too LOW ...')
        elif guess_num==target_num:
            print('Congrats, You get it right ...')
    return
#Main
print('HI or LOW GAME')
Playing();
