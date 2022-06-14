import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


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


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']  # подставьте свой ключ API
    tg_id = os.environ['TG_CHAT_ID']  # подставьте свой ID
    bot = ptbot.Bot(tg_token)
    bot.send_message(tg_id, "Бот запущен")
    bot.send_message(tg_id, "Введите время")
    bot.reply_on_message(reply)
    bot.run_bot()


