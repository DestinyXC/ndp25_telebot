import os
import time

import telebot
#from flask import Flask, request
from telebot import types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "7857517263:AAEKGJodf5GxBTW_WV-mWOgOnvwXzRMQM6I"

ADMIN_CHAT_ID = 878332131

bot = telebot.TeleBot(BOT_TOKEN)
#app = Flask(__name__)

user_list = []
chat_dict = {}
nested_list = []
id_list = []
commands = {
    'start'        :      'to register yourself (if you have not already).',
    'your_details'       : 'to check your details.',
    'edit'        : 'to edit your details.',
    'contact_us'    : 'to contact Customer Support Team.',
    'info': 'to get details of NDP shows.'
}


# handle the "/start" command        
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        chat_id = message.chat.id
        print(chat_id)
        print(id_list)
        for i in id_list:
            if str(chat_id) != i:
                msg = bot.send_message(message.chat.id, '''
Greetings! Welcome to NDP 2025 InfoBot!
My name is Thomas and I will be assisting you today.

Please type your name! (For example: Thomas)

NOTE: Please DO NOT Delete this chat to 'reset' the bot. If you need to change any information you have entered incorrectly, there are commands for you to do so after you have registered. If you require any other assistance, you can use the contact us command to send us your issue/query. 
Please wait for the bot to respond. DO NOT spam the bot with /start. If it does not respond after 5 minutes, you can try sending /start again.

Please note that the information can change anytime, do confirm the information with your ALP as well.
        ''')
            bot.register_next_step_handler(msg, ndp_show_date)
        else:
            bot.send_message(chat_id, "You have registered before, please use /help for aid. Thank you.")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    try:
        cid = m.chat.id
        help_text = "Greetings! Welcome to NDP 2025 InfoBot! \nMy name is Thomas and I will be assisting you today.\nThese are the commands you can use in the bot: \n"
        for key in commands:  # generate help text out of the commands dictionary defined at the top
            help_text += "Please use /" + key + " "
            help_text += commands[key] + "\n"
        bot.send_message(cid, help_text + "\nThank you!")  # send the generated help page
    except Exception as e:
        bot.reply_to(m, 'Something went wrong, please try again.')

#date of ndp show
def ndp_show_date(message):
    try:
        chat_id = message.chat.id
        name = message.text
        chat_dict.setdefault("Name", []).append(name)
        markup = types.ReplyKeyboardMarkup(row_width=3)
        itembtn1 = types.KeyboardButton('29/06/25')
        itembtn2 = types.KeyboardButton('06/07/25')
        itembtn3 = types.KeyboardButton('13/07/25')
        markup.add(itembtn1, itembtn2, itembtn3)
        date = bot.send_message(chat_id, "May I know which date is your NDP Show ? Please click on one of the buttons in the markup provided.", reply_markup=markup)
        bot.register_next_step_handler(date, choose_school)
        #bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

#choose school
def choose_school(message):
    try:
        chat_id = message.chat.id
        date = message.text
        chat_dict.setdefault("Show Date", []).extend([date])
        #print(text)
        print(type(date))
        if date == "13/07/25":
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('ADMIRALTY PRIMARY SCHOOL')
            itembtn2 = types.KeyboardButton('ALEXANDRA PRIMARY SCHOOL')
            itembtn3 = types.KeyboardButton('ANDERSON PRIMARY SCHOOL')
            itembtn4 = types.KeyboardButton('ANGLO-CHINESE SCHOOL (JUNIOR)')
            itembtn5 = types.KeyboardButton('ANGLO-CHINESE SCHOOL (PRIMARY)')
            itembtn6 = types.KeyboardButton('ANGSANA PRIMARY SCHOOL')
            itembtn7 = types.KeyboardButton('BEDOK GREEN PRIMARY SCHOOL')
            itembtn8 = types.KeyboardButton('BENDEMEER PRIMARY SCHOOL')
            itembtn9 = types.KeyboardButton('BOON LAY GARDEN PRIMARY SCHOOL')
            itembtn10 = types.KeyboardButton('BUKIT PANJANG PRIMARY SCHOOL')
            itembtn11 = types.KeyboardButton('CANBERRA PRIMARY SCHOOL')
            itembtn12 = types.KeyboardButton('CANOSSA CATHOLIC PRIMARY SCHOOL')
            itembtn13 = types.KeyboardButton('CEDAR PRIMARY SCHOOL')
            itembtn14 = types.KeyboardButton('CHIJ OUR LADY OF GOOD COUNSEL')
            itembtn15 = types.KeyboardButton('CHIJ OUR LADY OF QUEEN OF PEACE')
            itembtn16 = types.KeyboardButton("CHIJ ST. NICHOLAS GIRLS' SCHOOL")
            itembtn17 = types.KeyboardButton('COMPASSVALE PRIMARY SCHOOL')
            itembtn18 = types.KeyboardButton('CONCORD PRIMARY SCHOOL')
            itembtn19 = types.KeyboardButton('EAST SPRING PRIMARY SCHOOL')
            itembtn20 = types.KeyboardButton('EDGEFIELD PRIMARY SCHOOL')
            itembtn21 = types.KeyboardButton('FAIRFIELD METHODIST SCHOOL (PRIMARY)')
            itembtn22 = types.KeyboardButton('FENGSHAN PRIMARY SCHOOL')
            itembtn23 = types.KeyboardButton('FERN GREEN PRIMARY SCHOOL')
            itembtn24 = types.KeyboardButton('FRONTIER PRIMARY SCHOOL')
            itembtn25 = types.KeyboardButton('GREENDALE PRIMARY SCHOOL')
            itembtn26 = types.KeyboardButton('HORIZON PRIMARY SCHOOL')
            itembtn27 = types.KeyboardButton('JING SHAN PRIMARY SCHOOL')
            itembtn28 = types.KeyboardButton('KHENG CHENG SCHOOL')
            itembtn29 = types.KeyboardButton('KRANJI PRIMARY SCHOOL')
            itembtn30 = types.KeyboardButton('LAKESIDE PRIMARY SCHOOL')
            itembtn31 = types.KeyboardButton('MAYFLOWER PRIMARY SCHOOL')
            itembtn32 = types.KeyboardButton("METHODIST GIRLS' SCHOOL (PRIMARY)")
            itembtn33 = types.KeyboardButton('NANYANG PRIMARY SCHOOL')
            itembtn34 = types.KeyboardButton('NAVAL BASE PRIMARY SCHOOL')
            itembtn35 = types.KeyboardButton('NORTH VIEW PRIMARY SCHOOL')
            itembtn36 = types.KeyboardButton('OPERA ESTATE PRIMARY SCHOOL')
            itembtn37 = types.KeyboardButton('PEI HWA PRESBYTERIAN PRIMARY SCHOOL')
            itembtn38 = types.KeyboardButton('PEI TONG PRIMARY SCHOOL')
            itembtn39 = types.KeyboardButton('PRINCESS ELIZABETH PRIMARY SCHOOL')
            itembtn40 = types.KeyboardButton('QIFA PRIMARY SCHOOL')
            itembtn41 = types.KeyboardButton('QIHUA PRIMARY SCHOOL')
            itembtn42 = types.KeyboardButton('QUEENSTOWN PRIMARY SCHOOL')
            itembtn43 = types.KeyboardButton("RAFFLES GIRLS' PRIMARY SCHOOL")
            itembtn44 = types.KeyboardButton('RIVER VALLEY PRIMARY SCHOOL')
            itembtn45 = types.KeyboardButton('RIVERSIDE PRIMARY SCHOOL')
            itembtn46 = types.KeyboardButton('ROSYTH SCHOOL')
            itembtn47 = types.KeyboardButton('SENGKANG GREEN PRIMARY SCHOOL')
            itembtn48 = types.KeyboardButton('SHUQUN PRIMARY SCHOOL')
            itembtn49 = types.KeyboardButton("SINGAPORE CHINESE GIRLS' PRIMARY SCHOOL")
            itembtn50 = types.KeyboardButton('TANJONG KATONG PRIMARY SCHOOL')
            itembtn51 = types.KeyboardButton('TECK GHEE PRIMARY SCHOOL')
            itembtn52 = types.KeyboardButton('TECK WHYE PRIMARY SCHOOL')
            itembtn53 = types.KeyboardButton('TEMASEK PRIMARY SCHOOL')
            itembtn54 = types.KeyboardButton('VALOUR PRIMARY SCHOOL')
            itembtn55 = types.KeyboardButton('WOODLANDS RING PRIMARY SCHOOL')
            itembtn56 = types.KeyboardButton('XINMIN PRIMARY SCHOOL')
            itembtn57 = types.KeyboardButton('XISHAN PRIMARY SCHOOL')
            itembtn58 = types.KeyboardButton('YEW TEE PRIMARY SCHOOL')
            itembtn59 = types.KeyboardButton('YIO CHU KANG PRIMARY SCHOOL')
            itembtn60 = types.KeyboardButton('YISHUN PRIMARY SCHOOL')
            itembtn61 = types.KeyboardButton('YU NENG PRIMARY SCHOOL')
            itembtn62 = types.KeyboardButton('YUMIN PRIMARY SCHOOL')
            itembtn63 = types.KeyboardButton('ZHENGHUA PRIMARY SCHOOL')
            itembtn64 = types.KeyboardButton('AWWA SCHOOL @ NAPIRI')
            itembtn65 = types.KeyboardButton('CANOSSIAN SCHOOL')
            itembtn66 = types.KeyboardButton('CEREBRAL PALSY ALLIANCE SINGAPORE SCHOOL (EAST)')
            itembtn67 = types.KeyboardButton('CEREBRAL PALSY ALLIANCE SINGAPORE SCHOOL (WEST)')
            itembtn68 = types.KeyboardButton('CHAOYANG SCHOOL')
            itembtn69 = types.KeyboardButton('MINDS - TOWNER GARDENS SCHOOL')
            itembtn70 = types.KeyboardButton('RAINBOW CENTRE - YISHUN PARK SCHOOL')
            itembtn71 = types.KeyboardButton('APSN TANGLIN SCHOOL (SEC 3)')
            itembtn72 = types.KeyboardButton('EDEN SCHOOL (CAMPUS 2) (SEC 3)')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19, itembtn20, itembtn21, itembtn22, itembtn23, itembtn24, itembtn25, itembtn26, itembtn27, itembtn28, itembtn29, itembtn30, itembtn31, itembtn32, itembtn33
                    , itembtn34, itembtn35, itembtn36, itembtn37, itembtn38, itembtn39, itembtn40, itembtn41, itembtn42, itembtn43, itembtn44, itembtn45, itembtn46, itembtn47, itembtn48, itembtn49, itembtn50, itembtn51, itembtn52, itembtn53, itembtn54, itembtn55, itembtn56, itembtn57, itembtn58, itembtn59, itembtn60, itembtn61, itembtn62, itembtn63, itembtn64, itembtn65, itembtn66
                    , itembtn67, itembtn68, itembtn69, itembtn70, itembtn71, itembtn72)
            bot.send_message(chat_id, "Please wait as the options load. Thank you!", reply_markup=markup)
            time.sleep(1)
            school = bot.send_message(chat_id, "What school are you from? Please select a school in the markup provided.")
            bot.register_next_step_handler(school, phone_number)
        elif date == "06/07/25":
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn73 = types.KeyboardButton('placeholder school')
            markup.add(itembtn73)
            bot.send_message(chat_id, "Please wait as the options load. Thank you!", reply_markup=markup)
            time.sleep(1)
            school = bot.send_message(chat_id, "What school are you from? Please select a school in the markup provided.")
            bot.register_next_step_handler(school, phone_number)
        elif date == "29/06/25":
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn74 = types.KeyboardButton('placeholder school')
            markup.add(itembtn74)
            bot.send_message(chat_id, "Please wait as the options load. Thank you!", reply_markup=markup)
            time.sleep(1)
            school = bot.send_message(chat_id, "What school are you from? Please select a school in the markup provided.")
            bot.register_next_step_handler(school, phone_number)
        else:
            pass
        #bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

#enter phone number
def phone_number(message):
    try:
        chat_id = message.chat.id
        school = message.text
        chat_dict.setdefault("School", []).extend([school])
        phone = bot.send_message(chat_id, "Please enter your phone number (Eg: 81234567 or 91234567):")
        bot.register_next_step_handler(phone, validate_number)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')  

#validate the phone number given and display info
def validate_number(message):
    try:
        chat_id = message.chat.id
        text = message.text
        chat_dict.setdefault("Phone Number", []).extend([text])
        if not((text.isdigit() and len(text) == 8) and (text[0] == "8" or text[0] == "9")):
            msg = bot.send_message(chat_id, "Please enter a valid phone number. Example: 81234567 or 91234567\nPlease send your phone number again!")
            bot.register_next_step_handler(msg, validate_number)
            return
        chat_dict.setdefault("ID", []).extend([chat_id])
        print(chat_dict)
        if len(nested_list) > 0:
            nested_list.clear()
            for val in chat_dict.values():
                nested_list.append(val)
        else:
            for val in chat_dict.values():
                nested_list.append(val)
        #print(nested_list)
        id = nested_list[4]
        nested_list2 = ( ", ".join( repr(e) for e in id ) )
        if len(id_list) > 0:
            id_list.clear()
            id_list.append(nested_list2)
        else:
            id_list.append(nested_list2)
        print(id_list)
        list_ID = chat_dict["ID"]
        list_name = chat_dict["Name"]
        list_school = chat_dict["School"]
        for i in list_ID:
            if i == chat_id:
                index = list_ID.index(i)
                name = list_name[index]
                school = list_school[index]
        info_text = f"Nice to meet you, {name} from {school}\n\nThese are the commands you can use in the bot: \n\n" 
        for key in commands:  # generate help text out of the commands dictionary defined at the top
            info_text += "/" + key + " "
            info_text += commands[key] + "\n"
        msg = bot.send_message(chat_id, info_text + "\n Thank you!")  # send the generated help page)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')  

@bot.message_handler(commands=['your_details'])
def show_details(message):
    try:
        chat_id = message.chat.id
        list_ID = chat_dict["ID"]
        list_name = chat_dict["Name"]
        list_school = chat_dict["School"]
        list_date = chat_dict["Show Date"]
        list_number = chat_dict["Phone Number"]
        for i in list_ID:
            if i == chat_id:
                index = list_ID.index(i)
                name = list_name[index]
                school = list_school[index]
                show_date = list_date[index]
                number = list_number[index]
        bot.send_message(chat_id, f"Hello! Here are your details:\n\nYour name is {name}.\n\nYou are from {school}.\n\nYour show date is {show_date}.\n\nYour phone number is {number}.\n\nUse /edit to change details if they are inaccurate. Use /help for aid. Thank you!")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

@bot.message_handler(commands=['edit'])
def edit_details(message):
    try:
        chat_id = message.chat.id
        text = message.text
        markup = types.ReplyKeyboardMarkup(row_width=3)
        itembtn1 = types.KeyboardButton('Edit Name')
        itembtn2 = types.KeyboardButton('Edit School')
        itembtn3 = types.KeyboardButton('Edit Phone Number')
        markup.add(itembtn1, itembtn2, itembtn3)
        edit = bot.send_message(chat_id, "May I know which details would you like to change?\n\nSelect 'Edit School' to edit your school based on your show dates. Please use the markup provided.", reply_markup=markup)
        bot.register_next_step_handler(edit, process_edit_details)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.') 

def process_edit_details(message):
    try:
        chat_id = message.chat.id
        text = message.text
        edit_choice = message.text
        markup = types.ReplyKeyboardMarkup(row_width=3)
        itembtn1 = types.KeyboardButton('29/06/25')
        itembtn2 = types.KeyboardButton('06/07/25')
        itembtn3 = types.KeyboardButton('13/07/25')
        markup.add(itembtn1, itembtn2, itembtn3)
        if edit_choice == "Edit Name":
            edit_name = bot.send_message(chat_id, "Please send the name you want to change to.\nType 'Quit' to cancel.\nThank you.")
            bot.register_next_step_handler(edit_name, update_name)
        elif edit_choice == "Edit School":
            edit_date = bot.send_message(chat_id, "Please select the correct date of your NE Show.\nType 'Quit' to cancel.\nThank you.", reply_markup=markup)
            bot.register_next_step_handler(edit_date, update_date)
        elif edit_choice == "Edit Phone Number":
            edit_number = bot.send_message(chat_id, "Please send the phone number you would like to update to (Eg: 81234567 or 91234567).\nType 'Quit' to cancel.\nThank you.")
            bot.register_next_step_handler(edit_number, update_number)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

def update_name(message):
    try:
        chat_id = message.chat.id
        text = message.text
        list_ID = chat_dict["ID"]
        list_name = chat_dict["Name"]
        new_name = text
        if (text.title() == "Quit" or text.lower() == "quit") or (text.upper() == "QUIT"):
            bot.reply_to(message, "Quitting function...")
        else:
            for i in list_ID:
                if i == chat_id:
                    index = list_ID.index(i)
                    list_name[index] = new_name
            bot.send_message(chat_id, "Your name has been updated, use /your_details to check your details. Use /help for aid. Thank you.")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

def update_date(message):
    try:
        chat_id = message.chat.id
        text = message.text
        list_ID = chat_dict["ID"]
        list_date = chat_dict["Show Date"]
        new_date = text
        if (text.title() == "Quit" or text.lower() == "quit") or (text.upper() == "QUIT"):
            bot.reply_to(message, "Quitting function...")
        else:
            for i in list_ID:
                if i == chat_id:
                    index = list_ID.index(i)
                    list_date[index] = new_date
            markup = types.ReplyKeyboardMarkup(row_width=1)
            itembtn1 = types.KeyboardButton('ADMIRALTY PRIMARY SCHOOL')
            itembtn2 = types.KeyboardButton('ALEXANDRA PRIMARY SCHOOL')
            itembtn3 = types.KeyboardButton('ANDERSON PRIMARY SCHOOL')
            itembtn4 = types.KeyboardButton('ANGLO-CHINESE SCHOOL (JUNIOR)')
            itembtn5 = types.KeyboardButton('ANGLO-CHINESE SCHOOL (PRIMARY)')
            itembtn6 = types.KeyboardButton('ANGSANA PRIMARY SCHOOL')
            itembtn7 = types.KeyboardButton('BEDOK GREEN PRIMARY SCHOOL')
            itembtn8 = types.KeyboardButton('BENDEMEER PRIMARY SCHOOL')
            itembtn9 = types.KeyboardButton('BOON LAY GARDEN PRIMARY SCHOOL')
            itembtn10 = types.KeyboardButton('BUKIT PANJANG PRIMARY SCHOOL')
            itembtn11 = types.KeyboardButton('CANBERRA PRIMARY SCHOOL')
            itembtn12 = types.KeyboardButton('CANOSSA CATHOLIC PRIMARY SCHOOL')
            itembtn13 = types.KeyboardButton('CEDAR PRIMARY SCHOOL')
            itembtn14 = types.KeyboardButton('CHIJ OUR LADY OF GOOD COUNSEL')
            itembtn15 = types.KeyboardButton('CHIJ OUR LADY OF QUEEN OF PEACE')
            itembtn16 = types.KeyboardButton("CHIJ ST. NICHOLAS GIRLS' SCHOOL")
            itembtn17 = types.KeyboardButton('COMPASSVALE PRIMARY SCHOOL')
            itembtn18 = types.KeyboardButton('CONCORD PRIMARY SCHOOL')
            itembtn19 = types.KeyboardButton('EAST SPRING PRIMARY SCHOOL')
            itembtn20 = types.KeyboardButton('EDGEFIELD PRIMARY SCHOOL')
            itembtn21 = types.KeyboardButton('FAIRFIELD METHODIST SCHOOL (PRIMARY)')
            itembtn22 = types.KeyboardButton('FENGSHAN PRIMARY SCHOOL')
            itembtn23 = types.KeyboardButton('FERN GREEN PRIMARY SCHOOL')
            itembtn24 = types.KeyboardButton('FRONTIER PRIMARY SCHOOL')
            itembtn25 = types.KeyboardButton('GREENDALE PRIMARY SCHOOL')
            itembtn26 = types.KeyboardButton('HORIZON PRIMARY SCHOOL')
            itembtn27 = types.KeyboardButton('JING SHAN PRIMARY SCHOOL')
            itembtn28 = types.KeyboardButton('KHENG CHENG SCHOOL')
            itembtn29 = types.KeyboardButton('KRANJI PRIMARY SCHOOL')
            itembtn30 = types.KeyboardButton('LAKESIDE PRIMARY SCHOOL')
            itembtn31 = types.KeyboardButton('MAYFLOWER PRIMARY SCHOOL')
            itembtn32 = types.KeyboardButton("METHODIST GIRLS' SCHOOL (PRIMARY)")
            itembtn33 = types.KeyboardButton('NANYANG PRIMARY SCHOOL')
            itembtn34 = types.KeyboardButton('NAVAL BASE PRIMARY SCHOOL')
            itembtn35 = types.KeyboardButton('NORTH VIEW PRIMARY SCHOOL')
            itembtn36 = types.KeyboardButton('OPERA ESTATE PRIMARY SCHOOL')
            itembtn37 = types.KeyboardButton('PEI HWA PRESBYTERIAN PRIMARY SCHOOL')
            itembtn38 = types.KeyboardButton('PEI TONG PRIMARY SCHOOL')
            itembtn39 = types.KeyboardButton('PRINCESS ELIZABETH PRIMARY SCHOOL')
            itembtn40 = types.KeyboardButton('QIFA PRIMARY SCHOOL')
            itembtn41 = types.KeyboardButton('QIHUA PRIMARY SCHOOL')
            itembtn42 = types.KeyboardButton('QUEENSTOWN PRIMARY SCHOOL')
            itembtn43 = types.KeyboardButton("RAFFLES GIRLS' PRIMARY SCHOOL")
            itembtn44 = types.KeyboardButton('RIVER VALLEY PRIMARY SCHOOL')
            itembtn45 = types.KeyboardButton('RIVERSIDE PRIMARY SCHOOL')
            itembtn46 = types.KeyboardButton('ROSYTH SCHOOL')
            itembtn47 = types.KeyboardButton('SENGKANG GREEN PRIMARY SCHOOL')
            itembtn48 = types.KeyboardButton('SHUQUN PRIMARY SCHOOL')
            itembtn49 = types.KeyboardButton("SINGAPORE CHINESE GIRLS' PRIMARY SCHOOL")
            itembtn50 = types.KeyboardButton('TANJONG KATONG PRIMARY SCHOOL')
            itembtn51 = types.KeyboardButton('TECK GHEE PRIMARY SCHOOL')
            itembtn52 = types.KeyboardButton('TECK WHYE PRIMARY SCHOOL')
            itembtn53 = types.KeyboardButton('TEMASEK PRIMARY SCHOOL')
            itembtn54 = types.KeyboardButton('VALOUR PRIMARY SCHOOL')
            itembtn55 = types.KeyboardButton('WOODLANDS RING PRIMARY SCHOOL')
            itembtn56 = types.KeyboardButton('XINMIN PRIMARY SCHOOL')
            itembtn57 = types.KeyboardButton('XISHAN PRIMARY SCHOOL')
            itembtn58 = types.KeyboardButton('YEW TEE PRIMARY SCHOOL')
            itembtn59 = types.KeyboardButton('YIO CHU KANG PRIMARY SCHOOL')
            itembtn60 = types.KeyboardButton('YISHUN PRIMARY SCHOOL')
            itembtn61 = types.KeyboardButton('YU NENG PRIMARY SCHOOL')
            itembtn62 = types.KeyboardButton('YUMIN PRIMARY SCHOOL')
            itembtn63 = types.KeyboardButton('ZHENGHUA PRIMARY SCHOOL')
            itembtn64 = types.KeyboardButton('AWWA SCHOOL @ NAPIRI')
            itembtn65 = types.KeyboardButton('CANOSSIAN SCHOOL')
            itembtn66 = types.KeyboardButton('CEREBRAL PALSY ALLIANCE SINGAPORE SCHOOL (EAST)')
            itembtn67 = types.KeyboardButton('CEREBRAL PALSY ALLIANCE SINGAPORE SCHOOL (WEST)')
            itembtn68 = types.KeyboardButton('CHAOYANG SCHOOL')
            itembtn69 = types.KeyboardButton('MINDS - TOWNER GARDENS SCHOOL')
            itembtn70 = types.KeyboardButton('RAINBOW CENTRE - YISHUN PARK SCHOOL')
            itembtn71 = types.KeyboardButton('APSN TANGLIN SCHOOL (SEC 3)')
            itembtn72 = types.KeyboardButton('EDEN SCHOOL (CAMPUS 2) (SEC 3)')
            markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19, itembtn20, itembtn21, itembtn22, itembtn23, itembtn24, itembtn25, itembtn26, itembtn27, itembtn28, itembtn29, itembtn30, itembtn31, itembtn32, itembtn33
                    , itembtn34, itembtn35, itembtn36, itembtn37, itembtn38, itembtn39, itembtn40, itembtn41, itembtn42, itembtn43, itembtn44, itembtn45, itembtn46, itembtn47, itembtn48, itembtn49, itembtn50, itembtn51, itembtn52, itembtn53, itembtn54, itembtn55, itembtn56, itembtn57, itembtn58, itembtn59, itembtn60, itembtn61, itembtn62, itembtn63, itembtn64, itembtn65, itembtn66
                    , itembtn67, itembtn68, itembtn69, itembtn70, itembtn71, itembtn72)
            bot.send_message(chat_id, "Please wait as the options load. Thank you!", reply_markup=markup)
            time.sleep(1)
            school = bot.send_message(chat_id, "What school are you from? Please select a school in the markup provided.\n\nType 'Quit' to cancel.")
            bot.register_next_step_handler(school, update_school)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

def update_school(message):
    try:
        chat_id = message.chat.id
        text = message.text
        list_ID = chat_dict["ID"]
        list_school = chat_dict["School"]
        new_school = text
        if (text.title() == "Quit" or text.lower() == "quit") or (text.upper() == "QUIT"):
            bot.reply_to(message, "Quitting function...")
        else:
            for i in list_ID:
                if i == chat_id:
                    index = list_ID.index(i)
                    list_school[index] = new_school
            bot.send_message(chat_id, "Your school has been updated, use /your_details to check your details. Use /help for aid. Thank you.")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

def update_number(message):
    try:
        chat_id = message.chat.id
        text = message.text
        list_ID = chat_dict["ID"]
        list_number = chat_dict["Phone Number"]
        new_number = text
        if (text.title() == "Quit" or text.lower() == "quit") or (text.upper() == "QUIT"):
            bot.reply_to(message, "Quitting function...")
        else:
            for i in list_ID:
                if i == chat_id:
                    index = list_ID.index(i)
                    list_number[index] = new_number
            bot.send_message(chat_id, "Your number has been updated, use /your_details to check your details. Use /help for aid. Thank you.")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

@bot.message_handler(commands=['contact_us'])
def contact_us(message):
    try:
        chat_id = message.chat.id
        contact_us = bot.send_message(chat_id, "Please reply with the message which you would like to tell Customer Support Team.\nType 'Quit' to cancel.\nThank you.")
        bot.register_next_step_handler(contact_us, process_contact_us)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

@bot.message_handler(commands=['info'])
def info(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(row_width=3)
        itembtn1 = types.KeyboardButton('Quit')
        itembtn2 = types.KeyboardButton('NE Show No.')
        itembtn3 = types.KeyboardButton('Google map links')
        itembtn4 = types.KeyboardButton('Arrival Details')
        itembtn5 = types.KeyboardButton('Dismissal Details')
        itembtn6 = types.KeyboardButton('Direction of Arrival')
        itembtn7 = types.KeyboardButton('Liaison Personnel')
        itembtn8 = types.KeyboardButton('Seating Sector')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
        info_msg = bot.send_message(chat_id, "What would you like to know? Please use the markup provided.\nPlease note that the information can change anytime, do confirm the information with your ALP.\n\nPlease use the 'Quit' button before using any other commands.\n\nThank you!", reply_markup=markup)
        bot.register_next_step_handler(info_msg, process_info)
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')          

def process_info(message):
    try:
        chat_id = message.chat.id
        text = message.text
        list_ID = chat_dict["ID"]
        list_date = chat_dict["Show Date"]
        list_school = chat_dict["School"]
        for i in list_ID:
            if i == chat_id:
                index = list_ID.index(i)
        if (text.title() == "Quit" or text.lower() == "quit") or (text.upper() == "QUIT"):
            bot.reply_to(message, "Successfully exited /info.\nUse /help for more assistance.")
            bot.edit_message_reply_markup(chat_id, message_id=message.message_id - 1, reply_markup=None)
        elif text.lower() == "ne show no.":
            if list_date[index] == "29/06/25":
                bot.send_message(chat_id, "Your NE show no. is 1")
            elif list_date[index] == "06/07/25":
                bot.send_message(chat_id, "Your NE show no. is 2")
            elif list_date[index] == "13/07/25":
                bot.send_message(chat_id, "Your NE show no. is 3")
            repeat_info()
            repeat = bot.send_message(chat_id, "What else would you like to know?")
            bot.register_next_step_handler(repeat, process_info)
        elif text.lower() == "google map links":
            bot.send_message(chat_id, "Please wait while the route guide loads...")
            time.sleep(1)
            if list_school[index] == "BUKIT PANJANG PRIMARY SCHOOL":
                markup1 = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text=f"School to Padang route", url="https://maps.app.goo.gl/zoeQVt61ftcXQRFeA")
                markup2 = types.InlineKeyboardMarkup()
                button2 = types.InlineKeyboardButton(text=f"Padang to School route", url="https://maps.app.goo.gl/HKnUXPi34oEdBvkf8")
                markup1.add(button1)
                markup2.add(button2)
                bot.send_message(chat_id, "Route from BUKIT PANJANG PRIMARY SCHOOL to Padang", reply_markup=markup1)
                bot.send_message(chat_id, "Route from Padang to BUKIT PANJANG PRIMARY SCHOOL", reply_markup=markup2)
                bot.send_message(chat_id, "Click the links above to follow the routes.")
                repeat_info()
                repeat = bot.send_message(chat_id, "What else would you like to know?")
                bot.register_next_step_handler(repeat, process_info)
        elif text.lower() == "arrival details":
            bot.send_message(chat_id, "Your arrival to Padang timings are as follows:")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.') 

def repeat_info():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = types.KeyboardButton('Quit')
    itembtn2 = types.KeyboardButton('NE Show No.')
    itembtn3 = types.KeyboardButton('Google map links')
    itembtn4 = types.KeyboardButton('Arrival Details')
    itembtn5 = types.KeyboardButton('Dismissal Details')
    itembtn6 = types.KeyboardButton('Direction of Arrival')
    itembtn7 = types.KeyboardButton('Liaison Personnel')
    itembtn8 = types.KeyboardButton('Seating Sector')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

    return


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")


@bot.message_handler(func=lambda message: "/" not in message.text)
def process_contact_us(message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        qns = message.text
        if (qns.title() == "Quit" or qns.lower() == "quit") or (qns.upper() == "QUIT"):
            bot.reply_to(message, "Quitting function...")
        else:
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text=f"Reply to {user_name}", url=f"tg://user?id={user_id}")
            markup.add(button)
            #chat_dict.setdefault("Questions", []).extend([qns])
            #print(chat_dict)
            bot.send_message(ADMIN_CHAT_ID, f"Message from {user_name} (ID: {user_id}):\n{qns}", reply_markup=markup)
            bot.send_message(chat_id, "Message has been sent to Customer Support Team.\n\nWe will get back to you as soon as possible.\n\nThank you!\nUse /help for more options!")
    except Exception as e:
        bot.reply_to(message, 'Something went wrong, please try again.')

def listener(messages):
    
    #When new messages arrive TeleBot will call this function.
    
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot.set_update_listener(listener)  # register listener


# Handle incoming webhook updates
#processed_updates = set()

'''@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        json_data = request.get_json(force=True)
        print("Received update:", json_data)
        update = telebot.types.Update.de_json(json_data)

        # Check if the update has already been processed
        if update.update_id in processed_updates:
            return "OK"

        # Mark the update as processed
        processed_updates.add(update.update_id)

        # Process the update
        bot.process_new_updates([update])
        return "OK"
    except Exception as e:
        print("Error processing update:", str(e))
        return "ERROR", 500

import threading

def clear_processed_updates():
    global processed_updates
    while True:
        processed_updates.clear()
        time.sleep(3600)  # Clear every hour

threading.Thread(target=clear_processed_updates, daemon=True).start()

# Set the webhook URL when the app starts
if __name__ == "__main__":
    # Remove any existing webhook
    bot.remove_webhook()
    # Set the webhook to your Render service's URL
    bot.set_webhook(url="https://ndp25-telebot.onrender.com/webhook")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))'''

bot.remove_webhook()
bot.infinity_polling()