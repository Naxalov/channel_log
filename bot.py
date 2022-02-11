
import os
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler
    
)
#Define a start handler
def start(update: Update, context: CallbackContext):
   
    update.message.reply_text(

        text='Welcome to the bot!',
    )
   


def main():
    TOKEN = os.environ.get('TOKEN')
     # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

# Run the bot
if __name__ == '__main__':
    main()
