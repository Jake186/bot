from telegram.ext import Updater, MessageHandler, Filters
from telegram import Bot, Update
import pytesseract
from PIL import Image

TOKEN = 'AAFURx-WKUHHHSbP0cbohoANbcgY3gzdzik'

def image_to_text(bot: Bot, update: Update):
    user = update.message.from_user
    photo_file = bot.getFile(update.message.photo[-1].file_id)
    photo_file.download('user_image.jpg')
    
    # OCR processing
    extracted_text = pytesseract.image_to_string(Image.open('user_image.jpg'))
    
    if not extracted_text:
        extracted_text = "Sorry, I couldn't extract any text from the image."
    
    update.message.reply_text(extracted_text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handle images
    dp.add_handler(MessageHandler(Filters.photo, image_to_text))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
