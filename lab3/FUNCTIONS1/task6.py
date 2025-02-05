def reversed_sent():
    user = input()
    sentence = user.split()
    rev = sentence[::-1]
    rev_sen = ' '.join(rev)
    print("Reversed sentence:", rev_sen)
reversed_sent()
    