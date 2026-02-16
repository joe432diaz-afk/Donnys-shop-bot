import os
import traceback
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

try:
    # Get your BotFather token from Render environment variables
    TOKEN = os.environ["TOKEN"]
    if not TOKEN:
        raise ValueError("TOKEN environment variable is missing!")

    # /start command with welcome message and buttons
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("View Cheat Codes", callback_data="cheat_codes")],
            [InlineKeyboardButton("Contact Donny", callback_data="contact_donny")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "👋 Hi folks! Welcome to Donny's Shop.\n\n"
            "Here for all your spiritual chest cheat codes and healing tools.\n\n"
            "PM @itsDonny1212 for help, or check the price lists and send your crypto "
            "account according to the product price.\n\n"
            "You’ll automatically get a confirmation message once processed.",
            reply_markup=reply_markup
        )

    # Handle button clicks
    async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        
        if query.data == "cheat_codes":
            await query.edit_message_text("🔑 Here are the cheat codes:\n[Insert your cheat codes list]")
        elif query.data == "contact_donny":
            await query.edit_message_text("📩 PM @itsDonny1212 for help!")

    # Build and run the bot
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

except Exception as e:
    print("ERROR:")
    traceback.print_exc()
