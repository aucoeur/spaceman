test = ['s','g','d','t','y','g','l','w','b','r']
secret_word = 'stare'
reveal = [x for x in secret_word if x in test]
hide = [x for x in secret_word if x not in test]
print(secret_word)
print(len(secret_word))

def check():
    print(reveal)
    print(hide[0].replace(hide[0], '_'))


def check2():
    print(set(secret_word).intersection(test))
    print(set(secret_word).difference(test))