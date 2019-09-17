from spaceman import is_guess_in_word, letters_guessed

# def mock_guess(monkeypatch):
#     with monkeypatch.context() as m:
#         m.setattr('builtins.input', 'p')
#         guess = input('Enter a letter: ').lower()
#         assert guess == 'z', 'error with var guess'

def test_is_guess_in_word():

    assert is_guess_in_word('a', 'baloney') == True, 'is_guess_in_word() Error: new input in letters_guessed matches secret_word'

    assert is_guess_in_word('g', 'baloney') == False, 'is_guess_in_word() Error: duplicate input in letters_guessed'

    assert is_guess_in_word('t', 'baloney') == False, 'is_guess_in_word() Error: new input in letters_guessed, does not match secret_word'


if '__name__' == '__main__':
    test_is_guess_in_word()