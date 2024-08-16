#python-telegram-bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


async def start(update, context):
    await update.message.reply_text('hi')
async def get_text(update, context):
    print(update)
    text = update.message.text
    await update.message.reply_text(text[::-1])

app = ApplicationBuilder().token("7473045798:AAHyEHGVsLAncnXCH4suZ7QkMXbc6HRhEhk").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, get_text))
print('start bot')
app.run_polling()