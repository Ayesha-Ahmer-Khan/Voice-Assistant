from word2number import w2n

def normalize_numbers(text):
    words = text.split()
    output = []

    for word in words:
        clean = word.lower().strip(",.")
        try:
            number = w2n.word_to_num(clean)
            output.append(str(number))
        except:
            output.append(word)

    return " ".join(output)