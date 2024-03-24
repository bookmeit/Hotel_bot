import telebot
import config
import hotel

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Для поиска информации об отеле введите его ID.")

@bot.message_handler(func=lambda message: True)
def search_hotels_handler(message):
    chat_id = message.chat.id
    hotel_id = message.text
    hotel_info = hotel.search_hotels(hotel_id)
    if hotel_info:
        hotel_name, tagline = hotel.parse_hotels_data(hotel_info)
        if hotel_name:
            response_message = f"Название отеля: {hotel_name}\n"
            if tagline:
                response_message += f"Описание: {tagline}"
            bot.send_message(chat_id, response_message)
        else:
            bot.send_message(chat_id, "Информация об отеле не найдена.")
    else:
        bot.send_message(chat_id, "Произошла ошибка при поиске информации об отеле.")

if __name__ == "__main__":
    bot.polling()