def read_text():
    with open('data.txt', 'r', encoding='utf-8') as file:
        return file.read().split()


def write_text(text):
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write(text)
