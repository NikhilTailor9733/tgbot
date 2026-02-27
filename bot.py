from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = update.message.text

        response = requests.post(
            "https://oracle-x6tl.onrender.com/ask",
            json={
                "user_id": str(update.message.chat_id),
                "text": user_text
            },
            timeout=60
        )

        reply = response.json()["reply"]

        await update.message.reply_text(reply)

    except Exception as e:
        print("ERROR:", e)
        await update.message.reply_text("Brain connection failed.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🤖 Telegram Bot Running...")
app.run_polling()