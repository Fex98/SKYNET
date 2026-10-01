import os
import telebot
import time

# قراءة توكن البوت من متغيرات البيئة في المنصة (أمنياً أفضل)
TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! بوت مراقبة الميكروتك يعمل بنجاح على مدار الساعة 🚀")

@bot.message_handler(commands=['status'])
def check_status(message):
    # هنا يمكنك لاحقاً إضافة كود فحص الميكروتك
    bot.reply_to(message, "حالة النظام: متصل ويعمل بشكل سليم ✅")

def main():
    print("Bot is starting...")
    # حلقة تكرار لضمان عدم توقف البوت نهائياً في حال حدوث أي انقطاع مؤقت بالاتصال
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(10) # انتظار 10 ثوانٍ قبل إعادة المحاولة

if __name__ == '__main__':
    main()
