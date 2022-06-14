import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse

TG_TOKEN = os.environ['TELEGRAM_TOKEN']  # подставьте свой ключ API
TG_ID = os.environ['TG_CHAT_ID']  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)


def reply(chat_id, total_time):
    message_id = bot.send_message(chat_id, "Запуск таймера")
    bot.create_countdown(parse(total_time), notify_progress, chat_id=chat_id, message_id=message_id,
                         total_time=parse(total_time))


def notify_progress(time, chat_id, message_id, total_time):
    bar = render_progressbar(total_time, time)
    bot.update_message(chat_id, message_id, f"Осталось {time} секунд \n{bar}")
    if time == 0:
        bot.send_message(chat_id, "Время вышло!")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 - (100 * (iteration / float(total))))
    filled_length = int(length * (total - iteration) // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    load_dotenv()
    bot.send_message(TG_ID, "Бот запущен")
    bot.send_message(TG_ID, "Введите время")
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == '__main__':
    main()
