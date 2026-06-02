files_to_read = ['file1.txt', 'file2.txt', 'file3.txt']

try:
    out_file = open('combined.txt', 'w', encoding='utf-8')

    for filename in files_to_read:
        try:
            in_file = open(filename, 'r', encoding='utf-8')
            content = in_file.read()
            in_file.close()

            out_file.write("=== Содержимое " + filename + " ===\n")
            out_file.write(content + "\n\n")
            print("Файл", filename, "успешно добавлен.")
        except FileNotFoundError:
            print("Ошибка: Файл", filename, "не найден и будет пропущен.")

    out_file.close()
    print("Все доступные файлы объединены в combined.txt")

except Exception:
    print("Произошла ошибка при создании файла combined.txt")