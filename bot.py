from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN ="7848177898:AAFAvOolBxDTleXM63lpPkUMaYYUv-Ei6T4"

# Handle files
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.video or update.message.audio or update.message.photo[-1]
    
    # Get file info
    tg_file = await file.get_file()
    file_path = f"downloads/{file.file_unique_id}"
    
    # Save file locally
    await tg_file.download_to_drive(file_path)
    
    await update.message.reply_text(f"✅ File saved: {file_path}")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Document.ALL | filters.Video.ALL | filters.Audio.ALL | filters.PHOTO, handle_file))
    app.run_polling()

if __name__ == "__main__":
    main()
