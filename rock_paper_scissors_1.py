from shutil import get_terminal_size
from os import name, system
from time import sleep
import random
import textwrap
import sys

# Database
player1_default_title = ['You', 'Your Majesty', 'Player 1', 'The mighty human', 'The weak organic form']
player1_title = ['You', 'Your Majesty', 'Player 1', 'The mighty human', 'The weak organic form']
current_name = 'Default'
player2_title = ['The computer', 'The machine', 'Botio Botev', 'The stupid calculator', 'The ugly bot']
message_move = ['Make your move: ', 'Your turn: ', 'Choose your destiny: ', 'Play: ', 'What will you do?: ']
message_draw = ['', 'Are you a copy of my bot?', 'Are you coping my moves?', 'This is getting boring...']
player1_round = [f'{random.choice(player1_title)} won this round!',
                 f'{random.choice(player1_title)} got him this time!',
                 f'{random.choice(player1_title)} scored!',
                 f'{random.choice(player1_title)} got lucky this time!']
player2_round = [f'{random.choice(player2_title)} won this round!',
                 f'{random.choice(player2_title)} got you this time!',
                 f'{random.choice(player2_title)} scored!',
                 f'{random.choice(player2_title)} got lucky this time!']
draw_round = [f'It\'s a draw! {random.choice(message_draw)}', f'DRAW! {random.choice(message_draw)}', 'Tie', 'No score']
jokes = ['If I got paid to play rock paper scissors, I would be making money hand over fist.', 'Dwayne Johnson (The Rock) asked; “go ahead! Name any wrestler, and I bet I could beat him.” She replied; “what about a wrestler named Paper?”', 'Make a pair of scissors, specifically designed to cut paper, made out of sharpened stone. Call them Rock Paper Scissors.', 'Rock music always beat Scissors’ sister. At least on Paper…', 'I misplaced Dwayne Johnson’s cutting tool for the origami workshop. I can’t believe I lost the Rock’s Paper Scissors.', 'Why is it pointless to throw Scissors in a game of rock-paper-scissors against an illegal immigrant? Because they do not have papers.', 'I just won the most exciting rock paper scissors match of my life. The cop said “Papers” I said “Scissors” and immediately drove away. He must have been crazy for a rematch because he chased me for 10 minutes!', 'Rap is like scissors. It always loses to rock.']
computer_move = [1, 2, 3]
moves = [0, 'ROCK', 'PAPER', 'SCISSORS']
typewrite = True
typewrite_on_off = 'OFF'
points_to_win = 5


def main():

    def screen_width():
        width, rows = get_terminal_size()
        return width

    def clear():
        sleep(2)
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def typewriter(message, mode):
        if mode:
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            print()
        else:
            print(message)

    def options():
        while True:
            title_screen()
            global current_name
            global typewrite
            global typewrite_on_off
            global points_to_win

            print(f'1. Change name ({current_name})')
            print(f'2. Turn {typewrite_on_off} Typewriter')
            print(f'3. Set points to win game ({points_to_win})')
            print('4. Back')
            print()
            typewriter('\033[38;5;8mEnter (1), (2), (3) or (4)\033[0;0m', typewrite)
            choice = input()
            if choice not in ['1', '2', '3', '4']:
                typewriter('Invalid input. Please enter (1), (2), (3) or (4)', typewrite)
                clear()
                continue
            if choice == '1':
                clear()
                title_screen()
                custom_name = input('Enter your name (max. 12 letters): ')
                if 1 > len(custom_name) or len(custom_name) > 12:
                    typewriter('Invalid input. Please enter between 1 and 12 letters', typewrite)
                    sleep(2)
                    continue
                elif not custom_name.isalpha():
                    typewriter('Invalid input. Only letters allowed', typewrite)
                    sleep(2)
                    continue
                global player1_title
                player1_title = [custom_name]
                current_name = custom_name
                clear()
                continue
            elif choice == '2':
                if typewrite:
                    typewrite = False
                    typewrite_on_off = 'ON'
                else:
                    typewrite = True
                    typewrite_on_off = 'OFF'
                clear()
                continue
            elif choice == '3':
                clear()
                title_screen()
                custom_points_to_win = input('Enter the number of points to win the game (min.1, max.10): ')
                if not custom_points_to_win.isdigit():
                    typewriter('Invalid input. Please enter a digit', typewrite)
                    sleep(2)
                    continue
                elif 1 > int(custom_points_to_win) or int(custom_points_to_win) > 10:
                    typewriter('Invalid input. Please enter a digit between 1 and 10', typewrite)
                    sleep(2)
                    continue
                points_to_win = int(custom_points_to_win)
                clear()
                continue
            elif choice == '4':
                typewriter('Going back...', typewrite)
                clear()
                break

    def help_menu():
        print()
        print(textwrap.fill('\nRock-Paper-Scissors is a simple two-player game, where you and your opponent (the computer) simultaneously choose one of the following three options: "rock", "paper", or "scissors". The rules are as follows:', 80))
        print('· Rock beats scissors (the scissors get broken by the rock)\n'
              '· Scissors beats paper (the paper gets cut by the scissors)\n'
              '· Paper beats rock (the paper covers the rock)\n')
        print(textwrap.fill('The winner is the player whose choice beats the choice of his opponent. If both players choose the same option (e.g., "paper"), the game outcome is "draw". The default game is played until one player gets 5 wins.', 80))
        print()
        input('Press (Enter) to go back')
        clear()
        return

    def title_screen():
        game_name = f'\033[38;5;{str(random.randint(1, 255))}m                ROCK-PAPER-SCISSORS\033[0;0m'
        print('=' * screen_width())
        print(game_name.center(screen_width()))
        print('\033[38;5;8m              by boyko.gr | V1.00\033[0;0m'.center(screen_width()))
        print('='*screen_width())

    def start_screen():
        while True:
            title_screen()
            print('1. Start game')
            print('2. Options')
            print('3. Help')
            print('4. Exit game')
            print()
            typewriter('\033[38;5;8mEnter (1), (2), (3) or (4)\033[0;0m', typewrite)
            choice = input()
            if choice not in ['1', '2', '3', '4']:
                typewriter('Invalid input. Please enter (1), (2), (3) or (4)', typewrite)
                clear()
                continue
            if choice == '1':
                typewriter('Starting game...', typewrite)
                clear()
                game()
                continue
            elif choice == '2':
                typewriter('Opening Options...', typewrite)
                clear()
                options()
                continue
            elif choice == '3':
                help_menu()
                continue
            elif choice == '4':
                typewriter('Thank you for playing! Exiting game...', typewrite)
                clear()
                break

    def game():

        def round_result(p1, p2):
            print('...')
            clear()
            title_screen()
            typewriter(f'{random.choice(player1_title)} played {moves[p1]}', typewrite)
            sleep(0.5)
            typewriter(f'{random.choice(player2_title)} played {moves[p2]}', typewrite)
            sleep(0.5)
            if p1 == p2:
                return 0
            elif (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
                return 1
            else:
                return 2

        def stats():
            print()
            typewriter('STATISTICS', typewrite)
            print()
            sleep(1)
            typewriter(f'TURNS played: {turn}', typewrite)
            print()
            typewriter(f'Rock\'s played:  {p1_played_moves[0]} | {p1_won_moves[0]} of them were won | {p1_lost_moves[0]} were lost | {p1_draw_moves[0]} were tied', typewrite)
            print()
            typewriter(f'Paper\'s played: {p1_played_moves[1]} | {p1_won_moves[1]} of them were won | {p1_lost_moves[1]} were lost | {p1_draw_moves[1]} were tied', typewrite)
            print()
            typewriter(f'Scissors played: {p1_played_moves[2]} | {p1_won_moves[2]} of them were won | {p1_lost_moves[2]} were lost | {p1_draw_moves[2]} were tied', typewrite)
            print()
            input('Press (Enter) to go back to menu')
            typewriter('Going back to Menu...', typewrite)

        def after_game():
            while True:
                command_after_game = input('(1) NEW GAME | (2) STATISTICS | (3) BACK TO MENU\n')
                if command_after_game == '1':
                    typewriter('Starting new game...', typewrite)
                    clear()
                    return 'New'
                if command_after_game == '2':
                    stats()
                    clear()
                    return
                if command_after_game == '3':
                    typewriter('Going back to Menu...', typewrite)
                    clear()
                    return
                if command_after_game not in ['1', '2', '3']:
                    print('Invalid input. Please enter (1), (2) or (3).')
                    clear()
                    title_screen()
                    continue

        def check_score():
            if score1 == points_to_win:
                clear()
                for _ in range(5):
                    title_screen()
                    print()
                    print(f"\033[38;5;{random.randint(1, 255)}m                {random.choice(player1_title).upper()} WON THE GAME!\033[0;0m".center(screen_width()))
                    sleep(1)
                    clear()
                title_screen()
                print()
                print(f'{random.choice(player1_title).upper()} won the game!')
                print()
                return 'End'
            elif score2 == points_to_win:
                clear()
                title_screen()
                print()
                print(f'{random.choice(player1_title)} lost the game!'.center(screen_width()))
                print()
                return 'End'

        while True:
            turn = 1
            score1 = 0
            score2 = 0
            p1_played_moves = [0, 0, 0]
            p1_won_moves = [0, 0, 0]
            p1_lost_moves = [0, 0, 0]
            p1_draw_moves = [0, 0, 0]

            while True:
                if turn == 1:
                    title_screen()

                if check_score() == 'End':
                    if after_game() == 'New':
                        break
                    else:
                        return

                print(f'Score: Player {score1} | Computer {score2}')
                print()
                if score1 == points_to_win - 1 or score2 == points_to_win - 1:
                    print(f'ROUND {turn}. MATCH POINT!'.center(screen_width()))
                else:
                    print(f'ROUND {turn}'.center(screen_width()))
                print()
                print(f'{random.choice(message_move)}(1) ROCK | (2) PAPER | (3) SCISSORS | (4) JOKE | (0) BACK TO MENU\n')

                p1_move = input()
                p2_move = random.choice(computer_move)
                if p1_move not in ['1', '2', '3', '4', '0']:
                    print('Invalid input. Please enter (1), (2), (3), (4) or (0).')
                    clear()
                    if turn > 1:
                        title_screen()
                    continue
                if p1_move == '0':
                    typewriter('Going back to Menu...', typewrite)
                    clear()
                    return
                elif p1_move == '4':
                    print()
                    print(textwrap.fill(random.choice(jokes), 80))
                    print()
                    input('Press (Enter) to return to the game')
                    typewriter('Let\'s play...', typewrite)
                    clear()
                    if turn > 1:
                        title_screen()
                    continue
                else:
                    p1_played_moves[int(p1_move) - 1] += 1
                    result = round_result(int(p1_move), p2_move)
                    if result == 0:
                        p1_draw_moves[int(p1_move) - 1] += 1
                        typewriter(f'{random.choice(draw_round)}', typewrite)
                        print()
                        turn += 1
                    elif result == 1:
                        p1_won_moves[int(p1_move) - 1] += 1
                        score1 += 1
                        typewriter(f'{random.choice(player1_round)}', typewrite)
                        print()
                        turn += 1
                    elif result == 2:
                        p1_lost_moves[int(p1_move) - 1] += 1
                        score2 += 1
                        typewriter(f'{random.choice(player2_round)}', typewrite)
                        print()
                        turn += 1
                    else:
                        clear()
                        title_screen()
                        typewriter('Something went wrong. #@CK!', typewrite)

    start_screen()
    return


main()
