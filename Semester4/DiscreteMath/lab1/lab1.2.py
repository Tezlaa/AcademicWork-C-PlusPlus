def word_set(word: str) -> set:
    return set(word)


if __name__ == '__main__':
    word_1 = 'roundooodd'
    word_2 = 'world'
    word_3 = 'BogdanTishenko'

    print(word_set(word_1))
    print(word_set(word_2))
    print(word_set(word_3))
