def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]

if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
