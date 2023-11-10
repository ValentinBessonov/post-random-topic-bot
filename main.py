import datetime
from functools import wraps
import json
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random_topic_selector import get_random_topic
from openai_post_generator import generate_post

with open('config.json', 'r') as f:
    config = json.load(f)

BOT_TOKEN = config.get('bot_token')
CHANNEL_ID = config.get('channel_id')
ALLOWED_USER_NAME = config.get('allowed_user_name')

def authorization(func):
    print(f'Authorization for {func.__name__} command...')

    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        print(f'User {update.effective_user} is trying to execute {func.__name__} command...')
        if update.effective_user.username == ALLOWED_USER_NAME:
            return await func(update, context, *args, **kwargs)
        else:
            await context.bot.send_message(chat_id=update.message.chat_id, text="You are not allowed to execute this command.")
    return wrapper
 
async def main_daily_callback(context: ContextTypes.DEFAULT_TYPE):
    print('Sending random post to channel...')
    post = get_random_post()
    await context.bot.send_message(chat_id=CHANNEL_ID, text=post)
    
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update {update} caused error {context.error}')
    await update.message.reply_text(f'Error: {context.error}')

@authorization
async def send_random_post_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('Sending random post to channel...')
    post = get_random_post()
    await context.bot.send_message(chat_id=CHANNEL_ID, text=post)
    
@authorization
async def get_random_post_to_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('Sending random post to bot...')
    post = get_random_post()
    await update.message.reply_text(post)
    
@authorization   
async def get_post_with_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('Sending post with topic to bot...')
    user_input = " ".join(context.args)
    post = generate_post(user_input)
    await update.message.reply_text(post)
    
@authorization
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('Pinging bot...')
    await update.message.reply_text('Pong!')
    
def get_random_post():
    random_topic = get_random_topic('topics.txt')
    post = generate_post(random_topic)
    return post

if __name__ == '__main__':
    print('Bot starting...')
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    job_queue = app.job_queue
    
    nicosia_tz = pytz.timezone('Asia/Nicosia')
    morning_daily_post_time = datetime.time(hour=9, minute=0, tzinfo=nicosia_tz)
    job_every_10_am = job_queue.run_daily(main_daily_callback, time=morning_daily_post_time, days=(0, 1, 2, 3, 4, 5, 6))
    
    app.add_handler(CommandHandler(send_random_post_to_channel.__name__, send_random_post_to_channel))
    app.add_handler(CommandHandler(get_random_post_to_bot.__name__, get_random_post_to_bot))
    app.add_handler(CommandHandler(get_post_with_topic.__name__, get_post_with_topic))
    app.add_handler(CommandHandler(ping.__name__, ping))
    
    app.add_error_handler(error_handler)
    
    print('Bot polling...')
    app.run_polling()