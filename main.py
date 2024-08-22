import random
import string


def Getinput(text):
    while True:
        vall = input(text)
        if len(vall) > 0:
            break
        print("you must enter some words!")
    return vall

sifra = " " + string.punctuation + string.digits + string.ascii_letters
sifra = list(sifra)
klic = sifra.copy()

random.shuffle(klic)

#sifrovani
sifrovani = Getinput("Enter your message")
desifrovani = ""

for letter in sifrovani:
    index = sifra.index(letter)
    desifrovani += klic[index]

print(f"originální zpráva: {sifrovani}")
print(f"encryptovaná zpráva: {desifrovani}")


#desifrovana zprava
desifrovani = Getinput("Enter encrypted message")
sifrovani = ""

for letter in desifrovani:
    index = klic.index(letter)
    sifrovani += sifra[index]

print(f"encrypted message: {desifrovani}")
print(f"original message: {sifrovani}")
