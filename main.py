from telegram import Update
from telegram.ext import *
from dotenv import load_dotenv
import os
import bot_response
load_dotenv()

TOK = os.getenv('DIAMOND_KEBAB')

print('Starting a bot....')

# Commands
async def start_commmand(update, context):
    await update.message.reply_text('Hello! Welcome To Diamond kebab! use / command')

async def help(update, context):
    await update.message.reply_text('You can browse menu using /menu\nknow more buy /want_to_know_more\nYou can order by /want_to_order.\nYou also can text me. :)')


async def Menu(update, context):
    text = "What's on your menu?"
    ans = bot_response.bot_response(text)
    await update.message.reply_text(ans)


async def Want_to_know_more(update, context):
    text = "Want to know more about you"
    ans = bot_response.bot_response(text)
    await update.message.reply_text(ans)

# async def Want_to_buy(update, context):
#     # Extract any parameters after the /want_to_order command
#     # For example, if the user sends "/want_to_order pizza", you can get "pizza"
#     item_to_order = context.args[0] if context.args else None
#
#     text = f"I want to order {item_to_order}"
#     ans = bot_response.bot_response(text)
#     await update.message.reply_text(ans)
async def Want_to_buy(update, context):
    text = "I want to order"
    ans = bot_response.bot_response(text)
    await update.message.reply_text(ans)


# Message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat.id
    user_name = update.message.chat.username

    user_msg = update.message.text
    ans = bot_response.bot_response(user_msg)
    await update.message.reply_text(ans)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update has error {update} the error is {context.error}")

if __name__ == '__main__':
    application = Application.builder().token(TOK).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(CommandHandler('menu', Menu))
    application.add_handler(CommandHandler('want_to_know_more', Want_to_know_more))
    application.add_handler(CommandHandler('want_to_order', Want_to_buy))
    application.add_handler(CommandHandler('help', help))

    # Message
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    # ERRORS
    application.add_error_handler(error)
    # Run bot
    application.run_polling(1.0)