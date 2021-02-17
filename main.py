import random


def get_word():
    word_dict = {'Animal': ['cat', 'dog', 'fish', 'horse', 'lizard', 'snake', 'wolf', 'fox', 'mouse', 'turtle'],
                 'Furniture': ['bed', 'chair', 'table', 'wardrobe', 'stool', 'bookcase', 'drawer'],
                 'Fruits': ['apple', 'pineapple', 'banana', 'orange', 'mango', 'watermelon', 'strawberry', 'kiwi',
                            'grape', 'cherry'],
                 'Colors': ['red', 'blue', 'yellow', 'green', 'purple', 'white', 'black', 'pink', 'orange', 'brown'],
                 'Sport': ['soccer', 'football', 'basketball', 'swimming', 'cycling', 'tennis', 'running', 'baseball',
                           'volleyball', 'climbing']
                 }
    word1 = random.choice(random.choice(list(word_dict.values())))
    category1 = get_key(word1, word_dict)
    return [word1, category1]


def get_key(val, dict):
    for key, value in dict.items():
        if val in value:
            return key


if __name__ == '__main__':
    word_list = get_word()
    word = word_list[0]
    category = word_list[1]
    curr = '_' * len(word)
    fail = ''
    success = ''
    mistakes = 0
    while mistakes < 5 and (not curr.__eq__(word)):
        print(f'the category is {category}')
        print(f'the letters of the word you have so far are {curr}\nyou have {5 - mistakes} mistakes left')
        if mistakes > 0:
            print(f'the mistakes so far are {fail}')
        guess = input('please enter a letter\n')
        if not len(guess) == 1:
            print('\nillegal input\n')

        elif (guess in success) or (guess in fail):
            print('\nyou already made that guess\n')

        else:
            if guess in word:
                success = success + guess + ','
                for i in range(0, len(word)):
                    if word[i].__eq__(guess):
                        if 0 < i < len(word):
                            curr = curr[:i] + word[i] + curr[i + 1:]
                        elif i == 0:
                            curr = word[i] + curr[i + 1:]
                        else:
                            curr = curr[:i] + word[i]
                print('\nyou guessed correctly :)\n')
            else:
                fail = fail + guess + ','
                mistakes = mistakes + 1
                print('the guess was incorrect :(')

    if mistakes < 5:
        print('\ncongratulations, you won')

    else:
        print('\nyou lost, better luck next time')
