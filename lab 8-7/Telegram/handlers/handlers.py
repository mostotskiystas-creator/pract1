def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Бот працює! ✅")
