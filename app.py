import requests, random, json, string, os

os.system('cls')

def hiddenNameGen():
    length = random.randint(4, 16)
    letters = "Il"
    return ''.join(random.choice(letters) for i in range(length))

def regularNameGen():
    length = random.randint(4, 16)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

choice = input('Choose your name generator option!\n(1) Regular Name Generator\n(2) Hidden Name Generator\nChoice: ')

if choice == '1':
    while True:
        name = regularNameGen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            print('[+]: ' + name + ' is available!')

if choice == '2':
    while True:
        name = hiddenNameGen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            print('[+]: ' + name + ' is available!')
