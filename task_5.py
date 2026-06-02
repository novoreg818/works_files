try:
    file = open('words.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    words = []
    for line in lines:
        clean_word = line.strip()
        if len(clean_word) > 0:
            words.append(clean_word)

    words_alpha = words.copy()
    words_alpha.sort(key=str.lower)

    file_alpha = open('sorted_alphabetically.txt', 'w', encoding='utf-8')
    for w in words_alpha:
        file_alpha.write(w + "\n")
    file_alpha.close()
    print("Файл sorted_alphabetically.txt создан.")

    words_len = words.copy()
    words_len.sort(key=len)

    file_len = open('sorted_by_length.txt', 'w', encoding='utf-8')
    for w in words_len:
        file_len.write(w + "\n")
    file_len.close()
    print("Файл sorted_by_length.txt создан.")

    words_rev = words.copy()
    words_rev.sort(key=str.lower, reverse=True)

    file_rev = open('sorted_reverse.txt', 'w', encoding='utf-8')
    for w in words_rev:
        file_rev.write(w + "\n")
    file_rev.close()
    print("Файл sorted_reverse.txt создан.")

    print("Сортировка успешно завершена.")

except FileNotFoundError:
    print("Ошибка: Файл words.txt не найден.")