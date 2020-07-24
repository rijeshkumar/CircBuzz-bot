import os
from telegram.ext import Updater, Defaults
from telegram import ParseMode
from addons.utils import logger
from handlers.handlers import msg_handlers


def main():
    logger.warning("ahh waking up...")
    defaults = Defaults(parse_mode=ParseMode.HTML)
    updater = Updater(token = "1325100358:AAHQsZINVSccBo57LH1qn0ahU17ZH0EZdAI" ,use_context=True ,workers=200)
    msg_handlers(updater.dispatcher)
    updater.start_polling()
    logger.warning("Ready to rock...")
    updater.idle()

if __name__ == '__main__':
    main()
