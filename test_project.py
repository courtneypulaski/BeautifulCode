from project import validate_guess
from project import check_guess
from project import format_result
from project import GuessingGame

def test_validate_guess():
    game = GuessingGame(3,3,True)
    game.available_colors = [(1,'red','🔴'),(2,'orange','🟠'),(3,'yellow','🟡')]
    assert validate_guess(game, 'blue, green, red') == ''
    assert validate_guess(game, 'red, red, red, red') == ''
    assert validate_guess(game, 'red, yellow, orange') == [1,3,2]
    assert validate_guess(game, 'blue green red') == ''
    assert validate_guess(game, 'red red red red') == ''
    assert validate_guess(game, 'red yellow orange') == [1,3,2]
    assert validate_guess(game, 'b,g,r') == ''
    assert validate_guess(game, 'r r r r') == ''
    assert validate_guess(game, 'r y o') == [1,3,2]
    game.available_colors = [(4,'green','🟢'),(5,'blue','🔵'),(6,'purple','🟣')]
    assert validate_guess(game, 'red, yellow, orange') == ''
    assert validate_guess(game, 'blue, green, green') == [5,4,4]
    game.available_colors = [(4,'green','🟢'),(5,'blue','🔵'),(6,'purple','🟣'),(2,'orange','🟠'),(3,'yellow','🟡')]
    assert validate_guess(game, 'green, blue') == ''
    assert validate_guess(game, 'orange, blue, green') == [2,5,4]
    assert validate_guess(game, 'g   b') == ''
    assert validate_guess(game, 'o   b   g') == ''
    game = GuessingGame(4,2,True)
    assert validate_guess(game, 'orange, blue, green') == ''
    game.available_colors = [(4,'green','🟢'),(5,'blue','🔵'),(6,'purple','🟣')]
    assert validate_guess(game, 'blue, purple,green,blue') == [5,6,4,5]

def test_check_guess():
    game = GuessingGame(3,3,True)
    game.available_colors = [(4,'green','🟢'),(5,'blue','🔵'),(6,'purple','🟣'),(2,'orange','🟠'),(3,'yellow','🟡'),(1,'red','🔴')]
    game.pattern = [1,3,4,3]
    assert check_guess(game, [1,2,3,4]) == '1022'
    assert check_guess(game, [1,4,1,3]) == '1201'
    game.pattern = [1,5,3,2,1]
    assert check_guess(game, [1,1,5,3,1]) == '10221'

def test_format_result():
    game = GuessingGame(3,3,True)
    assert format_result(game, '11201') == "Right Place ✅: 3; Wrong Place ➖: 1"
    assert format_result(game, '1110') == "Right Place ✅: 3; Wrong Place ➖: 0"
    assert format_result(game, '22120') == "Right Place ✅: 1; Wrong Place ➖: 3"
    assert format_result(game, '21012') == "Right Place ✅: 2; Wrong Place ➖: 2"
    assert format_result(game, '22100') == "Right Place ✅: 1; Wrong Place ➖: 2"
    game = GuessingGame(3,3,False)
    assert format_result(game, '11201') == "✅✅➖⛔✅"
    assert format_result(game, '1110') == "✅✅✅⛔"
    assert format_result(game, '22120') == "➖➖✅➖⛔"
    assert format_result(game, '21012') == "➖✅⛔✅➖"
    assert format_result(game, '22100') == "➖➖✅⛔⛔"
