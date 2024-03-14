import sys
import random

class GuessingGame:
    all_colors = [(1,'red','🔴'),(2,'orange','🟠'),(3,'yellow','🟡'),(4,'green','🟢'),(5,'blue','🔵'),(6,'purple','🟣')]

    def __init__(self, spaces, colors, hard_mode):
        random.shuffle(self.all_colors)
        self._available_colors = self.all_colors[0:colors]
        self.hard_mode = hard_mode
        self.max_guesses = 3
        if self.hard_mode:
            self.max_guesses += 2
        if spaces >= 5:
            self.max_guesses += 1
        if spaces >= 7:
            self.max_guesses += 1
        if colors >= 5:
            self.max_guesses += 1
        self.current_guess = 1
        self.generate_pattern(spaces)


    def __str__(self):
        cols = ''
        for num in self.pattern:
            for i in self.available_colors:
                if num == i[0]:
                    cols += str(i[2])
                    break
        return cols

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self,pattern):
        self._pattern = pattern
        self._count = self._generate_count(pattern)

    @property
    def pattern_counts(self):
        return self._count

    @property
    def available_colors(self):
        return self._available_colors

    @available_colors.setter
    def available_colors(self, colors):
        self._available_colors = colors

    def generate_pattern(self, spaces):
        spaces = int(spaces)
        temp_pattern = []
        # generate a pattern, a list of color numbers
        for _ in range(spaces):
            temp_pattern.append(random.choice(self.available_colors)[0])
        self.pattern = temp_pattern

    def _generate_count(self, count_pattern):
        # for later use, count how many of each number is in the pattern
        temp_counts = {}
        for i in count_pattern:
            temp_counts[i] = temp_counts.get(i,0) + 1
        return temp_counts

    def get_guess(self):
        guess_colors = ''
        # get a string of the names of available colors
        for i in self.available_colors:
            guess_colors += f"{str(i[1])} ({str(i[1][0])})"
            # formatting stuff below
            if i != self.available_colors[-1]:
                guess_colors += ', '
            if i == self.available_colors[-2]:
                guess_colors += 'and '
        current_guess = ''
        # get a guess from the user, send it to validation; repeat if it's not valid
        while current_guess == '':
            current_guess = input(f"Enter a guess, using {len(self.pattern)} of the colors {guess_colors} separated by commas or single spaces: ")
            if current_guess.strip().lower() == 'quit' or current_guess.strip().lower() == 'end':
                print("Game Ended.")
                print(f"Pattern: {self}")
                return 'quit'
            current_guess = validate_guess(self, current_guess)
        # current_guess is a list of numbers
        return current_guess

def format_result(curr_game, result):
    # reformats the string if hard mode is on
    new_result = ''
    if curr_game.hard_mode == True:
        #print('hard mode')
        counts = {'✅': 0, '➖': 0, '⛔': 0}
        for i in range(len(result)):
            if result[i] == '1':
                counts['✅'] += 1
            elif result[i] == '2':
                counts['➖'] += 1
            elif result[i] == '0':
                counts['⛔'] += 1
        #print(f"counts: {counts}")
        new_result = f"Right Place ✅: {counts['✅']}; Wrong Place ➖: {counts['➖']}"
    else:
        #print('easy mode')
        for i in range(len(result)):
            if result[i] == '1':
                new_result += '✅'
            elif result[i] == '2':
                new_result += '➖'
            elif result[i] == '0':
                new_result += '⛔'
    return new_result

def validate_guess(curr_game, guess):
    # guess is a string, hopefully of color words
    # get the list of names of valid colors
    col_names = []
    for i in curr_game.available_colors:
        col_names.append(i[1])
        col_names.append(i[1][0])
    # make sure it's a list of the right number of colors
    if ',' in guess:
        guess_list = guess.split(',')
    else:
        guess_list = guess.split(' ')
    if len(guess_list) != len(curr_game.pattern):
        print(f"Wrong number of colors- Make sure your guess has {len(curr_game.pattern)} colors separated by commas or single spaces.")
        return ''
    # check each color name, make sure it's a valid guess, and replace it with the corresponding number
    for i in range(len(guess_list)):
        guess_list[i] = guess_list[i].strip()
        if guess_list[i] == '':
            continue
        if guess_list[i] not in col_names:
            print(f"{guess_list[i]} is not a valid color for the current game configuration.")
            return ''
        for j in curr_game.available_colors:
            if guess_list[i] == j[1] or guess_list[i] == j[1][0]:
                guess_list[i] = j[0]
                break
    # guess_list is a list of numbers
    return guess_list

def check_guess(curr_game, guess):
    # result is a string of numbers. 0 = not in pattern, 1 = right spot, 2 = wrong spot
    first_pass = ''
    #print(f"pattern_counts: {curr_game.pattern_counts}")
    # need to use dict() to create a copy and not another reference to the same object
    temp_counts = dict(curr_game.pattern_counts)
    #print(f"initial counts: {temp_counts}")
    # first pass, look for exact matches
    for i in range(len(guess)):
        #print(f"element being compared: {guess[i]}")
        #print(f"number of remaining: {temp_counts.get(guess[i],0)}")
        if guess[i] == curr_game.pattern[i]:
            first_pass += '1'
            temp_counts[guess[i]] -= 1
        else:
            first_pass += '-'
        #print(f"new counts: {temp_counts}")
        #print(f"first pass result: {first_pass}")
    result = ''
    if '-' in first_pass:
        for i in range(len(guess)):
            if first_pass[i] == '-' and guess[i] in curr_game.pattern and temp_counts.get(guess[i],0) > 0:
                result += '2'
                temp_counts[guess[i]] -= 1
            elif first_pass[i] == '1':
                result += '1'
            else:
                result += '0'
        #print(f"new counts: {temp_counts}")
    else:
        result = first_pass
    return result

def determine_result(curr_game, guess):
    result = check_guess(curr_game, guess)
    #print(f"end result: {result}")
    if result == '1' * len(curr_game.pattern):
        #print("MATCH!")
        result = 'match'
    else:
        result = format_result(curr_game, result)
        #print(f"formatted result: {result}")
    return result


def main():
    game_stat = get_action()
    if game_stat == (0,0,0):
        return
    print("Lets Play!")
    game = GuessingGame(game_stat[0],game_stat[1],game_stat[2])
    print(f"{game.max_guesses} Guesses Available.")
    while game.current_guess <= game.max_guesses:
        #print(f"current guess: {game.current_guess}")
        #print(f"guesses allowed: {game.max_guesses}")
        guess = game.get_guess()
        #print(guess)
        #print(game.pattern)
        if guess == 'quit':
            return
        result = determine_result(game, guess)
        if result == 'match':
            print("You Win!")
            print(game)
            game.current_guess = game.max_guesses + 1
        elif game.current_guess < game.max_guesses:
            print(f"Result: {result}")
            if game.hard_mode == False:
                print("✅: Right Spot, ➖: Wrong Spot, ⛔: Not Present")
            print("Try Again!")
            game.current_guess += 1
        else:
            game.current_guess += 1
    if result != 'match':
        print("All guesses used. Play Again.")
        print(f"Pattern: {game}")


def test_main():
    game = GuessingGame(3,3,True)
    game.available_colors = [(4,'green','🟢'),(5,'blue','🔵'),(6,'purple','🟣'),(2,'orange','🟠'),(3,'yellow','🟡'),(1,'red','🔴')]
    game.pattern = [1,5,3,2,1]
    current_guess = [1,5,3,2,1]
    print(f"guess: {current_guess}")
    print(f"pattern: {game.pattern}")
    result = check_guess(game, current_guess)
    if result == 'match':
        print("You Win!")
        print(game)
    else:
        print("Try Again")


def get_action():
    print("Welcome to the Color Guesser!")
    data = 0
    game = []
    while data < 3:
        try:
            if data == 0:
                action = input("How many SPACES (3-8) should there be? ").strip().lower()
            elif data == 1:
                action = input("How many COLORS (2-6) do you want to guess with? ").strip().lower()
            elif data == 2:
                action = input("Do you want to play HARD MODE? Y/N: ").strip().lower()
        except EOFError:
            action = 'quit'
            print('')
        if action == "quit":
            print("Thanks for playing!")
            return (0,0,0)
        elif action == "help":
            if data == 0:
                print("* Enter the number of spaces you wish to guess. For example, a 3 would result in a board like this: ⚪⚪⚪")
            elif data == 1:
                print("* Enter the number of colors you wish to guess. If 6 is entered, all available colors (🔴🟠🟡🟢🔵🟣) will be used.")
            elif data == 2:
                print("* Hard Mode means an incorrect guess will be given the number correct, in the right space or not, but not the locations.")
        else:
            if data == 0 or data == 1:
                try:
                    guesses = int(action)
                except ValueError:
                    print("Please enter a number.")
                    continue
                else:
                    if data == 0 and (guesses <= 2 or guesses >= 9):
                        print("Ensure your number of guesses is between 3 and 8")
                        continue
                    elif data == 1 and (guesses <= 1 or guesses >= 7):
                        print("Ensure your number of colors is between 2 and 6")
                        continue
                    else:
                        data += 1
                        game.append(guesses)
            elif data == 2:
                if action not in ('y','n'):
                    print("Not a valid response, try again")
                else:
                    game.append(action == 'y')
                    data += 1
    return tuple(game)




if __name__ == "__main__":
    while True:
        main()
        restart = input("Play Again? Enter Y/N: ").strip().lower()
        if restart != 'y':
            break
