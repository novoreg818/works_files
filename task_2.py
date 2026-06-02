word_to_find = input("Введите слово для поиска: ").lower()

try:
    file = open('text.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    found = False
    count = 0
    found_lines = []

    line_number = 1
    for line in lines:
        words_in_line = line.split()
        line_has_word = False
        for w in words_in_line:
            if w.lower() == word_to_find:
                found = True
                line_has_word = True
                count += 1

        if line_has_word:
            found_lines.append(str(line_number))

        line_number += 1

    out_file = open('search_results.txt', 'w', encoding='utf-8')
    if found:
        print("Слово найдено!")
        print("Встречается раз:", count)
        print("В строках:", ", ".join(found_lines))

        out_file.write("Слово '" + word_to_find + "' найдено.\n")
        out_file.write("Встречается раз: " + str(count) + "\n")
        out_file.write("В строках: " + ", ".join(found_lines) + "\n")
    else:
        print("Слово не найдено в тексте.")
        out_file.write("Слово '" + word_to_find + "' не найдено.\n")
    out_file.close()
    print("Результаты записаны в search_results.txt")

except FileNotFoundError:
    print("Ошибка: Файл text.txt не найден.")