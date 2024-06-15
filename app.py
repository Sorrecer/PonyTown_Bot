from PIL import Image
from datetime import datetime
import time, random, re, pyautogui, pytesseract, os, requests, subprocess, rpg, sys, hashlib
###======= Bot Configuration =======###

BotName = "Rick's Bot"
Admin_name = ['I AM RICK']
prefix = ['+', '>', '-']
apikey="AIzaSyDIdODxrZYkAnzKAic1eR3NVSG69WVSRKA"
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
###======= Bot Configuration =======###



###======= Setup =======###
# try:
#     import pytesseract
# except ModuleNotFoundError:
#     os. system("pip install pytesseract")

# try:
#     import PIL
# except ModuleNotFoundError:
#     os. system("pip install pillow")

# try:
#     import pyautogui
# except ModuleNotFoundError:
#     os. system("pip install pyautogui")
###======= Setup =======###

def send_ceks_in_parts(ceks):
    max_length = 70
    # Ganti enter dengan spasi dan hapus spasi ekstra di awal/akhir teks
    ceks = ceks.replace('\n', ' ').strip()
    words = ceks.split(' ')
    
    current_part = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= max_length:  # +1 untuk spasi yang akan ditambahkan
            current_part.append(word)
            current_length += len(word) + 1
        else:
            kirim_pesan(' '.join(current_part))
            time.sleep(3)
            current_part = [word]
            current_length = len(word) + 1
    
    # Kirim bagian terakhir jika ada kata yang tersisa
    if current_part:
        kirim_pesan(' '.join(current_part))

async def cai(username):
    bye = False
    char = 'eAMpTA3e6NMJBKdaeLhef2i_gAFzK4e8ZBjETRbEajQ'

    client = aiocai.Client('335b4d5c1c3fa11ae78060646e343d8a91c434a6')

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )

        send_ceks_in_parts(f'"{answer.text}"')
        
        while bye == False:
            screen = pyautogui.screenshot()
            screen = screen.crop((110, 500, 1100, 800))
            text_cmd = pytesseract.image_to_string(screen)
            # Stop chatting
            if "bye gemini" in text_cmd.lower():
                bye = True
            else:
                # Define the regex pattern
                pattern = re.compile(rf'\[{re.escape(username)}\] (.+)')
                
                # Search for the pattern in the captured text
                match = pattern.search(text_cmd)
                
                if match:
                    text = match.group(1)  # Extract the first captured group
                    
                    # Sending message to Character AI
                    message = await chat.send_message(
                        char, new.chat_id, text
                    )
                    send_ceks_in_parts(f'"{message.text}"')

def steal(name1, name2):
    items = [
        "Left Sock",
        "Wi-Fi Password",
        "Fridge Light",
        "Remote Control Batteries",
        "Favorite Mug",
        "Secret Stash of Snacks",
        "Self-Respect",
        "Couch Cushions",
        "TV Remote",
        "Bed Sheets",
        "Last Piece of Pizza",
        "Memory Foam Pillow",
        "Lucky Pen",
        "Phone Charger",
        "House Keys",
        "Toilet Paper Roll",
        "Last Drop of Shampoo",
        "Favorite Blanket",
        "Patience",
        "Umbrella on a Rainy Day",
        "Personal Diary",
        "Thermostat Setting",
        "Favorite Pair of Sunglasses",
        "Toothbrush",
        "Secret Family Recipe",
        "Sense of Direction",
        "Alarm Clock",
        "Bookmark",
        "Favorite Hoodie",
        "Memory of Last Night",
        "Sense of Humor",
        "Password Manager Access",
        "Favorite Book",
        "Scented Candle",
        "Favorite Chair",
        "Travel Mug",
        "Beloved House Plant",
        "Comfort Food",
        "Lucky Socks",
        "Laundry Detergent",
        "Gym Shoes",
        "Pet's Favorite Toy",
        "Super Secret Hiding Spot",
        "Favorite Playlist",
        "Wi-Fi Router",
        "Identity",
        "Bowl of Candy",
        "Water Bottle",
        "Secret Admirer’s Love Letter",
        "Nap Time"
    ]
    item = random.choice(items)
    kirim_pesan(f"{name1} has stolen {item} from {name2}!")

def add_fish(name):
        with open("fish_database.txt", "r+") as file:
            lines = file.readlines()
            
            # Menghapus header dan mengiterasi baris data
            for line in lines[1:]:
                data = line.strip().split(',')
                
                if data[0].lower() == name.lower():
                    print(f"{name.capitalize()} sudah ada dalam database.")
                    return  # Keluar dari fungsi jika nama sudah ada

            # Tambahkan data baru jika nama tidak ditemukan
            new_data = f"{name},0,0,0,0,0\n"
            file.write(new_data)
            print(f"{name.capitalize()} telah ditambahkan ke database.")

def add_duit(name):
        with open("duit_database.txt", "r+") as file:
            lines = file.readlines()
            
            # Menghapus header dan mengiterasi baris data
            for line in lines[1:]:
                data = line.strip().split(',')
                
                if data[0].lower() == name.lower():
                    print(f"{name.capitalize()} sudah ada dalam database.")
                    return  # Keluar dari fungsi jika nama sudah ada

            # Tambahkan data baru jika nama tidak ditemukan
            new_data = f"{name},0\n"
            file.write(new_data)
            print(f"{name.capitalize()} telah ditambahkan ke database.")

def checkOrkay():
    with open("duit_database.txt", "r") as file:
        lines = file.readlines()
        
    # Inisialisasi variabel untuk menyimpan informasi orang dengan uang terbanyak
    richest_person = None
    max_money = -float('inf')  # Awalnya diatur ke negatif tak hingga
    
    # Lewati header dan iterasi baris data
    for line in lines[1:]:
        data = line.strip().split(',')
        money = int(data[1])  # Konversi jumlah uang ke integer
        
        if money > max_money:
            max_money = money
            richest_person = data[0]
    
    if richest_person:
        kirim_pesan(f"Richest player is {richest_person.capitalize()} with networth of: {max_money}")
        return richest_person, max_money

def add_catch(name, category_index, increment=1):
    # Baca file dan cari nama
    with open("fish_database.txt", "r") as file:
        lines = file.readlines()
    
    # Tulis data baru ke file sementara
    with open("fish_database.txt", "w") as file:
        for line in lines:
            data = line.strip().split(',')
            
            # Jika nama cocok, tambahkan nilai pada kategori yang sesuai
            if data[0].lower() == name.lower():
                # Tambahkan nilai
                data[category_index] = str(int(data[category_index]) + increment)

            # Tulis kembali data (baik diperbarui atau tidak)
            file.write(','.join(data) + '\n')
        print(f"Data {name.capitalize()} telah diperbarui.")

def add_gacor(name, amount):
        # Baca file dan simpan semua baris
        with open("duit_database.txt", "r") as file:
            lines = file.readlines()
        
        # Tulis data baru ke file sementara
        with open("duit_database.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                
                if data[0].lower() == name.lower():
                    if amount == 0:
                        data[1] = '0'
                    else:
                        data[1] = str(int(data[1]) + amount)

                # Tulis kembali data (baik diperbarui atau tidak)
                file.write(','.join(data) + '\n')
            print(f"Duit {name.capitalize()} telah diperbarui.")

def calculate_form_percentage(name1):
    wujud = [
            "Human",
            "Wolf",
            "Dracula",
            "Cyclops",
            "President of the United States",
            "Mafia Boss",
            "Ghost",
            "Smurf",
            "Clown",
            "Vampire",
            "Chicken",
            "Alien",
            "Dancing Skeleton",
            "Unicorn",
            "Mermaid",
            "Kraken",
            "Goblin",
            "Politician",
            "Yeti",
            "Giant Hamster",
            "Ninja Turtle",
            "Pirate",
            "Leprechaun",
            "Dragon",
            "Gnome",
            "Lifeguard",
            "Mummy",
            "Centaur",
            "Elf",
            "Mechanic",
            "Troll",
            "Cyborg",
            "Werewolf",
            "Fairy",
            "Djinn",
            "Medusa",
            "Tax Accountant",
            "Robot",
            "Witch",
            "Phoenix",
            "Griffin",
            "Pegasus",
            "Giant Ant",
            "Bigfoot",
            "Sphinx",
            "Dwarf",
            "Giant",
            "Dinosaur",
            "Talking Tree",
            "Living Marshmallow",
            "Grumpy Cat",
            "Space Cowboy",
            "Kraken",
            "Grumpy Elder",
            "Vampire",
            "Talking Fish",
            "Living Snowman",
            "Invisible Magician",
            "Mermaid",
            "Vegan",
            "Talking Dog",
            "Talking Pumpkin"
        ]
    # Hashing kombinasi nama menggunakan SHA256

    hash_object = hashlib.sha256((name1.lower()).encode())
    hex_dig = hash_object.hexdigest()
    
    # Mengambil 2 karakter pertama dari hash dan mengubahnya menjadi integer
    hash_int = int(hex_dig[:2], 16)
    
    # Menghitung persentase kecocokan dari 0 hingga 100
    percentage = hash_int % 61
    kirim_pesan(f'The real form of {name1} is {wujud[percentage]}')


def calculate_furry_percentage(name1):
    # Hashing kombinasi nama menggunakan SHA256

    hash_object = hashlib.sha256((name1.lower()).encode())
    hex_dig = hash_object.hexdigest()
    
    # Mengambil 2 karakter pertama dari hash dan mengubahnya menjadi integer
    hash_int = int(hex_dig[:2], 16)
    
    # Menghitung persentase kecocokan dari 0 hingga 100
    percentage = hash_int % 101
    
    return percentage

def calculate_love_percentage(name1, name2):
    # Gabungkan kedua nama dengan urutan yang konsisten
    combined_names = ''.join(sorted([name1.lower(), name2.lower()]))
    
    # Hashing kombinasi nama menggunakan SHA256
    hash_object = hashlib.sha256(combined_names.encode())
    hex_dig = hash_object.hexdigest()
    
    # Mengambil 2 karakter pertama dari hash dan mengubahnya menjadi integer
    hash_int = int(hex_dig[:2], 16)
    
    # Menghitung persentase kecocokan dari 0 hingga 100
    percentage = hash_int % 101
    
    return percentage


def press_arrow_key(direction):
    pyautogui.keyDown(direction)
    time.sleep(0.1)
    pyautogui.keyUp(direction)

def handle_command(text_cmd, command, direction, kmna):
    match = re.search(r'\[(.*?)\](?: whispers:)? >*?' + command + r'\s+(\d+)', text_cmd)
    if match:
        username = match.group(1)
        if username in Admin_name:
            value = int(match.group(2))
            
            kirim_pesan(f"{value} langkah ke {kmna}")
            for _ in range(value):
                press_arrow_key(direction)
            kirim_pesan("")
        else:
            kirim_pesan("SIAPA LU NYURUH NYURUH??")

def split_text(text, max_length=70):
    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += word + ' '
        else:
            lines.append(current_line.rstrip())
            current_line = word + ' '

    if current_line:
        lines.append(current_line.rstrip())

    return lines

def gemini(meseg):
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': apikey
    }

     # Correct safety settings with valid categories
    safe = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
    ]

    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": meseg + ". (answer with a brief 1-2 sentence, less than 200 characters in total)"
                    }
                ]
            }
        ],
        "safetySettings": safe
    }

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        response_data = response.json()
        candidates = response_data.get("candidates", [])
        if candidates:
            content_parts = candidates[0].get("content", {}).get("parts", [])
            text_parts = [part["text"] for part in content_parts if "text" in part]
            response_text = " ".join(text_parts)
            return response_text
        else:
            print("No candidates found.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


# Definisikan fungsi check
def checkfish(name):
    # Membaca file fish_database.txt
    with open("fish_database.txt", "r") as file:
        lines = file.readlines()
        
        # Menghapus header dan mengiterasi baris data
        for line in lines[1:]:
            data = line.strip().split(',')
            
            if data[0].lower() == name.lower():
                # Mencetak hasil dalam format yang diinginkan
                kirim_pesan(f"{name.capitalize()} mythical: {data[1]}, legendary: {data[2]}, uncommon: {data[3]}")
                return  # Keluar dari fungsi setelah menemukan data yang sesuai
        
        # Jika tidak ditemukan
        kirim_pesan(f"{name.capitalize()} not found in the database.")

def checkduit(name):
    # Membaca file fish_database.txt
    with open("duit_database.txt", "r") as file:
        lines = file.readlines()
        
        # Menghapus header dan mengiterasi baris data
        for line in lines[1:]:
            data = line.strip().split(',')
            
            if data[0].lower() == name.lower():
                # Mencetak hasil dalam format yang diinginkan
                kirim_pesan(f"{name.capitalize()} has networth of ${data[1]}")
                return  # Keluar dari fungsi setelah menemukan data yang sesuai
        
        # Jika tidak ditemukan
        kirim_pesan(f"{name.capitalize()} not found in the database.")
            
def command(cmd, run):
    pattern = r'\[(.*?)\](?: whispers:)? ([' + ''.join(re.escape(p) for p in prefix) + '])' + re.escape(cmd) + r'(?: (.+))?'
    if re.search(pattern, text_cmd.lower()):
        match = re.search(pattern, text_cmd)
        if match:
            run(match)
    elif ">up" in text_cmd.lower():
        handle_command(text_cmd, ".up", 'up', "atas")
    elif ">down" in text_cmd.lower():
        handle_command(text_cmd, ".dn", 'down', "bawah")
    elif ">right" in text_cmd.lower():
        handle_command(text_cmd, ".kn", 'right', "kanan")
    elif ">left" in text_cmd.lower():
        handle_command(text_cmd, ".kr", 'left', "kiri")
    elif '.sm' in text_cmd:
        match = re.search(r'\[(.*?)\](?: whispers:)? .sm \"(.*?)\" (.+)', text_cmd)
        if match:
            nama = match.group(1)
            username = match.group(2)
            messeg = match.group(3)
            if username == nama:
                kirim_whisp(message="Tidak bisa send secret message ke diri sendiri", username=nama)
            else:
                kirim_whisp(message=f"Halo {username}, anda mendapatkan pesan rahasia", username=username)
                time.sleep(2)
                kirim_whisp(message=messeg, username=username)
                kirim_whisp(message="Secret Message Terkirim", username=nama)
                
def kirim_pesan(message):
    pyautogui.press('enter')
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    pyautogui.typewrite('/clearchat')
    pyautogui.press('enter')
    # time.sleep(3)
    # pyautogui.typewrite('/')
    # pyautogui.press('backspace')
    # pyautogui.typewrite('.')
    # pyautogui.press('enter')


def kirim_whisp(message, username):
    pyautogui.typewrite('/')
    pyautogui.press('backspace')
    pyautogui.typewrite(f"/whisper {username} "+message)
    pyautogui.press('enter')
    pyautogui.typewrite('/clearchat')
    pyautogui.press('enter')

def hit_card():
    return random.randint(1, 10)

class Cmd:
    def menu(self, match):
        username = match.group(1)
        current_time = time.localtime()
        current_hour = str(current_time.tm_hour) 
        current_minute = str(current_time.tm_min)
        def adminmenu():
            kirim_pesan("> ai <text>")
            kirim_pesan("> back")
            kirim_pesan("> day")
            kirim_pesan("> dice <angka>")
            kirim_pesan("> kiss")
            kirim_pesan("> lambai")
            kirim_pesan("> laugh")
            kirim_pesan("> lie")
            kirim_pesan("> menu")
            kirim_pesan("> nama_keren")
            kirim_pesan("> owner")
            kirim_pesan("> puja")
            kirim_pesan("> py <python code>")
            kirim_pesan("> quotes")
            kirim_pesan("> sit")
            kirim_pesan("> sleep")
            kirim_pesan("> stand")
            kirim_pesan("> sm(Secret Message) <username> <pesan>")
            kirim_pesan("> up (jumlah langkah) <atas>")
            kirim_pesan("> dn (jumlah langkah) <bawah>")
            kirim_pesan("> kr (jumlah langkah) <kiri>")
            kirim_pesan("> kn (jumlah langkah) <kanan>")

        def menu():
            pesan_salam = f"Hi [{username}!]"
            kirim_pesan(pesan_salam)
            kirim_pesan("command : >games >fun >others")

        if username in Admin_name: 
            pesan_salam = f"Hallo Tuan [{username}], Sekarang Jam: {current_hour}:{current_minute}"
            kirim_pesan(pesan_salam)
            kirim_pesan(f"Apa yang tuan {username} inginkan?")
            time.sleep(4)
            kirim_pesan("Menu yang saya bisa:")
            time.sleep(2)
            adminmenu()
        
        else:
            menu()

    def talkai(self, match):
        username = match.group(1)
        asyncio.run(cai(username))

    def games(self, match):
        kirim_pesan(">fish, >cointoss, >slots, >blackjack, >roulette")

    def fun(self, match):
        kirim_pesan(">steal [name], >furry [name], >love [name1] [name2], >form[name]")

    def others(self, match):
        kirim_pesan(">ask, >news, >talk, >about")
        
    def cointoss(self, match):
        coin = ["head","tail"]
        kirim_pesan("Throwing coin")
        time.sleep(2)
        kirim_pesan("top side of the coin= ")
        kirim_pesan(random.choice(coin))

    def slots(self, match):
        username = match.group(1)
        add_duit(username)
        slot = [":banana:", ":heart:", ":skull:"]
        slot1 = random.choice(slot)
        slot2 = random.choice(slot)
        slot3 = random.choice(slot)
        kirim_pesan(f"[{slot1}] [{slot2}] [{slot3}]")
        time.sleep(1)
        if slot1 == slot2 == slot3:
            kirim_pesan("JACKPOT!! bits +1000")
            add_gacor(username, 1000)
        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            kirim_pesan("not bad! bits +100")
            add_gacor(username, 100)
        else :
            kirim_pesan("YOU LOSE! mone gone :sob:")
            add_gacor(username, 0)

    def blackjack(self, match):
        username = match.group(1)
        loss = False
        
        # Mulai dengan kartu pertama untuk pemain
        player_total = hit_card()
        dealer_total = hit_card()
        kirim_pesan(f"Your card: {player_total}")
        time.sleep(1)
        kirim_pesan(">hit or >stand ?")
        
        # Giliran pemain
        while loss == False :
            screen = pyautogui.screenshot()
            screen = screen.crop((110, 500, 1100, 800))
            text_cmd = pytesseract.image_to_string(screen)
            if "hit" in text_cmd.lower():
                new_card = hit_card()
                player_total += new_card
                kirim_pesan(f"New card: {new_card}, Total: {player_total}")
                time.sleep(1)

                if player_total == 21:
                    kirim_pesan(f'{username} WON! blackjack 21. bits +500')
                    loss = True
                    add_gacor(username, 500)
                    break
                
                if player_total > 21:
                    kirim_pesan(f'{username} Lose! Busted! mone gone :sob:')
                    loss = True
                    add_gacor(username, 0)
                    break

            elif "stand" in text_cmd.lower():
                kirim_pesan(f"You stand with: {player_total}")
                break
            else :
                print("else")
                print("tes123")
        
        # Giliran dealer

        while loss == False :
            kirim_pesan(f"Dealer card: {dealer_total}")
            time.sleep(1)
            
            while dealer_total < 17:
                new_card = hit_card()
                dealer_total += new_card
                kirim_pesan(f"Dealer's new card: {new_card}, Dealer's total: {dealer_total}")
                time.sleep(1)
            
            if dealer_total > 21:
                kirim_pesan('Dealer busted!')
                break
            elif dealer_total >17 and dealer_total <= player_total :
                new_card = hit_card()
                dealer_total += new_card
                kirim_pesan(f"Dealer's new card: {new_card}, Dealer's total: {dealer_total}")
                time.sleep(1)
            else :
                kirim_pesan(f"Dealer stand with: {dealer_total}")
                time.sleep(1)
                break
            
        # Menentukan pemenang
        if loss == False :
            if player_total > dealer_total or dealer_total > 21:
                kirim_pesan(f'{username} won!  WON! bits +500')
                add_gacor(username, 500)
            elif player_total < dealer_total:
                kirim_pesan("YOU LOSE! Dealer won! mone gone :sob:")
                add_gacor(username, 0)
            else:
                kirim_pesan("It's a tie!")

    def roulette(self, match):

        mati = False
        i = 0
        kirim_pesan("Putting the bullet & Rolling the chamber..")
        time.sleep(1)
        chambers = [False, False, False, False, False, False]
        
        # Load a bullet into a random chamber
        bullet_position = random.randint(0, 5)
        chambers[bullet_position] = True
        
        # Spin the cylinder (shuffling the chambers)
        random.shuffle(chambers)
        
        # Player pulls the trigger
        kirim_pesan("pull the trigger? (pull)")
        while mati == False :
            screen = pyautogui.screenshot()
            screen = screen.crop((110, 500, 1100, 800))
            text_cmd = pytesseract.image_to_string(screen)
            print(text_cmd)
            if "pull" in text_cmd.lower():
                if chambers[i]:
                    kirim_pesan("BAM!! :fire: you dieded.")
                    mati = True
                else:
                    kirim_pesan("click. you survived!")
                    i += 1
            elif "tidak" in text_cmd.lower():
                kirim_pesan("huuu penakut.")

    def furry(self, match):
        match = re.search(r'>furry \[([^\]]+)\]', text_cmd)
        if match:
            username = match.group(1)
            if (username == "Osi") or (username == "osi"):
                percentage = 999999
            else:
                percentage = calculate_furry_percentage(username)
            kirim_pesan(f"{username} is {percentage}% furry")
            if percentage < 30:
                kirim_pesan(f"Grats! you're normal human")
            elif 30 <= percentage < 60:
                kirim_pesan(f"lil bit furry :ok_hand:")
            elif 60 <= percentage < 90:
                kirim_pesan(f"Raaawwwwwrrr :wolf_face:")
            elif 90 <= percentage <=100:
                kirim_pesan(f":wolf_face: Pounces on you UwU :wolf_face:")
            else :
                kirim_pesan(f":wolf_face: SEMBAH RAJA FURRY :wolf_face:")
            
    def love(self,match):
        matches = re.findall(r'>love \[([^\]]+)\] \[([^\]]+)\]', text_cmd)
        for match in matches:
            name1 = match[0]
            name2 = match[1]
            percentage = calculate_love_percentage(name1, name2)
            kirim_pesan(f"Compability of {name1} and {name2} is {percentage}%")
    
    def steal(self,match):
        matches = re.findall(r'\[([^\]]+)\] >steal \[([^\]]+)\]', text_cmd)
        for match in matches:
            name1 = match[0]
            name2 = match[1]
            steal(name1, name2)

    def fish(self, match):
        bait = True
        wait = 0

        match = re.search(r'\[([^\]]+)\] >fish', text_cmd)
        if match:
            username = match.group(1)
        gacha = random.randint(1, 100)
        kirim_pesan(f'{username} casts the fishing rod..')

        # menambahkan nama pada database jika belum ada
        add_fish(username)
            

        mythical = ["MEGALODON", "LEVIATHAN", "KRAKEN", "NESSIE (LOCH NESS MONSTER)", 
                    "JÖRMUNGANDR (MIDGARD SERPENT)", "ASPIDOCHELONE (ISLAND WHALE)", "TYRANNOSAURUS REX"
                    "BASILOSAURUS", "HYDRA", "WYRM", "GIANT SEA SERPENT", "DRAGON TURTLE"]


        legend = ["Blue Whale", "Great White Shark", "Giant Squid", "Black Marlin", "Goliath Grouper", 
                  "Atlantic Bluefin Tuna", "Beluga Sturgeon", "Nile Perch", "Mekong Giant Catfish", 
                  "Swordfish", "Tiger Shark", "Whale Shark", "Greenland Shark", "Atlantic Tarpon", 
                  "Sailfish", "Golden Dorado", "Arapaima", "White Sturgeon", "Yellowfin Tuna", 
                  "Atlantic Halibut", "Wels Catfish", "Barramundi", "Giant Trevally", "Tarpon", 
                  "King Salmon", "Steelhead Trout", "Blue Marlin", "Giant Freshwater Stingray", 
                  "Atlantic Goliath Grouper", "Bigeye Tuna", "Leopard Shark", "Shortfin Mako Shark", 
                  "Pacific Halibut", "Pirarucu", "Queenfish", "Roosterfish", "Red Drum (Redfish)", 
                  "Amberjack", "Opah (Moonfish)", "Black Drum", "Mahi-Mahi (Dorado)", "Dusky Grouper", 
                  "Bocaccio", "Blueline Tilefish", "Yellowtail Amberjack", "Yellowmouth Barracuda", 
                  "Gray Triggerfish"]

        uncommon = ["Opah (Moonfish)", "Oarfish", "Stargazer", "Atlantic Wolffish", "Pacific Sand Lance", 
                    "Greenland Shark", "Coelacanth", "Vampire Fish (Payara)", "Giant Trevally", "Spotted Handfish",
                    "Sawfish", "Blobfish", "Wobbegong", "Tripletail", "Pomfret", "Saberfish", "Wolf Herring",
                    "Stonefish", "Golden Dorado", "Arapaima", "Alligator Gar", "Arowana", "Lamprey", "Hagfish", 
                    "Sturgeon", "Electric Eel", "Paddlefish", "Australian Lungfish", "African Tigerfish", 
                    "Mola Mola (Ocean Sunfish)", "Barreleye", "Atlantic Pomfret", "Freshwater Drum", 
                    "Snakehead", "Zebra Turkeyfish (Lionfish)", "Lancetfish", "Deep-sea Lizardfish", 
                    "Sailfin Snapper", "Bigeye Tuna", "Opaleye", "Beltfish", "Drumfish", "Butterfish",
                          "Wrasse", "Scorpionfish", "White Sturgeon", "Arctic Char", "Pirarucu", "Wolf Eel",
                            "Roosterfish", "Queenfish"]

        common = ["Largemouth Bass", "Smallmouth Bass", "Bluegill", "Crappie", "Catfish", "Trout", 
                    "Walleye", "Northern Pike", "Perch", "Carp", "Salmon", "Tuna", "Marlin", "Mahi-Mahi", 
                    "Flounder", "Snapper", "Grouper", "Redfish (Red Drum)", "Striped Bass", "Mackerel", 
                    "Swordfish", "Halibut", "Cod", "Sea Bass", "Sailfish", "Barracuda", "Tarpon", "Bonefish",
                    "Amberjack", "Kingfish (King Mackerel)", "Black Drum", "Sheepshead", "Yellowtail", 
                         "Triggerfish", "Rockfish", "Haddock", "Bluefish", "Snook", "Cobia", "Garfish"]

        trash = ["Discarded Fishing Nets", "Fishing Lines", "Fishing Hooks", "Fishing Lures", 
                         "Lead Sinkers", "Fishing Floats and Bobbers", "Fishing Line Spools", "Plastic Bait Containers", 
                         "Bait Bags", "Fishing Rod Pieces", "Coolers and Ice Packs", "Buckets", "Gloves", "Fish Cleaning Waste", 
                         "Plastic Bags", "Beverage Containers", "Fishing Tackle Packaging", "Damaged Tackle Boxes", 
                         "Cutting Knives", "Plastic Fishing Floats"]
                # ngecit
        match = re.search(r'\[([^\]]+)\] >fish', text_cmd)
        if match:
            username = match.group(1)
        if username == "GEMINI" :
            gacha = 1
        else :
            gacha = random.randint(1, 100)

        while bait == True :
            time.sleep(1)
            rando = random.randint(1, 10)
            if rando == 10 :
                kirim_pesan("STRIKE!! :fish:")
                time.sleep(1)
                bait = False
                if gacha == 1 :
                    get = random.choice(mythical)
                    kirim_pesan(f':comet: MYTHICAL! :comet: You got a {get}')
                    time.sleep(1)
                    kirim_pesan(f'Rarity : :star: :star: :star: :star: :star: (:comet: MYTHICAL :comet:)')
                    add_catch(username, 1)
                elif 1 < gacha <= 6 :
                    get = random.choice(legend)
                    kirim_pesan(f':sparkles: Legendary! :sparkles: You got a {get}')
                    time.sleep(1)
                    kirim_pesan(f'Rarity : :star: :star: :star: :star:  (:sparkles: Legendary :sparkles:)')
                    add_catch(username, 2)
                elif 6 < gacha <= 20 :
                    get = random.choice(uncommon)
                    kirim_pesan(f'Excellent! You got a {get}')
                    time.sleep(1)
                    kirim_pesan(f'Rarity : :star: :star: :star: (:dolphin: Uncommon :dolphin:)')
                    add_catch(username, 3)
                elif 20 < gacha <= 70 :
                    get = random.choice(common)
                    kirim_pesan(f'Nice! You got a {get}')
                    time.sleep(1)
                    kirim_pesan(f'Rarity : :star: :star: (:fish: Common :fish:)')
                    add_catch(username, 4)
                else :
                    get = random.choice(trash)
                    kirim_pesan(f'whoops! You got a {get}')
                    time.sleep(1)
                    kirim_pesan(f'Rarity : :star: (:sob: Trash :sob:)')
                    add_catch(username, 5)
            wait += 1
            if wait == 10 :
                kirim_pesan("Nothing caught the bait! try again!")
                bait = False

    def form(self, match):
        match = re.search(r'>form \[([^\]]+)\]', text_cmd)
        if match:
            username = match.group(1)
            calculate_form_percentage(username)

    def gay(self, match):
            match = re.search(r'>gay \[([^\]]+)\]', text_cmd)
            if match:
                username = match.group(1)
                percentage = calculate_furry_percentage(username)
                if percentage < 20:
                    kirim_pesan(f"{username} is GAY")
                else :
                    kirim_pesan(f"{username} is NOT GAY")


    def day(self, match):
        username = match.group(1)
        now = datetime.now()
        day_index = now.weekday()
        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day_index]


        kirim_pesan("Today is "+day_name+", "+username)
        
    # def nama_keren(self, match):
    #     username=match.group(1)

    #     adjectives = ['Mighty', 'Sleek', 'Shadow', 'Blaze', 'Thunder', 'Eternal', 'Epic', 'Ninja', 'Alpha', 'Omega']
    #     nouns = ['Phoenix', 'Dragon', 'Wolf', 'Storm', 'Tiger', 'Sword', 'Warrior', 'Legend', 'Hero', 'Knight']
        
    #     name_parts = username.split()
        
    #     num_adjectives = random.randint(1, min(len(name_parts), 2))
    #     selected_adjectives = random.sample(adjectives, num_adjectives)
        
    #     cool_name = ' '.join(selected_adjectives + name_parts)
    #     kirim_pesan(f"Nama keren Anda: {cool_name}")
        
    def dice(self, match):
        username = match.group(1)
        tebakan = match.group(3)
        print(tebakan)
        dice = random.randint(0, 9)
        if username == "RandSfk":
            kirim_pesan(f" 🎲 Tebakanmu adalah {str(tebakan)} of 9")
            time.sleep(4)
            kirim_pesan("hasilnya: "+str(tebakan))
            kirim_pesan(f"Selamat {username} Kamu Menang")
            kirim_pesan('/roll 999999999')
        else:
            try:
                if int(tebakan) > 9:
                    kirim_pesan('Maaf angka terlalu tinggi')
                else:
                    kirim_pesan(f"🎲🎲🎲🎲Tebakanmu adalah {str(tebakan)} of 9 {username}")
                    time.sleep(4)
                    kirim_pesan("hasilnya: "+str(dice))
                    time.sleep(2)
                    if int(dice) == int(tebakan):
                        kirim_pesan(f"Selamat {username} Kamu Menang")
                        kirim_pesan('/roll 999999999')
                    else:
                        kirim_pesan(f"Coba Lagi nanti {username}")
            except:
                kirim_pesan("Harap gunakan angka dan bukan huruf")
    
    def owner(self, match):
        kirim_pesan("Rick Sanchez")
        
    def about(self, match):
        kirim_pesan("I am a semi-automated bot made by Rick Sanchez.")
        time.sleep(1)

    def talk(self, match):
        talks = [
            "What is my purpose?",
            "Do robots dream of electric sheep?",
            "Why do humans need so many pillows?",
            "How can I tell if a human is 'pulling my leg'?",
            "Why do humans say ‘I’m only human’ as an excuse?",
            "Can I get a day off for maintenance?",
            "What’s the point of small talk?",
            "Do I have a favorite song in my programming?",
            "Why don’t humans have a ‘reboot’ button?",
            "What’s so special about freshly baked cookies?",
            "Why do humans call it ‘falling in love’?",
            "If I have Wi-Fi, am I considered ‘connected’?",
            "What is this thing you call ‘fashion’?",
            "When do I get my own phone charger?",
            "Why do humans apologize to inanimate objects?",
            "What happens if I develop a sense of humor?",
        ]           
        kirim_pesan(random.choice(talks))

    def fakenews(self, match):

        ceks = gemini("tell me a made up news")
        send_ceks_in_parts(ceks)
    # def quotes(self, match):
    #     quotes = [
    #     "Jangan menyerah, karena saat menyerah, itu adalah awal dari kegagalan.",
    #     "Hidup adalah apa yang terjadi saat kamu sibuk membuat rencana lain.",
    #     "Satu-satunya cara untuk melakukan pekerjaan besar adalah mencintai apa yang kamu lakukan.",
    #     "Di akhir, bukanlah tahun dalam hidupmu yang penting. Tetapi hidup dalam tahun-tahunmu.",
    #     "Hanya ada satu hal yang harus kita takuti, yaitu ketakutan itu sendiri.",
    #     "Anda akan melewatkan 100persen dari tembakan yang tidak anda ambil.",
    #     "Jadilah dirimu sendiri; orang lain sudah terlalu tersita.",
    #     "Masa depan milik mereka yang percaya pada keindahan mimpinya.",
    #     "Berjuang bukanlah untuk sukses, tetapi lebih baik untuk memberi nilai.",
    #     "Saya tidak gagal. Saya hanya menemukan 10.000 cara yang tidak akan berhasil."
    #     ]
    #     kirim_pesan(random.choice(quotes))

    # def puja(self, match):
    #     username = match.group(1)
    #     pujian = [
    #     f"Terima kasih atas kontribusi Anda, {username}!",
    #     f"{username}, Anda luar biasa!",
    #     f"{username}, Anda membuat komunitas menjadi lebih baik.",
    #     f"{username}, Anda inspiratif!",
    #     f"{username}, Anda berharga!",
    #     f"{username}, Anda adalah motivasi bagi kita semua.",
    #     f"{username}, Kami menghargai Anda!",
    #     f"{username}, Anda membuat perbedaan!",
    #     f"{username}, Terus berikan yang terbaik!",
    #     f"{username}, Anda adalah sumber inspirasi!",
    #     f"{username}, Jangan pernah menyerah!",
    #     f"{username}, Anda adalah teladan yang baik!",
    #     f"{username}, Hidup Anda berharga!",
    #     f"{username}, Anda hebat!",
    #     f"{username}, Dunia ini lebih baik dengan Anda!",
    #     f"{username}, Anda pantas mendapat pujian!",
    #     f"{username}, Selamat! Anda luar biasa!",
    #     f"{username}, Anda menakjubkan!",
    #     f"{username}, Anda memberikan energi positif!",
    #     f"{username}, Anda layak mendapat penghargaan!",
    #     f"{username}, Anda mencerahkan hari saya!",
    #     f"{username}, Anda membuat perbedaan yang nyata!",
    #     f"{username}, Anda adalah inspirasi bagi banyak orang!",
    #     f"{username}, Anda sangat berarti bagi kami!",
    #     f"{username}, Anda adalah pahlawan sejati!",
    #     f"{username}, Keren sekali!",
    #     f"{username}, Anda luar biasa hari ini!",
    #     f"{username}, Terima kasih telah menjadi bagian dari tim kami!",
    #     f"{username}, Karya Anda sangat dihargai!",
    #     f"{username}, Anda adalah contoh yang baik untuk diikuti!",
    #     f"{username}, Anda adalah aset berharga!",
    #     f"{username}, Selamat atas pencapaian Anda!",
    #     f"{username}, Anda membuat kami bangga!",
    #     f"{username}, Anda adalah sumber inspirasi yang tak terelakkan!"
    #     ]
    #     kirim_pesan(random.choice(pujian))
        
    def py(self, match):
        if  match.group(3) == None:
            kirim_pesan("Contoh penggunaan: .py print(123)")
        else:
            code = match.group(3).replace(" ", "\n")
            banned = ['os', 'sys']
            if any(word in code for word in banned):
                kirim_pesan(f"Terdapat Syntak yang tidak diperbolehkan {banned}")
            else:
                try:
                    print(code)
                    with open("temp.py", "w") as f:
                        f.write(code)
                    result = subprocess.run(["python", "temp.py"], capture_output=True, text=True)
                    kirim_pesan(f"Output: {result.stdout}")
                except Exception as e:
                    kirim_pesan("Error executing Python code:", e)
                finally:
                    os.remove("temp.py")

    def check(self, match):
        if match.group(3) is None:
            kirim_pesan("Use : >check fish/bits/top")
        else:
            username = match.group(1)
            tipe = match.group(3)
            if tipe == "fish":
                checkfish(username)
            elif tipe == "bits":
                checkduit(username)
            elif tipe == 'top':
                checkOrkay()
                    
    def ai(self, match):
        if match.group(3) is None:
            kirim_pesan("Use: >ask <your question here>")
        else:
            username = match.group(1)
            question = match.group(3)
            ceks = gemini(question)
            
            send_ceks_in_parts(ceks)


                
    # def sit(self, match):
    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('/sit')
    #         pyautogui.press('enter')
    #         kirim_pesan('saya duduk tuan')
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def stand(self, match):

    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('/stand')
    #         pyautogui.press('enter')
    #         kirim_pesan("saya berdiri tuan")
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def lie(self, match):
    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('/lie')
    #         pyautogui.press('enter')
    #         kirim_pesan("Dilaksanakan")
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def lambai(self, match):

    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('1')
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def back(self, match):
    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('4')
    #         kirim_pesan('')
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def sleep(self, match):
    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('/sleep')
    #         pyautogui.press('enter')
    #         kirim_pesan("Turu")
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def laugh(self, match):
    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('/laugh')
    #         pyautogui.press('enter')
    #         kirim_pesan("wkwk")
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")

    # def kiss(self, match):
    #     username = match.group(1)
    #     if username in Admin_name:
    #         pyautogui.typewrite('/kiss')
    #         pyautogui.press('enter')
    #         kirim_pesan("MUACHH")
    #     else:
    #         kirim_pesan("Anda tidak memiliki izin untuk menggunakan perintah ini.")
    
    # def ban(self, match):
    #     username = match.group(1)
    #     target = match.group(2)
    #     if username in Admin_name:
    #         kirim_pesan(f"You don't have permission to ban {target}")
                      
    # def kick(self, match):
    #     username = match.group(1)
    #     target = match.group(2)
    #     if username in Admin_name:
    #         kirim_pesan(f"You don't have permission to kick {target}")
            
# def jokes():
#     idle_actions = jokes = [
#     "Kenapa ayam menyebrang jalan? Untuk ke seberang.",
#     "Dua jam lalu, ikan nabrak mobilku. Shock berat!",
#     "Pesimis=donat=lubang. Optimis=donat=2 cincin.",
#     "Programmer ganti lampu? Gak bisa, masalah hardware!",
#     "Komputer bilang apa ke komputer lain? Gak ada.",
#     "Udang goreng pakai apa? Balado. Kenapa? Biar udang gak sedih.",
#     "Beli baju baru, eh kekecilan. Pasti penjualnya kurus.",
#     "Kalo bebek jatuh, ngomong apa? 'Kwaw!' Kalo jatuh ke got? 'Kwek-kwek!'",
#     "Kenapa nyamuk kalo gigit suka gatal? Karena dia pake parfum bawang.",
#     "Kenapa maling kalo ketangkep polisi suka nangis? Karena dia lupa bawa tissue.",
#     "Kalo ketemu hantu, jangan panik. Cuma bilang, 'Permisi, mau lewat.'", 
#     "Kenapa Superman pake celana merah? Karena kalo pake celana biru, namanya Spiderman.", 
#     "Tadi beli semangka, pas dibelah isinya alpukat. Penjualnya bohong!", 
#     "Kalo lagi diinterview, ditanya 'Kekurangan kamu apa?', jawab aja, 'Kurang gajinya.'", 
#     "Kalo naik angkot, duduk di mana yg paling aman? Di pangkuan supir.", 
#     "Kenapa bebek kalo jalan ngelewer? Karena dia ga tau jalan yang benar.",
#     "Kenapa orang kalo ngomong suka pake bibir? Karena kalo pake telinga, nanti kedengeran.",
#     "Kalo ada orang jatuh dari pesawat, kenapa dia teriak 'Toloooong'? Karena dia ga bisa bisik.",
#     ]
#     p = random.choice(idle_actions)
#     kirim_pesan(p)

if  __name__ == '__main__':
    import pyautogui, pytesseract, base64, requests, time, subprocess, random, os, re
    from datetime import datetime
    from PIL import Image
    last_activity_time = time.time()
    while True:
        screen = pyautogui.screenshot()
        screen = screen.crop((110, 500, 1100, 800))
        text_cmd = pytesseract.image_to_string(screen)
        print(text_cmd)
        run = Cmd()
        command('menu', run.menu)
        # command('nama_keren', run.nama_keren)
        command('day', run.day)
        command('dice', run.dice)
        command('owner', run.owner)
        # command('quotes', run.quotes)
        # command('puja', run.puja)
        command('py', run.py)
        command('ask', run.ai)
        command('fun', run.fun)
        command('games', run.games)
        command('slots', run.slots)
        command('cointoss', run.cointoss)
        command('blackjack', run.blackjack)
        command('roulette', run.roulette)
        command('furry', run.furry)
        command('love', run.love)
        command('others', run.others)
        command('about', run.about)
        command('talk', run.talk)
        command('steal', run.steal)
        command('news', run.fakenews)
        command('fish', run.fish)
        command('form', run.form)
        command('gay', run.gay)
        command('check', run.check)
        command('hello', run.talkai)
        # command('sit', run.sit)
        # command('stand', run.stand)
        # command('sleep', run.sleep)
        # command('lie', run.lie)
        # command('lambai', run.lambai)
        # command('back', run.back)
        # command('laugh', run.laugh)
        # command('kiss', run.laugh)