import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time()

write_words(10, 'тип_первый_текстовик.txt')
write_words(30, 'тип_второй_текстовик.txt')
write_words(200, 'тип_третий_текстовик.txt')
write_words(100, 'тип_четвертый_текстовик.txt')

end_time = time()
print(f"Время работы функций: {end_time - start_time:.6f} секунд")

threads = []
start_time_threads = time()

thread_args = [
    (10, 'Тип_пятый_текстовик.txt'),
    (30, 'Тип_шестой_текстовик.txt'),
    (200, 'Тип_сельмой_текстовик.txt'),
    (100, 'Тип_восьмой_текстовик.txt')
]

for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Время работы потоков: {end_time_threads - start_time_threads:.6f} секунд")
