import re
import itertools


def parse_text(text: str, k: int = 10, n: int = 4):
    all_sent = amount_of_sentences(text)
    all_non_dec_sent = amount_of_non_declarative_sentences(text)
    av_len_of_sent = average_len_of_sent(text)
    av_word_len = average_word_len(text)
    top_n_grams = n_grams(text, k, n)
    return f"Amount_of_sentences: {all_sent}\nAmount_of_non_declarative_sentences: {all_non_dec_sent}\n" \
           f"Average length of the sentence: {av_len_of_sent}\nAverage length of the word: {av_word_len}\n" \
           f"N-grams result: {top_n_grams}"


def amount_of_sentences(text):
    size = 0
    abbreviations = {"al.", "i.e.", "e.g.", "Mr.", "Mrs.", "Dr.", "Lt.", "Rep.", "Jan.", "Feb.", "Mar.", "Apr.", "Jun.",
                     "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec.", "Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat.",
                     "Sun.",  "sec.", "in.", "lbs.", "min.", "hr.", "wk.", "cent.", "yr."}
    words = text.split()
    for word in words:
        if len(word) > 1 and word not in abbreviations and not word[-2].isupper() and word.endswith(".") or word.endswith("!") or word.endswith("?") or word.endswith("..."):
            size += 1
    return size


def amount_of_non_declarative_sentences(text):
    size = 0
    for word in text:
        if word.endswith("!") or word.endswith("?"):
            size += 1
    return size


def average_len_of_sent(text):
    amount_of_chars = 0
    words = text.split(" ")
    for word in words:
        if re.match("^[0-9.]*$", word):
            continue
        elif word.endswith("..."):
            amount_of_chars += len(word) - 3
        elif word.endswith(".") or word.endswith("!") or word.endswith("?") or word.endswith(","):
            amount_of_chars += len(word) - 1
        else:
            amount_of_chars += len(word)
    return amount_of_chars / amount_of_sentences(text)


def average_word_len(text):
    amount_of_chars = 0
    words = text.split()
    amount_of_words = len(words)
    if amount_of_words == 0:
        return 0
    for word in words:
        if not re.match("^[A-Za-z'.]*$", word):
            amount_of_words -= 1
            continue
        elif word.endswith("..."):
            amount_of_chars += len(word) - 3
        elif word.endswith(".") or word.endswith("!") or word.endswith("?") or word.endswith(","):
            amount_of_chars += len(word) - 1
        else:
            amount_of_chars += len(word)
    return amount_of_chars / amount_of_words


def n_grams(text, k, n):
    words = text.split()
    n_gr = dict()
    for word in words:
        i = 0
        while i + n <= len(word):
            if word[i:i + n] in n_gr.keys():
                n_gr[word[i:i + n]] += 1
            else:
                n_gr[word[i:i + n]] = 1
            i += 1
    top_n_grams = dict(itertools.islice((sorted(n_gr.items(), key=lambda v: v[1], reverse=True)), k))
    return top_n_grams


def main():
    """text = "Deborah D.K. was angry at her son. Her son didn't listen to her. Her son was 16 yr. old. " \
           "Her son thought he knew everything. Her son yelled at Deborah. " \
           "He told her he didn't have to do anything. He didn't have to listen to her. " \
           "He didn't have to go to school. He didn't have to do his homework. He didn't have to study. He was 16. " \
           "He could do anything he wanted to do. What could Deborah do? She wasn't married. She was divorced. " \
           "Could she control her son? He would listen to his father. But his father was not there. " \
           "In Feb. his father moved in another city." """
    """text = input("Enter text:\n")
    ans = input("Do you want to change K and N for N-grams? [y/n]\n")
    if ans.lower() == "y":
        K = int(input("Enter K: "))
        N = int(input("Enter N: "))
        print(parse_text(text, K, N))
    else:
        print(parse_text(text)) """
    print(average_word_len("Her son A1B2C3 didn't listen to her. Her son was 16 yr. old..."))


if __name__ == "__main__":
    main()
