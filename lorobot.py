import logging

from telegram import Update
from telegram.ext import (
    filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
    )

from secret_tokens import SECRET_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='lorobot.log',
    level=logging.INFO
)

secret_token = SECRET_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_chat.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, {}. I'm a bot, please talk to me!".format(user_name)
        )


async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
        )


def main():
    application = ApplicationBuilder().token(secret_token).build()

    start_handler = CommandHandler('start', start)
    talk_to_me_handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND), talk_to_me
        )

    application.add_handler(start_handler)
    application.add_handler(talk_to_me_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
