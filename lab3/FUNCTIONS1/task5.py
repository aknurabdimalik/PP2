import itertools
def permut_word():
    word = input()
    permut = itertools.permutations(word)
    for perm in permut:
        print(''.join(perm))
        
permut_word()