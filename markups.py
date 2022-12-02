from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


RestartButton = KeyboardButton('/Restart')
HelpButton = KeyboardButton('Help')
Restart = ReplyKeyboardMarkup(resize_keyboard = True).add(RestartButton, HelpButton)


#user buttons
GetOrderButton = InlineKeyboardButton(text='✅', callback_data='getnumber')
ContactButton = InlineKeyboardButton(text='📲', url='https://t.me/')
UserMenu = InlineKeyboardMarkup(row_width=2)
UserMenu.add(GetOrderButton, ContactButton)


#admin buttons
AdminMenu = InlineKeyboardMarkup(row_width=2)
AddOrderButton = InlineKeyboardButton(text='➕', callback_data='addnumber')
AdminMenu.add(AddOrderButton)
OrdersListButton = InlineKeyboardButton(text='📃', callback_data='allnumbers')
DeleteOrderButton = InlineKeyboardButton(text='❌', callback_data='deletenumber')
AdminMenu.add(OrdersListButton, DeleteOrderButton)