import requests, random, json, string, os
from console.utils import set_title

os.system('cls')

def title(text):
    set_title(text)

def hiddenNameGen():
    length = random.randint(4, 16)
    letters = "Il"
    return ''.join(random.choice(letters) for i in range(length))

def regularNameGen():
    length = random.randint(4, 16)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def lengthNameGen(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

title('Name Generator by ArilisDev | Tried: 0 | Used: 0 | Available: 0')

choice = input('Choose your name generator option!\n(1) Regular Name Generator\n(2) Hidden Name Generator\n(3) Generate by Length\nChoice: ')

tried = 0
used = 0
available = 0

if choice == '1':
    while True:
        name = regularNameGen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            print('[+]: ' + name + ' is available!')
            title('Name Generator by ArilisDev | Tried: ' + str(tried) + ' | Used: ' + str(used) + ' | Available: ' + str(available))
        else:
            tried = tried + 1
            used = used + 1
            title('Name Generator by ArilisDev | Tried: ' + str(tried) + ' | Used: ' + str(used) + ' | Available: ' + str(available))

if choice == '2':
    while True:
        name = hiddenNameGen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            title('Name Generator by ArilisDev | Tried: ' + str(tried) + ' | Used: ' + str(used) + ' | Available: ' + str(available))
            print('[+]: ' + name + ' is available!')
        else:
            tried = tried + 1
            used = used + 1
            title('Name Generator by ArilisDev | Tried: ' + str(tried) + ' | Used: ' + str(used) + ' | Available: ' + str(available))

if choice == '3':
    length = int(input('How long would you like the username? (4-16): '))
    while True:
        name = lengthNameGen(length)
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            title('Name Generator by ArilisDev | Tried: ' + str(tried) + ' | Used: ' + str(used) + ' | Available: ' + str(available))
            print('[+]: ' + name + ' is available!')
        else:
            tried = tried + 1
            used = used + 1
            title('Name Generator by ArilisDev | Tried: ' + str(tried) + ' | Used: ' + str(used) + ' | Available: ' + str(available))
