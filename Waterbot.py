import telebot
import datetime
import time
import threading
import random
from telebot import types

bot = telebot.TeleBot("7431422173:AAGqLZyjvcqhkN-2Mla2sm1XUuwleIAZH3A")


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    item2 = types.KeyboardButton("/fact")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Hello! I`m the bot to remeowind you to drink water", reply_markup=markup)
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=["fact"])
def fact_message(message):
    list = ["**Strange Density Behavior**: Unlike most substances, water expands as it freezes. This is why ice floats on liquid water. The molecular structure of ice creates a lattice that occupies more space than liquid water, making it less dense.",
            "**High Surface Tension**: Water has one of the highest surface tensions of any liquid due to its hydrogen bonding. This property allows small insects, like water striders, to walk on the surface of water without sinking.",
            "**Universal Solvent**: Water is often called the universal solvent because it can dissolve more substances than any other liquid. This is due to its polar nature, which allows it to interact with a variety of molecules, making it essential for transporting nutrients and waste in biological organisms.",
            "**Triple Point**: Water is one of the few substances that can exist in all three states of matter (solid, liquid, and gas) within the natural temperature and pressure ranges on Earth. Its 'triple point', where all three states coexist in thermodynamic equilibrium, occurs at 0.01°C and a specific pressure of 611.657 pascals."]
    random_fact = random.choice(list)
    bot.reply_to(message, f"Here it is! The interesting fact about water {random_fact}")


def send_reminders(chat_id):
    first_rem = "10:12"
    second_rem = "14:00"
    end_rem = "23:54"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Reminder: Drink soMeow water!")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)
