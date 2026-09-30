# pip install pyTelegramBotAPI 
# types --- turlar
# Keyboard --- keyboard
# button
# types
import telebot 
from telebot import types

TOKEN = "8891749068:AAFe8oFmu_njhRmlDbL7Lm8HJonHa78dC64"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    
    btn1 = types.KeyboardButton("Python")
    btn2 = types.KeyboardButton("Html")
    btn3 = types.KeyboardButton("Css")
    btn4 = types.KeyboardButton("Java")
    btn5 = types.KeyboardButton("Harry Potter")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Texnalogiya Tanlang', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Python":
        bot.send_message(message.chat.id, "Python darslari");
    elif message.text == "Html":
        bot.send_message(message.chat.id, """
                         🌐 HTML haqida qiziqarli ma’lumotlar:

💻 HTML — web-sahifalar yaratish uchun ishlatiladigan belgilash tili.

📌 HTML so‘zi “HyperText Markup Language” degan ma’noni anglatadi.

🧱 HTML yordamida web-sahifaning tuzilishi yaratiladi.

🏷️ HTML teglar orqali ishlaydi:
<h1> — sarlavha
<p> — paragraf
<img> — rasm
<a> — havola
<button> — tugma

🌍 HTML internetdagi deyarli barcha web-sahifalarning asosiy qismlaridan biridir.

🎨 HTML — sahifaning tuzilishini yaratadi,
CSS 🎨 — uning ko‘rinishini bezaydi,
JavaScript ⚡ — sahifaga harakat va funksiyalar qo‘shadi.

🔥 Qiziqarli fakt:
HTML dasturlash tili emas, balki markup (belgilash) tilidir.

🚀 HTML o‘rganish web-dasturlashni boshlash uchun yaxshi qadam!
                         """)
    elif message.text == "Css":
        bot.send_message(message.chat.id, "")
    elif message.text == "Java":
        bot.send_message(message.chat.id, "Java darslari")
    elif message.text == "Harry Potter":
        bot.send_message(message.chat.id, """
                         🧙‍♂️ Garri Potter — J. K. Rowling yaratgan mashhur sehrgar bola. Uning to‘liq ismi Harry James Potter.

⚡ Peshonasidagi chaqmoq izi — Voldemortning la’nati tufayli paydo bo‘lgan.

🦉 Garri 11 yoshida Hogwarts sehrgarlik maktabiga o‘qishga boradi.

🏰 Hogwartsda 4 ta fakultet bor:
🦁 Gryffindor
🐍 Slytherin
🦅 Ravenclaw
🦡 Hufflepuff

👬 Garrining eng yaqin do‘stlari — Ron Weasley va Hermione Granger.

🧹 Garri Quidditch o‘yinida Seeker bo‘lib o‘ynaydi va juda yoshligidan mashhur bo‘ladi.

🐍 Garri parseltongue — ilonlar tilida gapira olish qobiliyatiga ega.

🪄 Uning tayoqchasi 11 dyuym, holly daraxtidan yasalgan va ichida feniks pati bor.

🐈‍⬛ Hogwartsdagi professor McGonagall aslida mushukka aylana oladi! 🐱✨

🦉 Garrining boyqushi Hedwig deb ataladi va unga xatlar yetkazib turadi.

💚 Voldemort — Garrining eng katta dushmani. U Garri orqali mag‘lubiyatga uchraydi.

📚 Garri Potter haqidagi asosiy hikoya 7 ta kitobdan iborat.

🎬 Bu kitoblar asosida 8 ta film suratga olingan.

✨ Eng qiziq fakt: Garri Potter hikoyasining mashhur “9¾-platformasi” Londondagi King’s Cross vokzalidagi haqiqiy joydan ilhomlangan. 🚂🪄
                         """)

@bot.message_handler(commands=['about'])
def about(message):
    
    bot.send_message(message.chat.id, "I am ..... bot")




# kod yozildi yangilandi
bot.infinity_polling()