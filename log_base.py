from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime as DT
from timetable import columns_b

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('request_base.txt', 'a')
    now = DT.datetime.now(DT.timezone.utc).astimezone()
    time_format = "%Y-%m-%d %H:%M:%S"
    file.write(f"{now:{time_format}};{update.effective_user.id};{update.effective_user.username};{update.message.text};\n")
    file.close()

async def log_group_write(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Flag = True
    f = open('log_group_base.txt', 'r')
    for line in f.readlines():
        if str(update.effective_user.id) in line:
            await update.message.reply_text(f'You have a group!')
            Flag = False
    f.close()

    if str(update.message.text[7:]) not in columns_b and Flag:
        await update.message.reply_text(f'Apparently such a group is not in the database!\nOr you made a mistake when entering...\nPlease restart and follow the template:\n/group НПМбд-01-21')
        Flag = False

    if Flag:
        f = open('log_group_base.txt', 'a')
        f.write(f'{str(update.message.text[7:])};{update.effective_user.id};{update.effective_user.name};\n')
        f.close()
        text = str(update.message.text)
        await update.message.reply_text(f'Your group {text[7:]} was added!\nYou can use /help to learn more...\n')

async def log_group_take(update: Update, context: ContextTypes.DEFAULT_TYPE):
    f = open('log_group_base.txt', 'r')
    for line in f.readlines():
        if str(update.effective_user.id) in line:
            return str(line[:11])

    return '-'

