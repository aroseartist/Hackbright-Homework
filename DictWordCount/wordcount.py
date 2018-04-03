
#opens test text
def count_spaces(file_name):
    log_text = open(file_name)
    word_count = {}
    for line in log_text:
        line = line.rstrip()
        clean_line = line.strip(".")
        clean_line_1 = clean_line.strip(",")
        words = clean_line_1.split(" ")
        for word in words:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1
            sorted_word_count = sorted(word_count)
    for word in sorted_word_count:
        quantity = sorted_word_count[word]
        print word, quantity

    log_text.close()

count_spaces("test.txt")
