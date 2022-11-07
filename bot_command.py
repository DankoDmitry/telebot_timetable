from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime as DT
from log_base import *
from timetable import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def time_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    now = DT.datetime.now(DT.timezone.utc).astimezone()
    time_format = "%Y-%m-%d %H:%M:%S"
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = week[DT.datetime.today().weekday()]
    await update.message.reply_text(f'Now {now:{time_format}} ({day})')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    comands = '/group\n/lesson\n/lesson_tomorrow\n/hello\n/time\n/help\n'
    await update.message.reply_text(comands)

async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Please enter the command as: \n/group НПМбд-01-21')

async def group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await log_group_write(update, context)

async def lesson_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    group = await log_group_take(update, context)
    if group != '-':
        await Lessons_in_day(update, context, await log_group_take(update, context), DT.datetime.today().weekday())
    else:
        update.message.reply_text(f'Apparently you or such a group is not in the database!\nPlease enter the command as: \n/group НПМбд-01-21')

async def lesson_tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    day = DT.datetime.today().weekday() + 1
    if day == 7: day = 0
    if group != '-':
        day = DT.datetime.today().weekday() + 1
        if day == 7: day = 0
        await Lessons_in_day(update, context, await log_group_take(update, context), day)
    else:
        update.message.reply_text(f'Apparently you or such a group is not in the database!\nPlease enter the command as: \n/group НПМбд-01-21')

