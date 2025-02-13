from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler , filters, CallbackContext
import os

TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update:Update,context:CallbackContext):
    await update.message.reply_text("Hello I new bot ")

async def echo (update: Update, context:CallbackContext):
    await update.message.reply_text(update.message.text+"by bot")

def main():
    app=Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.Text , echo))
    print("Bot is running ...............")

    app.run_polling()

if __name__=="__main__":
    main()

