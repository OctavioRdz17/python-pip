import random

def choise_options():
    options = ('piedra','papel','tijera')
    user_option =  input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    computer_option = random.choice(options)
    print(f'***The computer choosed => {computer_option.upper()}***')

    #revisar la opcion del usuario
    if user_option not in options:
        print('Esa opcion no es valida')
        return None, None

    return user_option,computer_option

def check_rules(user_option, computer_option,user_wins,computer_wins):
    if user_option == computer_option:
        print('empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('Usted gano')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Usted gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Usted gano')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano')
            computer_wins += 1
    return user_wins,computer_wins

def check_score(user_wins,computer_wins):
    if computer_wins == 2:
        print('🎖️ El ganador es Computer 🎖️')
        return False
    if user_wins == 2:
        print('🎖️ El ganador es User 🎖️a')
        return False
    return True
        

def run_game():
    #inicializa las variables
    computer_wins = 0
    user_wins = 0
    rounds =  1

    while True:
        print('*'*10)
        print('ROUND',rounds)
        print('*'*10)
        print('COMPUTER',computer_wins,"VS",'USER',user_wins)

        rounds += 1

        # we create the options vars for computer and user
        user_option ,computer_option,= choise_options()
        #function to check the rules for each game
        user_wins,computer_wins=check_rules(user_option, computer_option,user_wins,computer_wins)

        game_continue = check_score(user_wins,computer_wins)
        if not game_continue:break
            
    


run_game()