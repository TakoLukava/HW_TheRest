words = str(input('Enter set of words, please: '))
separator = input('Enter separator: ')

def len_n_words():
    lis = words.split()
    count = 0

    while count < len(lis):
        lis[count] = str(len(lis[count])) + lis[count]
        count += 1
    return lis

print(len_n_words())


