#Number guessing game

from random import randint

real_num = randint(1,100)

tries = 5
attempts = 0
game_state = 'play'
score = 0
victory = False

while True:

    if(game_state == 'end'):
        break

    while game_state == 'play':
        print(real_num)
        while attempts < tries:
            try:
                guess = int(input('Guess the number: '))
            except ValueError:
                print('Guess can only be an integer')
                guess = 0
                if(score > 0):
                    score -= 50
                    print('You lost 50 points')

            if(guess == real_num):
                print(f'Congrats you have won the number was {real_num}.')
                score += 100
                print(f'score: {score}')
                game_state = 'end'
                victory = True
                break
            
            elif(real_num - real_num*0.1 <= guess <= real_num+0.1*real_num):
                print(f'The guess is within 10% of the number, +50 points.')
                score +=50
                

            elif(guess > real_num):
                print('Guess is more than the number.')
                if(score > 0):
                    score -= 25
                    print(f'You lost 25 points')
                    

            elif(guess < real_num):
                print('Guess is less than the number.')
                if(score > 0):
                    score -= 25
                    print('You lost 25 points')
                    
            
            attempts += 1
            print(f"score: {score}")
            print(f'You have {tries - attempts} guesses left.')
            print('--------------------------------')

            

        game_state = 'end'

    if(game_state == 'end'):
        
        play_again = input("Do you wanna play again? (Yes/No): ")

        if(play_again.lower() == 'yes'):
            print('--------------------------------')
            print('--------------------------------')
            game_state = 'play'
            real_num = randint(1,100)
            attempts = 0
            

        elif(play_again.lower() == 'no'):
            if(not victory):
                print('Game Over.')
            if(victory):
                print('You won the game, thanks for playing.')
            break
            