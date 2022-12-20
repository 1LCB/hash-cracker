import hashlib

word = input("enter some word: ").encode()

print(f"md5: {hashlib.md5(word).hexdigest()}")
print(f"sha-256: {hashlib.sha256(word).hexdigest()}")