import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get token from environment variable (NEVER hardcode!)
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"سلام {user.mention_html()}! من یک ربات هستم."
    )

async def help_command(update: Update, context):
    """Send a message when the command /help is issued."""
    await update.message.reply_text("دستورات: /start - شروع")

async def echo(update: Update, context):
    """Echo the user message."""
    await update.message.reply_text(f"شما گفتید: {update.message.text}")

def main():
    """Start the bot."""
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not set!")
        return

    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot with polling
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
