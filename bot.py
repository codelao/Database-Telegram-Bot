import telebot
from telebot import types
import markups as nav
from config import TOKEN, ADMIN, Sticker
from db import Database

bot = telebot.TeleBot(TOKEN)

#database file
db = Database('')

#I used markdown for beautiful text
markdown = '''
*bold text*
[text](URL)
'''


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == ADMIN:
            bot.send_sticker(message.from_user.id, Sticker, reply_markup=nav.Restart)
            bot.send_message(message.from_user.id, 'Welcome to Admin panel!', reply_markup=nav.AdminMenu)
        else:
            bot.send_sticker(message.from_user.id, Sticker, reply_markup=nav.Restart)
            bot.send_message(message.from_user.id, 'Hi, ' + message.from_user.username + 
                '!', reply_markup=nav.UserMenu
                )

     
@bot.message_handler(commands=['Restart'])
def restart(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == ADMIN:
            messageadmin = bot.send_message(message.chat.id, 'Restarting')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting.')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting..')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting...')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting..')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting.')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting.')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting..')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageadmin.message_id, text='Restarting...')
            bot.delete_message(chat_id=message.chat.id, message_id=messageadmin.message_id)
            bot.send_sticker(message.from_user.id, Sticker, reply_markup=nav.Restart)
            bot.send_message(message.from_user.id, 'Welcome to Admin panel!', reply_markup=nav.AdminMenu)  
        else:
            messageuser = bot.send_message(message.chat.id, 'Restarting')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting.')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting..')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting...')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting..')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting.')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting.')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting..')
            bot.edit_message_text(chat_id=message.chat.id, message_id=messageuser.message_id, text='Restarting...')
            bot.delete_message(chat_id=message.chat.id, message_id=messageuser.message_id)
            bot.send_sticker(message.from_user.id, Sticker, reply_markup=nav.Restart)
            bot.send_message(message.from_user.id, 'Hi there!', reply_markup=nav.UserMenu)

            
@bot.message_handler()
def help(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Help':
            if message.from_user.id == ADMIN:
                bot.send_message(message.chat.id, '➕ - add number\n'
                    '📃 - how many numbers are loaded into the database at the moment\n'
                    '❌ - delete number', reply_markup=nav.AdminMenu
                    )
            else:
                bot.send_message(message.chat.id, '✅ - find number\n'
                    '📲 - contact the manager', reply_markup=nav.UserMenu
                    )
        else:
            bot.send_message(message.chat.id, 'Unknown command')

     
@bot.callback_query_handler(func=lambda callback: callback.data == 'addnumber')
def addnumber(callback):
    addordermessage = bot.send_message(callback.message.chat.id, 'Enter the number')
    bot.register_next_step_handler(addordermessage, addnumber2)

def addnumber2(message: types.Message):
    if not db.get_number(message.text):
        db.add_number(message.text)
        bot.send_message(message.chat.id, 'Number ' + message.text + ' has been successfully added to the database')
    else:
        bot.send_message(message.chat.id, 'This number already exists')

        
@bot.callback_query_handler(func=lambda callback: callback.data == 'getnumber')
def getnumber(callback):
    getordermessage = bot.send_message(callback.message.chat.id, 'Write your number')
    bot.register_next_step_handler(getordermessage, getnumber2)

def getnumber2(message: types.Message):
    if not db.get_number(message.text):
        bot.send_message(message.chat.id, '*Number:* ' + message.text + '\n'
            '*Status:* Not found\n'
            'Try again or [contact the manager](https://t.me/)', parse_mode='Markdown'
            )
    else:
        bot.send_message(message.chat.id, '*Number:* ' + message.text + '\n'
            '*Status:* Found', parse_mode='Markdown'
            )

          
@bot.callback_query_handler(func=lambda callback: callback.data == 'deletenumber')
def deletenumber(callback):
    deleteordermessage = bot.send_message(callback.message.chat.id, 'Enter the number you want to delete')
    bot.register_next_step_handler(deleteordermessage, deletenumber2)

def deletenumber2(message: types.Message):
    if not db.get_number(message.text):
        bot.send_message(message.chat.id, 'This number does not exist')
    else:
        db.delete_number(message.text)
        bot.send_message(message.chat.id, 'You have deleted number ' + message.text)


@bot.callback_query_handler(func=lambda callback: callback.data == 'allnumbers')
def allnumbers(callback):
    numbers = db.all_numbers()
    bot.answer_callback_query(callback.id, show_alert=True, text='Bot has sent you the results')
    bot.send_message(callback.message.chat.id, numbers)

    
if __name__ == "__main__":
    bot.polling(none_stop=True)