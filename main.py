from telegram.ext import *
import Constants as keys
import Responses as R

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Hey mate! what\'s up.')


def help_command(update, context):
    update.message.reply_text("""List of commands: 
    
    /start
    /help
    /about
    
If you have any queries other than this then ask @lynnchamaru""")


def about_command(update, context):
    update.message.reply_text('I\'m a chatbot, I won\'t bring any harm to you')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("about", about_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
