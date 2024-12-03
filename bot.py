from telegram.ext import Updater, MessageHandler, Filters
import openai

# Укажите API-ключ OpenAI
openai.api_key = "ВАШ_API_КЛЮЧ"

# Функция обработки сообщений
def handle_message(update, context):
    user_input = update.message.text
    prompt = f"Баллы абитуриента: {user_input}\n{PROMPT}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    update.message.reply_text(response['choices'][0]['message']['content'])

# Настройка бота
updater = Updater("ВАШ_TELEGRAM_API_TOKEN")
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Запуск бота
updater.start_polling()
updater.idle()
updater.start_polling()
