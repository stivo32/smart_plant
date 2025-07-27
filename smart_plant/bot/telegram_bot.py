import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Привет! Я SmartPlant бот!")

async def status(update, context):
    await update.message.reply_text("Статус: всё стабильно 🌱")

def run_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    print("🤖 Telegram bot is running...")
    app.run_polling()

