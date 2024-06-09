from PIL import Image
from datetime import datetime
import time, random, re, pyautogui, pytesseract, os, requests, subprocess, rpg, sys, hashlib
###======= Bot Configuration =======###

BotName = "Rick's Bot"
Admin_name = ['I AM RICK']
prefix = ['+', '>', '-']
apikey="AIzaSyDb0-LMWXLjAiZZdKcMsXpkqqxWGXhAu6A"
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


def calculate_furry_percentage(name1):
    # Hashing kombinasi nama menggunakan SHA256
    hash_object = hashlib.sha256(name1.lower().encode())
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
        'x-goog-api-key': apikey}
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": meseg+". (answer with a brief sentence, less than 60 characters)"
                    }
                ]
            }
        ]
    }
    response = requests.post("https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent", headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        candidates = response_data.get("candidates", [])
        if candidates:
            content_parts = candidates[0].get("content", {}).get("parts", [])
            text_parts = [part["text"] for part in content_parts if "text" in part]
            response_text = " ".join(text_parts)
            return(response_text)
        else:
            print("No candidates found.")
            
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
    pyautogui.typewrite('/')
    pyautogui.press('backspace')
    pyautogui.typewrite("/say "+message)
    pyautogui.press('enter')
    pyautogui.typewrite('/clearchat')
    pyautogui.press('enter')

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
            kirim_pesan("I'm an automated bot made by Rick Sanchez")
            kirim_pesan("Available menus:")
            kirim_pesan(">games >fun >others")

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

    def games(self, match):
        kirim_pesan(">cointoss >slots >blackjack >roulette")

    def fun(self, match):
        kirim_pesan(">furry [name], >love [name1] [name2]")

    def others(self, match):
        kirim_pesan(">ask, >owner, >about")
        
    def cointoss(self, match):
        coin = ["head","tail"]
        kirim_pesan("Throwing coin")
        time.sleep(2)
        kirim_pesan("top side of the coin= ")
        kirim_pesan(random.choice(coin))

    def slots(self, match):
        slot = [":banana:", ":heart:", ":skull:"]
        slot1 = random.choice(slot)
        slot2 = random.choice(slot)
        slot3 = random.choice(slot)
        kirim_pesan(f"[{slot1}] [{slot2}] [{slot3}]")
        time.sleep(1)
        if slot1 == slot2 == slot3:
            kirim_pesan("JACKPOT!!")
        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            kirim_pesan("not bad!")
        else :
            kirim_pesan("YOU LOSE!")

    def blackjack(self, match):

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
                    kirim_pesan("You WON! blackjack 21.")
                    loss = True
                    break
                
                if player_total > 21:
                    kirim_pesan("You Lose! Busted!")
                    loss = True
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
                kirim_pesan("You won! Dealer busted!")
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
                kirim_pesan("YOU WON!")
            elif player_total < dealer_total:
                kirim_pesan("YOU LOSE! Dealer won!")
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
    
    def day(self, match):
        username = match.group(1)
        now = datetime.now()
        day_index = now.weekday()
        day_name = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"][day_index]


        kirim_pesan("Sekarang adalah hari "+day_name+" "+username)
        
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
                    
    def ai(self, match):
        if match.group(3) == None:
            kirim_pesan("Use: >ask <your question here>")
        else:
            username = match.group(1)
            question = match.group(3)
            ceks = gemini(question)
            if username in Admin_name:
                if isinstance(ceks, list):
                    for item in ceks:
                        kirim_pesan(item)
                        time.sleep(7)
                elif ceks == None:
                    kirim_pesan("too much request")
                    gemini(question)
                else:
                    kirim_pesan(ceks)
            elif username not in Admin_name:
                kirim_pesan(ceks)
                
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
        # command('day', run.day)
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
        # command('sit', run.sit)
        # command('stand', run.stand)
        # command('sleep', run.sleep)
        # command('lie', run.lie)
        # command('lambai', run.lambai)
        # command('back', run.back)
        # command('laugh', run.laugh)
        # command('kiss', run.laugh)