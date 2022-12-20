import string, itertools

ascii_lowercases = list(string.ascii_lowercase)

MAX_WORD_LENGTH = 5

for i in range(1, MAX_WORD_LENGTH + 1):
    charlist = [[x for x in ascii_lowercases]] * i

    for combinations in itertools.product(*charlist):
        combinations = "".join(combinations)
        with open("../wordlist.txt", "a") as file:
            file.write(combinations + "\n")
    print("finished!", i)