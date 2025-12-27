import os
from telegram.ext import Application, CommandHandler
TOKEN = os.environ.get("BOT_TOKEN")
async def start(update, context):
    await update.message.reply_text("TEST")
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("BOT READY")
    app.run_polling()
if __name__ == "__main__":
    main()
