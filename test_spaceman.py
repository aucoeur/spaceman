from spaceman import is_guess_in_word, letters_guessed, get_guessed_word, is_word_guessed

# def mock_guess(monkeypatch):
#     with monkeypatch.context() as m:
#         m.setattr('builtins.input', 'p')
#         guess = input('Enter a letter: ').lower()
#         assert guess == 'z', 'error with var guess'

def test_is_guess_in_word():

    assert is_guess_in_word('a', 'baloney') == True, 'is_guess_in_word() Error: new input in letters_guessed matches secret_word'

    assert is_guess_in_word('g', 'baloney') == False, 'is_guess_in_word() Error: duplicate input in letters_guessed'

    assert is_guess_in_word('t', 'baloney') == False, 'is_guess_in_word() Error: new input in letters_guessed, does not match secret_word'

def test_get_guessed_word():
    
    assert get_guessed_word('baloney', 'balonéy') == 'Answer: b a l o n _ y', 'get_guessed_word() Error'

    assert get_guessed_word('baloney', 'bologna')  == 'Answer: b a l o n _ _', 'get_guessed_word() Error'

    assert get_guessed_word('baloney', 'blanoey') == 'Answer: b a l o n e y', 'get_guessed_word() Error' 

def test_is_word_guessed():

    assert is_word_guessed('baloney','baloney') == True, 'Error: should return true'

    assert is_word_guessed('baloney', 'blanoey') == True, 'Error: same letters, different order'


if '__name__' == '__main__':
    test_is_guess_in_word()
    test_get_guessed_word()
    test_is_word_guessed()