from telegram.ext import ApplicationBuilder, MessageHandler, filters
import openai

# Укажите API-ключ OpenAI
openai.api_key = "ВАШ_API_КЛЮЧ"

# Функция обработки сообщений
async def handle_message(update, context):
    user_input = update.message.text
    prompt = f"Баллы абитуриента: {user_input}\n{PROMPT}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        await update.message.reply_text(response['choices'][0]['message']['content'])
    except Exception as e:
        await update.message.reply_text("Произошла ошибка при обработке вашего запроса.")

# Настройка бота
application = ApplicationBuilder().token("ВАШ_TELEGRAM_API_TOKEN").build()

# Добавление обработчика сообщений
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Запуск бота
if __name__ == "__main__":
    application.run_polling()
