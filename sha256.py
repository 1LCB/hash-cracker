import hashlib, concurrent.futures, os


def verify(word):
    hashed_word = hashlib.sha256(word.encode()).hexdigest()
    if hash_ == hashed_word:
        print(f'\n{hash_} => {word}')
        os._exit(0)


hash_ = input("enter your sha-256: ")

print("reading the wordlist.txt...")
with open('wordlist.txt', 'r') as file:
    wordlist = list(map(lambda x: x.replace("\n", ""), file.readlines()))

print("analyzing...")
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(verify, wordlist)

print(f"\nyour hash couldn't be found in {len(wordlist)} words!\n")

input("press enter to continue")