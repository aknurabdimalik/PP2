def histogram(lst):
    for number in lst:
        print('*' * number)
input_list = list(map(int, input().split()))

histogram(input_list)
