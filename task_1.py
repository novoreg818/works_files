try:
    file = open('input.txt', 'r', encoding='utf-8')
    text = file.read()
    file.close()

    lines_count = 0
    if len(text) > 0:
        lines = text.split('\n')
        lines_count = len(lines)

    words = text.split()
    words_count = len(words)

    out_file = open('statistics.txt', 'w', encoding='utf-8')
    out_file.write("Количество строк: " + str(lines_count) + "\n")
    out_file.write("Количество слов: " + str(words_count) + "\n")
    out_file.close()

    print("Файл statistics.txt успешно создан. Строк:", lines_count, "Слов:", words_count)
except FileNotFoundError:
    print("Ошибка: Файл input.txt не найден. Пожалуйста, создайте его.")