# This is annoyobot
# sends a message every hour to eva and val
# author: vls
# date: 01.02.2020
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def hourlymsg(context: telegram.ext.CallbackContext):
    cid = -337445266 #chat id of "Grace Playground" Group
    now = datetime.now()
    msgtries = 1
    appendedtxt = "time."
    while True:
        datestr = now.strftime('%H:%M:%S on the %d.%m.%Y')
        msgtext = 'The time is ' + datestr
        if msgtries > 250:
            raise Exception("I Give up")
        msgtext += " \nI tried sending this message {} ".format(msgtries)
        msgtext += appendedtxt
        try:
            context.bot.send_message(chat_id=cid, text=msgtext)
            break
        except Exception as e:
            print(e)
            msgtries += 1
            appendedtxt = "times."

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("I don't take commands")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)  

def main():
    try:
        with open('token', 'r') as f:
            token = f.readlines()
    except IOError:
        print("You need the tokenfile!") 

    #start message queu
    updater = Updater(token[0], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    hour_job = dp.job_queue.run_repeating(hourlymsg, interval=3600, first=0)
    hour_job.run(dp)
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
