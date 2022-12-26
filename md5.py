import hashlib, concurrent.futures, os


def verify(word):
    hashed_word = hashlib.md5(word.encode()).hexdigest() # create a md5 hash
    if hash_ == hashed_word:
        print(f'\n{hash_} => {word}')
        os._exit(0)


hash_ = input("enter your md5: ")

print("reading the wordlist.txt...")
with open('wordlist.txt', 'r') as file:
    wordlist = file.read().split('\n')
    for word in wordlist:
        if word == "":
            wordlist.remove(word)

print("analyzing...")
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(verify, wordlist)

print(f"\nyour hash couldn't be found in {len(wordlist)} words!\n")

input("press enter to continue")