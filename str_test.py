test = ['s','g','d','t','y','g','l','w','b','r']
secret_word = 'stare'

reveal = [x for x in secret_word if x in test]
hide = [x for x in secret_word if x not in test]

underscore = '_'
ans_list = []

print(secret_word)
print(len(secret_word))

def check():
    pass
    
def check2():
    print(frozenset(secret_word).intersection(test))
    print(frozenset(secret_word).difference(test))


print(reveal)
print(hide)

def test1():
    for item in secret_word:
        if item in test:
            ans_list.append(item)
        else:
            ans_list.append(underscore)

    print(' '.join(ans_list))

def set_test():
    i = 0
    while i < (len(secret_word)):
        char = secret_word[i]

        if set(test).intersection(char):
            print(*char)
        else:
            print(*'_')
        i += 1