import telebot
from telebot import types
from telebot.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats
import json
from collections import deque
from telebot import types
import re
from datetime import datetime, timedelta
import os
DATA_FILE = 'dranoew108.json'
user_temp_data = {}
namee = ""
name = 11
mbda = ""
magsd = ""
mbda2 = ""
magsd2 = ""
zaman = ""
zaman2 = ""
amrt = ""
noae = ""
noae4=""
name1 = ""
name2 = ""
name22 = ""
noae1 = ""
noae2 = ""
amar = ""
amar1 = ""
amar3 = ""
tre = ""
call=""
chat = ""
CHANNEL_ID_1 = '@retesw4'
CHANNEL_ID_2 = '@mmmdder'
CHANNEL_ID_3 = '@tre23ue'
entm = {}
script_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        dra = json.load(f)
else:
    dra = {}
agh = {}
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['add_player'])
def add_player(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            if user_id in dra:
                bot.send_message(message.chat.id, 'این کاربر به عنوان پلیر وجود دارد!!')
            else:
                test = "نام پلیر"
                dra[user_id] = {
                    'نام پلیر': test,
                    'mhb': 30,
                    'دارایی': {
                        'megdar': {
                            'چوب': {'مقدار': 0},
                            'اهن': {'مقدار': 0},
                            'sang energi':{'مقدار': 10}
                        },
                        'tolidi': {
                            'کارخانه': {
                                'لول': 1,
                                'بازدهی': 50,
                                'نوع': 'چوب',
                                'bzup': 20,
                                'update': {
                                    'nm': {
                                        'چوب': {'tedad': 30}
                                    }
                                }
                            },
                            'اهنگری': {
                                'لول': 1,
                                'بازدهی': 30,
                                'نوع': 'اهن',
                                'bzup': 30,
                                'update': {
                                    'nm': {
                                        'چوب': {'tedad': 30},
                                        'اهن': {'tedad': 20}
                                    }
                                }
                            }
                        },
                        'منبع غذایی': {
                            'غذاها': {
                                'کنسرو': {'مقدار': 50,
                                        'zr': 2},
                                'test': {'مقدار': 20,
                                        'zr': 1}
                            },
                            'تولیدی': {
                                'کارخانه کنسرو سازی': {
                                    'لول': 2,
                                    'بازدهی': 30,
                                    'نوع': 'کنسرو',
                                    'bzup': 15,
                                    'update': {
                                        'nm': {
                                            'چوب': {'tedad': 20},
                                            'اهن': {'tedad': 20}
                                        }
                                    }
                                }
                            }
                        },
                        'منابع انسانی': {
                            'نیروی انسانی': {
                                'مردم': {'mgd':50,
                                        'msr': 1,
                                        'ghn':50},
                                'دانشمند': {'mgd':5,
                                        'msr': 1,
                                        'ghn':5},
                                'مهندس': {'mgd':5,
                                        'msr': 1,
                                        'ghn':5},
                                'دکتر': {'mgd':2,
                                        'msr': 1,
                                        'ghn':2},
                                'سرباز': {'mgd':10,
                                        'msr': 1,
                                        'ghn':10}
                            },
                            'ساختمان': {
                                'تلپورتر': {
                                    'لول': 1,
                                    'بازدهی': {
                                        'مردم': {'بازده': 5,
                                                'مصرفی': 1,
                                                'bzb': 5},
                                        'دانشمند': {'بازده': 1,
                                                    'مصرفی': 1,
                                                    'bzb': 1},
                                        'مهندس': {'بازده': 1,
                                                'مصرفی': 1,
                                                'bzb': 1},
                                        'دکتر': {'بازده': 1,
                                                'مصرفی': 2,
                                                'bzb': 1},
                                        'سرباز': {'بازده': 3,
                                                'مصرفی': 1,
                                                'bzb': 3}
                                    }
                                }
                            }
                        }
                    }
                }

                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, f'پلیر {test} اضافه شد!')
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
@bot.message_handler(commands=['load_players'])
def load_players(message):
    user_id = message.from_user.id
    user_id2 = str(message.reply_to_message.from_user.id)
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id in adl:
        try:
            with open(DATA_FILE, 'r') as json_file:
                loaded_dict = json.load(json_file)
                gph = loaded_dict[user_id2]
            bot.send_message(message.chat.id, str(gph))
        except FileNotFoundError:
            bot.send_message(message.chat.id, f"فایل {DATA_FILE} پیدا نشد.")
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
@bot.message_handler(commands=['darai'])
def send_daraie(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
    else:    
        user_id = str(message.from_user.id)
    if user_id in dra:
        player_data = dra[user_id]
        response_message = f"نام پلیر: {player_data['نام پلیر']}\nمحبوبیت: {player_data['mhb']}\n"
        darai = player_data['دارایی']
        for factory, details in darai['منابع انسانی']['ساختمان'].items():
            response_message += f"{factory} سطح {details['لول']}\n"
        mardom = darai['منابع انسانی'].get('نیروی انسانی', {})
        for item, val in mardom.items():
            response_message += f"{item}: {val['mgd']}\n"
        for noee, details in darai['megdar'].items():
            response_message += f"{noee} : {details['مقدار']}\n"
        ghaza = darai["منبع غذایی"].get("غذاها", {})
        for item, val in ghaza.items():
            response_message += f"{item}: {val['مقدار']}\n"
        for factory, details in darai['tolidi'].items():
            response_message += f"{factory} {details['لول']}: {details['بازدهی']} {details['نوع']}\n"
# تولیدی منبع غذایی
        ghaza_tolid = darai["منبع غذایی"].get("تولیدی", {})
        for factory, val in ghaza_tolid.items():
            response_message += f"{factory} {val['لول']}: {val['بازدهی']} {val['نوع']}\n"
        bot.send_message(message.chat.id, response_message)
        start(message)
    else:
        bot.send_message(message.chat.id, "این کاربر هنوز به عنوان پلیر اضافه نشده است.")
    

@bot.message_handler(commands=['up'])
def up(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            if user_id in dra:
                player_data = dra[user_id]
                darai = player_data.get('دارایی', {})

                if 'tolidi' not in darai or 'megdar' not in darai:
                    bot.send_message(message.chat.id, "اطلاعات تولید یا مقدار برای این کاربر ناقص است.")
                    return

                response_message = f"بروزرسانی منابع:\n"
                for tolidi_name, details in darai['tolidi'].items():
                    bazde = details.get('بازدهی', 0)
                    type_d = details.get('نوع', '')
                    if type_d in darai['megdar']:
                        darai['megdar'][type_d]['مقدار'] += bazde
                        response_message += f"{type_d} : +{bazde} (از {tolidi_name})\n"
                        with open(DATA_FILE, 'w') as json_file:
                            json.dump(dra, json_file, indent=4)
                    else:
                        response_message += f"{type_d} وجود ندارد در منابع.\n"
                for tolidi_name, details in darai['منبع غذایی']['تولیدی'].items():
                    bazde = details.get('بازدهی', 0)
                    type_d = details.get('نوع', '')
                    if type_d in darai['منبع غذایی']['غذاها']:
                        darai['منبع غذایی']['غذاها'][type_d]['مقدار'] += bazde
                        response_message += f"{type_d} : +{bazde} (از {tolidi_name})\n"
                        with open(DATA_FILE, 'w') as json_file:
                            json.dump(dra, json_file, indent=4)
                    else:
                        response_message += f"{type_d} وجود ندارد در منابع.\n"
                    for tolidi_name, details in darai['منابع انسانی']['نیروی انسانی'].items():
                        mzn = details.get('ghn', 0)
                        sgq = tolidi_name
                        details['mgd'] -= mzn
                        response_message += f" مرگ {mzn} {sgq} بر اثر گشنگی\n"
                        details['ghn'] = details['mgd']
                        with open(DATA_FILE, 'w') as json_file:
                            json.dump(dra, json_file, indent=4) 
                    bot.send_message(message.chat.id, response_message)
            else:
                bot.send_message(message.chat.id, "این کاربر هنوز به عنوان پلیر اضافه نشده است.")
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.from_user.id)
    if user_id in dra:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        markup.add("|⬆️|-ارتقا", "|💵|-دارایی", "|♦️|-لشکرکشی", "|⚔|-دستور حمله", "|🗡|-دستور محاصره", "|🚀|-حمله موشکی", "|♣️|-توییتر")
        bot.send_message(message.chat.id, "سلام فرمانده، چه کاری براتون انجام بدم؟", reply_markup=markup)
        bot.register_next_step_handler(message, amlll)
    else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
def amlll(message):
    user_id = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    if message.text == "|⬆️|-ارتقا":
        if user_id in dra:
            player_data = dra[user_id]
            darai = player_data['دارایی']
            markupt.add("|👤|-منابع انسانی", "|🥣|-منابع غذایی", "|⛏|-منابع اقتصادی")
            bot.send_message(message.chat.id, "|❓|-لطفا بخش مورد نظر را انتخاب نمایید", reply_markup=markupt)
            bot.register_next_step_handler(message, aml)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
    elif message.text == "|💵|-دارایی":
        if user_id in dra:
            send_daraie(message)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")  
    if message.text == '|♦️|-لشکرکشی':
        markupt.add("زمینی", "دریایی","هوایی", "🔁 بازگشت به منو" )
        if user_id in dra:
            player_data = dra[user_id]
          # استفاده از متغیر سراسری
            bot.send_message(message.chat.id, "لطفا نوع لشکرکشی را وارد کنید", reply_markup= markupt)
            bot.register_next_step_handler(message, ppnoa)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
    elif message.text == '|⚔|-دستور حمله':
        if user_id in dra:
            player_data = dra[user_id]
            markupt.add("زمینی", "دریایی","هوایی", "🔁 بازگشت به منو" )
            bot.send_message(message.chat.id, "لطفا نوع حمله را وارد کنید", reply_markup= markupt )
            bot.register_next_step_handler(message,ppnw)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
    elif message.text == '|🗡|-دستور محاصره':
        if user_id in dra:
            player_data = dra[user_id]
            markupt.add("زمینی", "دریایی","هوایی", "🔁 بازگشت به منو" )
            bot.send_message(message.chat.id, "لطفا نوع محاصره را وارد کنید", reply_markup= markupt)
            bot.register_next_step_handler(message, ppnwe)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
    elif message.text == '|🚀|-حمله موشکی':
        if user_id in dra:
            player_data = dra[user_id]
            markupt.add("🔁 بازگشت به منو" )
            bot.send_message(message.chat.id, "لطفا مکان حمله را وارد کنید", reply_markup= markupt)
            bot.register_next_step_handler(message, ppnwemjlkh)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
    elif message.text == '|♣️|-توییتر':
        if user_id in dra:
            player_data = dra[user_id]
            markuptt2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markuptt2.add("🔁 بازگشت به منو" )
            bot.send_message(message.chat.id, "لطفا متن مورد نظر را وارد نمایید", reply_markup= markuptt2)
            bot.register_next_step_handler(message, pptte)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
def fwdwttdyt(message):
    user_id = str(message.from_user.id)
    player_data = dra[user_id]
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markupt.add("🔁 بازگشت به منو" )
    bot.send_message(message.chat.id, "لطفا مکان حمله را وارد کنید", reply_markup= markupt)
    bot.register_next_step_handler(message, ppnwemjlkh)
def ppnwemjlkh(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id] = {}  # پاکسازی داده‌های قبلی این کاربر
    user_temp_data[user_id]['noae2'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا آمار موشک های خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, eraa)
def ppmnt2wwe2lplk(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        bot.reply_to(message, "لطفا آمار آمار موشک های خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, eraa)
def eraa(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['amar1'] = message.text

    d = user_temp_data[user_id]
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['noae2']
        fwdwttdyt(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add('خير', 'بله', "↪️ باز گشت به مرحله قبل")

        bot.reply_to(message, "آیا دستور حمله موشکی را تایید می کنید؟", reply_markup=markupt)
        bot.register_next_step_handler(message, ppersalhghj2)

def ppersalhghj2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    javab = message.text
    d = user_temp_data.get(user_id, {})
    if message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['amar1']
        ppmnt2wwe2lplk(message)
    else:
        if javab == "بله":
            bot.send_message(
                CHANNEL_ID_2,
                f"آمار دستور حمله موشکی ارتش «{dra[user_id2]['نام پلیر']}» به منطقه «{d['noae2']}»\n «{d['amar1']}»"
            )
            photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-04_21-35-55.jpg')
            caption = f"|⚔️|-فرمانده ارتش «{dra[user_id2]['نام پلیر']}» دستور حمله موشکی به  منطقه «{d['noae2']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            with open(photo_path, 'rb') as photo:
                bot.send_photo(CHANNEL_ID_1, photo, caption=caption)
                bot.send_message(message.chat.id, "✅ دستور حمله موشکی با موفقیت ارسال شد")
                del user_temp_data[user_id]
                start(message)
        elif javab == "خیر":
            bot.send_message(message.chat.id, "✅ دستور حمله موشکی لغو شد")
            del user_temp_data[user_id]
            start(message)
def pptte(message):
    user_id = str(message.from_user.id)
    tre = message.text
    #entm = user_id
    user_temp_data[user_id] = tre
    if message.text == "🔁 بازگشت به منو":
        start(message)
        del user_temp_data[user_id] 
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)    
        # افزودن دکمه‌ها
        markupt.add('خير', 'بله')
        bot.send_message(message.chat.id, "آیا بیانیه خود را تایید می کنید؟", reply_markup= markupt)
        bot.register_next_step_handler(message, pnm)
def pnm(message):
    user_id = str(message.from_user.id)
    jb = message.text
    if jb == 'بله':
        bot.send_message(CHANNEL_ID_3, f"بیانیه فرمانده «{dra[user_id]['نام پلیر']}» :\n «{user_temp_data[user_id]}»")
        bot.send_message(message.chat.id, "✅ توییت شما با موفقیت ارسال شد")
        del user_temp_data[user_id]
        start(message)
    elif jb == 'خير':
        bot.send_message(message.chat.id, "✅ عملیات ارسال توییت متوقف شد")
        del user_temp_data[user_id]
        start(message)
def ngm22(message):
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)   
    markupt.add("زمینی", "دریایی","هوایی", "🔁 بازگشت به منو" )
    bot.send_message(message.chat.id, "لطفا نوع محاصره را وارد کنید", reply_markup= markupt)
    bot.register_next_step_handler(message, ppnwe)
def ppnwe(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id] = {}  # پاکسازی داده‌های قبلی این کاربر
    user_temp_data[user_id]['noae2'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا نام منطقه مورد نظر را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmnt2)
def ppnwe22e(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا نام منطقه مورد نظر را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmnt2)
def ppmnt2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['name2'] = message.text
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['noae2']
        ngm22(message)
    else:
        bot.reply_to(message, "لطفا آمار ارتش خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, pptaid2)
def ppmnt2wwe2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        bot.reply_to(message, "لطفا آمار ارتش خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, pptaid2)

def pptaid2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['amar1'] = message.text

    d = user_temp_data[user_id]
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['name2']
        ppnwe22e(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add('خير', 'بله', "↪️ باز گشت به مرحله قبل")

        bot.reply_to(message, "آیا دستور محاصره را تایید می کنید؟", reply_markup=markupt)
        bot.register_next_step_handler(message, ppersal2)

def ppersal2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    javab = message.text
    d = user_temp_data.get(user_id, {})
    if message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['amar1']
        ppmnt2wwe2(message)
    else:
        if javab == "بله":
            bot.send_message(
                CHANNEL_ID_2,
                f"آمار دستور محاصره ارتش {d['noae2']} «{dra[user_id2]['نام پلیر']}» به منطقه «{d['name2']}»\n «{d['amar1']}»"
            )
            if d['noae2'] == "زمینی":
                photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-04_21-35-55.jpg')
                caption = f"|⚔️|-فرمانده ارتش زمینی «{dra[user_id2]['نام پلیر']}» دستور محاصره منطقه «{d['name2']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            elif d['noae2'] == "دریایی":
                photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-26_11-57-33.jpg')
                caption = f"|🪝|-فرمانده ارتش دریایی «{dra[user_id2]['نام پلیر']}» دستور محاصره منطقه «{d['name2']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            elif d['noae2'] == "هوایی":
                photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-26_11-59-17.jpg')
                caption = f"|🛸|-فرمانده ارتش هوایی «{dra[user_id2]['نام پلیر']}» دستور محاصره منطقه «{d['name2']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            else:
                bot.send_message(message.chat.id, "نوع نیرو نامشخص است.")
                del user_temp_data[user_id]
                start(message)

            with open(photo_path, 'rb') as photo:
                bot.send_photo(CHANNEL_ID_1, photo, caption=caption)
            bot.send_message(message.chat.id, "✅ دستور محاصره با موفقیت ارسال شد")
            del user_temp_data[user_id]
            start(message)

        elif javab == "خیر":
            bot.send_message(message.chat.id, "✅ دستور محاصره لغو شد")
            del user_temp_data[user_id]
            start(message)
def aqws2(message):
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)   
    markupt.add("زمینی", "دریایی","هوایی", "🔁 بازگشت به منو" )
    bot.send_message(message.chat.id, "لطفا نوع حمله را وارد کنید", reply_markup= markupt )
    bot.register_next_step_handler(message,ppnw)
def ppnw(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id] = {}  # پاکسازی اطلاعات قبلی

    user_temp_data[user_id]['noae1'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا نام منطقه مورد نظر را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmnt)
def ppnwe22(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا نام منطقه مورد نظر را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmnt)
def ppmnt(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['name1'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['noae1']
        aqws2(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا آمار ارتش خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, pptaid)
def ppmntw2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا آمار ارتش خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, pptaid)
def pptaid(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['amar'] = message.text

    d = user_temp_data[user_id]
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['name1']
        ppnwe22(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add('خير', 'بله', "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "آیا دستور حمله را تایید می‌کنید؟", reply_markup=markupt)
        bot.register_next_step_handler(message, ppersal)

def ppersal(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    javab = message.text
    d = user_temp_data.get(user_id, {})
    if message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['amar']
        ppmntw2(message)
    else:
        if javab == "بله":
            bot.send_message(CHANNEL_ID_2, f" آمار دستور حمله  ارتش {d['noae1']} «{dra[user_id2]['نام پلیر']}» به منطقه «{d['name1']}»\n «{d['amar']}»")
            if d['noae1'] == "زمینی":
                photo_path = os.path.join(script_dir, 'picther\\ganz.jpg')
                caption = f"|⚔️|-فرمانده ارتش زمینی «{dra[user_id2]['نام پلیر']}» دستور حمله به منطقه «{d['name1']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            elif d['noae1'] == "دریایی":
                photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-26_13-06-16.jpg')
                caption = f"|🪝|-فرمانده ارتش دریایی «{dra[user_id2]['نام پلیر']}» دستور حمله به منطقه «{d['name1']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            elif d['noae1'] == "هوایی":
                photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-26_11-59-28.jpg')
                caption = f"|🛸|-فرمانده ارتش هوایی «{dra[user_id2]['نام پلیر']}» دستور حمله به منطقه «{d['name1']}» را ارسال کرد\n سناریو را تا زمان تعیین شده ارسال نمایید"
            else:
                bot.send_message(message.chat.id, "نوع نیرو نامشخص است.")
                del user_temp_data[user_id]
                start(message)
                

            with open(photo_path, 'rb') as photo:
                bot.send_photo(CHANNEL_ID_1, photo, caption=caption)
            bot.send_message(message.chat.id, "✅ دستور حمله با موفقیت ارسال شد")
            del user_temp_data[user_id]
            start(message)

        elif javab == "خیر":
            bot.send_message(message.chat.id, "✅ دستور حمله لغو شد")
            del user_temp_data[user_id]
            start(message)
def est22(message):
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)   
    markupt.add("زمینی", "دریایی","هوایی", "🔁 بازگشت به منو" )

    bot.send_message(message.chat.id, "لطفا نوع لشکرکشی را وارد کنید", reply_markup= markupt)
    bot.register_next_step_handler(message, ppnoa)

def ppnoa(message):
    user_id = message.from_user.id
    user_temp_data[user_id] = {}  # پاک کردن اطلاعات قبلی
    user_temp_data[user_id]['noae'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")

        bot.reply_to(message, "لطفا مبدا را واردکنيد", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmabdar)

def ppnoa223(message):
    user_id = message.from_user.id
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا مبدا را واردکنيد", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmabdar)

def ppmabdar(message):
    user_id = message.from_user.id
    user_temp_data[user_id]['mbda'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['noae']
        est22(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا مقصد را وارد کنيد", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmagsddr)
def ppmabdar2(message):
    user_id = message.from_user.id
    if message.text == "🔁 بازگشت به منو":
        start(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا مقصد را وارد کنيد", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmagsddr)
def ppmagsddr(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['magsd'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['mbda']
        ppnoa223(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا فاصله مبدا تا مقصد را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, ppmagsddrnkl)
def ppmagsddrnkl(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['klm'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['magsd']
        ppmabdar2(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
        bot.reply_to(message, "لطفا آمار و توضحیات لشکر خود را وارد نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, amteer)
def ppmagsddr2(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
    bot.reply_to(message, "لطفا آمار و توضحیات لشکر خود را وارد نمایید", reply_markup=markupt)
    bot.register_next_step_handler(message, amteer)
def ppmabdar23w(message):
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markupt.add("🔁 بازگشت به منو", "↪️ باز گشت به مرحله قبل")
    bot.reply_to(message, "لطفا فاصله مبدا تا مقصد را وارد نمایید", reply_markup=markupt)
    bot.register_next_step_handler(message, ppmagsddrnkl)
def amteer(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    user_temp_data[user_id]['amrt'] = message.text
    if message.text == "🔁 بازگشت به منو":
        start(message)
    elif message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['klm']
        ppmabdar23w(message)
    else:
        markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markupt.add('خير', 'بله', "↪️ باز گشت به مرحله قبل")
        bot.send_message(message.chat.id, "آیا دستور لشکرکشی را تایید می کنید؟", reply_markup= markupt)
        bot.register_next_step_handler(message, ppersalll)

def ppersalll(message):
    user_id = message.from_user.id
    user_id2 = str(message.from_user.id)
    javab = message.text
    d = user_temp_data.get(user_id, {})
    if message.text == "↪️ باز گشت به مرحله قبل":
        del user_temp_data[user_id]['amrt']
        ppmagsddr2(message)
    else:
        if javab == "بله":
            if 1 == 1:
                length = ((int(user_temp_data[user_id]['klm'])/100) * 60)
                #new_time = datetime.now() + timedelta(minutes=int(length))
                #zaman = f"{new_time.hour:02}:{new_time.minute:02}"
                bot.send_message(CHANNEL_ID_2, f"آمار ارتش {d['noae']} «{dra[user_id2]['نام پلیر']}»  برای لشکرکشی از منطقه «{d['mbda']}» به منطقه «{d['magsd']}»\n «{d['amrt']}»")
                if d['noae'] == "زمینی":
                    new_time = datetime.now() + timedelta(minutes=int(length))
                    zaman = f"{new_time.hour:02}:{new_time.minute:02}"
                    photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-26_13-06-27.jpg')
                    caption = f"|🔱|-ارتش زمینی «{dra[user_id2]['نام پلیر']}» از «{d['mbda']}» به طرف «{d['magsd']}» حرکت کردند \n|⏳|-زمان رسیدن: {zaman}"
                elif d['noae'] == "دریایی":
                    new_time = datetime.now() + timedelta(minutes=(int(length)/2))
                    zaman = f"{new_time.hour:02}:{new_time.minute:02}"
                    photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-26_12-01-26.jpg')
                    caption = f"|⚓️|-ارتش دریایی «{dra[user_id2]['نام پلیر']}» از «{d['mbda']}» به طرف «{d['magsd']}» حرکت کردند \n|⏳|-زمان رسیدن: {zaman}"
                elif d['noae'] == "هوایی":
                    new_time = datetime.now() + timedelta(minutes=(int(length)/3))
                    zaman = f"{new_time.hour:02}:{new_time.minute:02}"
                    photo_path = os.path.join(script_dir, 'picther\\photo_2025-06-05_21-54-20.jpg')
                    caption = f"|🛰|-ارتش هوایی «{dra[user_id2]['نام پلیر']}» از «{d['mbda']}» به طرف «{d['magsd']}» حرکت کردند \n|⏳|-زمان رسیدن: {zaman}"
                else:
                    bot.send_message(message.chat.id, "نوع نیرو نامشخص است.")
                    del user_temp_data[user_id]
                    return

                with open(photo_path, 'rb') as photo:
                    bot.send_photo(CHANNEL_ID_1, photo, caption=caption)
                bot.send_message(message.chat.id, "✅ دستور لشکرکشی با موفقیت ارسال شد")
                del user_temp_data[user_id]
                start(message)
            else:
                bot.send_message(message.chat.id , "|‼️|-مسیری برای انتخاب شما وجود ندارد لطفا دوباره انتخاب نمایید")
                del user_temp_data[user_id]['mbda']
                del user_temp_data[user_id]['magsd']
                del user_temp_data[user_id]['amrt']
                ppnoa223(message)
        elif javab == "خیر":
            bot.send_message(message.chat.id, "✅ دستور لشکرکشی لغو شد")
            del user_temp_data[user_id]
            start(message)
def aml(message):
    user_id = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    if message.text == "|⛏|-منابع اقتصادی":
        if user_id in dra:
            player_data = dra[user_id]
            darai = player_data['دارایی']
        
            for metod, datails in darai['tolidi'].items():
                markupt.add(f"{metod}")
            bot.send_message(message.chat.id, "|❓|-لطفا ساختمان مورد نظر را انتخاب کنید", reply_markup=markupt)
            bot.register_next_step_handler(message, ertega2)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
    elif message.text == "|🥣|-منابع غذایی":
        if user_id in dra:
            player_data = dra[user_id]
            darai = player_data['دارایی']
        
            for metod, datails in darai['منبع غذایی']['تولیدی'].items():
                markupt.add(f"{metod}")
            bot.send_message(message.chat.id, "|❓|-لطفا ساختمان مورد نظر را انتخاب کنید", reply_markup=markupt)
            bot.register_next_step_handler(message, ertegaghz2)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
def ertega2(message):
    user_id = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    player_data = dra[user_id]
    darai = player_data['دارایی']
    player_data['fa4'] = message.text
    msg = "موارد مورد نیاز برای ارتقا\n"
    for item, need in darai['tolidi'][message.text]['update']['nm'].items():
        ghz = need.get('tedad', 0)
        msg += f"{item} : {ghz}\n"
    msg += "آیا ارتقارا تایید میکنید؟"
    markupt.add("بله","خیر")
    bot.send_message(message.chat.id, msg, reply_markup=markupt)
    bot.register_next_step_handler(message, ertega)
def ertegaghz2(message):
    user_id = str(message.from_user.id)
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    player_data = dra[user_id]
    darai = player_data['دارایی']
    player_data['fa4'] = message.text
    msg = "موارد مورد نیاز برای ارتقا\n"
    for item, need in darai['منبع غذایی']['تولیدی'][message.text]['update']['nm'].items():
        ghz = need.get('tedad', 0)
        msg += f"{item} : {ghz}\n"
    msg += "آیا ارتقارا تایید میکنید؟"
    markupt.add("بله","خیر")
    bot.send_message(message.chat.id, msg, reply_markup=markupt)
    bot.register_next_step_handler(message, ertegaghz)
def ertegaghz(message):
    user_id = str(message.from_user.id)
    #skht = player_data['fa4']
    player_data = dra[user_id]
    darai = player_data['دارایی']
    can_upgrade = True
    if message.text == "بله":
        skht = player_data['fa4']  
        update_data = darai['منبع غذایی']['تولیدی'][skht]['update']['nm']
        resources = darai['megdar']
        for item, need in update_data.items():
            if item not in resources or resources[item]['مقدار'] < need['tedad']:
                can_upgrade = False
                break

        if can_upgrade:
            for item, need in update_data.items():
                resources[item]['مقدار'] -= need['tedad']
            bzup = darai['منبع غذایی']['تولیدی'][skht].get('bzup', 0)
            darai['منبع غذایی']['تولیدی'][skht]['لول'] += 1
            darai['منبع غذایی']['تولیدی'][skht]['بازدهی'] += bzup

            with open(DATA_FILE, 'w') as json_file:
                json.dump(dra, json_file, indent=4)
            bot.send_message(message.chat.id, f"|✅|-ساختمان {skht} با موفقیت ارتقا یافت!")
        else:
            bot.send_message(message.chat.id, "|‼️|-شما منابع کافی برای ارتقا ندارید.")
    else:  
        bot.send_message(message.chat.id, "|‼️|- ارتقا لغو شد")
    del player_data['fa4']
def ertega(message):
    user_id = str(message.from_user.id)
    player_data = dra[user_id]
    darai = player_data['دارایی']
    #skht = message.text
    if message.text == "بله":
        skht = player_data['fa4'] 
        if user_id not in dra:
            bot.send_message(message.chat.id, "|‼️|-شما پلیر نیستید!")
            start(message)
            return
        if skht not in darai['tolidi']:
            bot.send_message(message.chat.id, "|⚠️|-ساختمان وارد شده وجود ندارد.")
            start(message)
            return

        update_data = darai['tolidi'][skht]['update']['nm']
        resources = darai['megdar']
        can_upgrade = True

        for item, need in update_data.items():
            if item not in resources or resources[item]['مقدار'] < need['tedad']:
                can_upgrade = False
                break

        if can_upgrade:
            for item, need in update_data.items():
                resources[item]['مقدار'] -= need['tedad']
            bzup = darai['tolidi'][skht].get('bzup', 0)
            darai['tolidi'][skht]['لول'] += 1
            darai['tolidi'][skht]['بازدهی'] += bzup

            with open(DATA_FILE, 'w') as json_file:
                json.dump(dra, json_file, indent=4)
            bot.send_message(message.chat.id, f"|✅|-ساختمان {skht} با موفقیت ارتقا یافت!")
            start(message)
        else:
            bot.send_message(message.chat.id, "|‼️|-شما منابع کافی برای ارتقا ندارید.")
            start(message)
    else:  
        bot.send_message(message.chat.id, "|‼️|- ارتقا لغو شد")
    del player_data['fa4']
@bot.message_handler(commands=['afz'])
def afzodan(message):
    
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if not message.reply_to_message:
            bot.send_message(message.chat.id, "لطفاً به پیام کاربر مورد نظر پاسخ دهید.")
            return
        else:
            user_id = str(message.reply_to_message.from_user.id)
            
            markupt.add("|👤|-منابع انسانی", "|🥣|-منابع غذایی", "|⛏|-منابع اقتصادی")
            bot.send_message(message.chat.id, "|❓|-لطفا بخش مورد نظر را انتخاب نمایید", reply_markup=markupt)
            bot.register_next_step_handler(message, enttkhb)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
def enttkhb(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.text == "|⛏|-منابع اقتصادی":  
            bot.send_message(message.chat.id, 'اسم و لول و اندازه را وارد نمایید (فرمت: نام : مقدار لول: سطح)')
            bot.register_next_step_handler(message, afzd)
        elif message.text == "|🥣|-منابع غذایی":
            bot.send_message(message.chat.id, 'اسم و لول و اندازه را وارد نمایید (فرمت: نام : مقدار لول: سطح)')
            bot.register_next_step_handler(message, afzdgh)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید") 
def afzdgh(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if not message.reply_to_message:
            bot.send_message(message.chat.id, "لطفاً به پیام کاربر مورد نظر پاسخ دهید.")
            return

        user_id = str(message.reply_to_message.from_user.id)
        pattern = r"^(.*) : (\d+) (.+) لول: (\d+)\n(.*) : (\d+)\n(.*) : (\d+)\n(.*) : (\d+)\n(\d+)$"
        match = re.search(pattern, message.text)

        if match:
            skht = match.group(1).strip()
            tda = int(match.group(2))
            nao = match.group(3).strip()
            lvl = int(match.group(4))
            ert1 = match.group(5).strip()
            tda1 = int(match.group(6))
            ert2 = match.group(7).strip()
            tda2 = int(match.group(8))
            ert3 = match.group(9).strip()
            tda3 = int(match.group(10))
            bzp = int(match.group(11))
            if user_id not in dra:
                bot.send_message(message.chat.id, "این کاربر هنوز به عنوان پلیر اضافه نشده است.")
                afzdgh(message)

            dra[user_id]['دارایی']['منبع غذایی']['تولیدی'][skht] = {
                'لول': lvl,
                'بازدهی': tda,
                'نوع': nao,
                'bzup': bzp,
                'update': {
                    'nm': {
                        ert1: {'tedad': tda1},
                        ert2: {'tedad': tda2},
                        ert3: {'tedad': tda3}
                    }
                }
            }

            if nao not in dra[user_id]['دارایی']['منبع غذایی']['غذاها']:
                dra[user_id]['دارایی']['منبع غذایی']['غذاها'][nao] = {'مقدار': 0}

            with open(DATA_FILE, 'w') as json_file:
                json.dump(dra, json_file, indent=4)

            bot.send_message(message.chat.id, f'ساختمان {skht} با لول {lvl} و بازدهی {tda} از نوع {nao} اضافه شد!')
        else:
            bot.send_message(message.chat.id, "فرمت ورودی نادرست است. لطفاً دوباره امتحان کنید. \nفرمت صحیح: نام : مقدار نوع لول: سطح")
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")   
def afzd(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if not message.reply_to_message:
            bot.send_message(message.chat.id, "لطفاً به پیام کاربر مورد نظر پاسخ دهید.")
            return

        user_id = str(message.reply_to_message.from_user.id)
        pattern = r"^(.*) : (\d+) (.+) لول: (\d+)\n(.*) : (\d+)\n(.*) : (\d+)\n(.*) : (\d+)\n(\d+)$"
        match = re.search(pattern, message.text)

        if match:
            skht = match.group(1).strip()
            tda = int(match.group(2))
            nao = match.group(3).strip()
            lvl = int(match.group(4))
            ert1 = match.group(5).strip()
            tda1 = int(match.group(6))
            ert2 = match.group(7).strip()
            tda2 = int(match.group(8))
            ert3 = match.group(9).strip()
            tda3 = int(match.group(10))
            bzp = int(match.group(11))
            if user_id not in dra:
                bot.send_message(message.chat.id, "این کاربر هنوز به عنوان پلیر اضافه نشده است.")
                return

            # بررسی و ساخت ساختار مورد نیاز
            if 'دارایی' not in dra[user_id]:
                dra[user_id]['دارایی'] = {}

            if 'tolidi' not in dra[user_id]['دارایی']:
                dra[user_id]['دارایی']['tolidi'] = {}

            dra[user_id]['دارایی']['tolidi'][skht] = {
                'لول': lvl,
                'بازدهی': tda,
                'نوع': nao,
                'bzup': bzp,
                'update': {
                    'nm': {
                        ert1: {'tedad': tda1},
                        ert2: {'tedad': tda2},
                        ert3: {'tedad': tda3}
                    }
                }
            }

            if 'megdar' not in dra[user_id]['دارایی']:
                dra[user_id]['دارایی']['megdar'] = {}

            if nao not in dra[user_id]['دارایی']['megdar']:
                dra[user_id]['دارایی']['megdar'][nao] = {'مقدار': 0}

            with open(DATA_FILE, 'w') as json_file:
                json.dump(dra, json_file, indent=4)

            bot.send_message(message.chat.id, f'ساختمان {skht} با لول {lvl} و بازدهی {tda} از نوع {nao} اضافه شد!')
        else:
            bot.send_message(message.chat.id, "فرمت ورودی نادرست است. لطفاً دوباره امتحان کنید. \nفرمت صحیح: نام : مقدار نوع لول: سطح")
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید") 
@bot.message_handler(commands=['tft'])
def tft(message):
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    user_id = message.from_user.id
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    if user_id in adl:
        bot.send_message(message.chat.id, "لطفا گروه و تلفات مورد نظر را وارد نمایید")
        bot.register_next_step_handler(message, tft2)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
def tft2(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.text == "اتمام":
            bot.send_message(message.chat.id, "✅عملیات ثبت تلفات به اتمام رسید") 
        elif message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            pattern = r"^(.*) : (\d+)$"
            match = re.search(pattern, message.text)
            if match:
                mrd = match.group(1).strip()
                tda = int(match.group(2))
                dra[user_id]['دارایی']['منابع انسانی']['نیروی انسانی'][mrd]['mgd'] -= tda
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, "✅اعمال تلفات با موفقیت انجام شد") 
                tft(message)
            else:
                bot.send_message(message.chat.id, "فرمت ورودی نادرست است. لطفاً دوباره امتحان کنید.") 
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
            tft(message)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید") 
@bot.message_handler(commands=['afmnb'])
def afmnb(message):
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    user_id = message.from_user.id
    markupt = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    if user_id in adl:
        markupt.add("|👤|-منابع انسانی", "|🥣|-منابع غذایی", "|⛏|-منابع اقتصادی")
        bot.send_message(message.chat.id, "|❓|-لطفا بخش مورد نظر را انتخاب نمایید", reply_markup=markupt)
        bot.register_next_step_handler(message, afmnb2)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
def afmnb2(message):
    if message.text == "|⛏|-منابع اقتصادی":
       bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
       bot.register_next_step_handler(message, afmnbmg)
    elif message.text == "|🥣|-منابع غذایی":
       bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید")
       bot.register_next_step_handler(message, amnbgh) 
    elif message.text == "|👤|-منابع انسانی":
       bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید")
       bot.register_next_step_handler(message, amnbsn)  
def afmnbmg(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.text == "اتمام":
            bot.send_message(message.chat.id, "✅عملیات ثبت آیتم به اتمام رسید") 
        elif message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            pattern = r"^(.*) : (\d+)$"
            match = re.search(pattern, message.text)
            if match:
                mnb = match.group(1).strip()
                tda = int(match.group(2))
                if mnb in dra[user_id]['دارایی']['megdar']:
                    dra[user_id]['دارایی']['megdar'][mnb]['مقدار'] += tda
                else :
                    dra[user_id]['دارایی']['megdar'][mnb] ={'مقدار': tda}
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, f"✅{tda}{mnb} به دارایی اضافه شد") 
                bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
                bot.register_next_step_handler(message, afmnbmg)
            else:
                bot.send_message(message.chat.id, "فرمت ورودی نادرست است. لطفاً دوباره امتحان کنید.")
                bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
                bot.register_next_step_handler(message, afmnbmg) 
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
            bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
            bot.register_next_step_handler(message, afmnbmg)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید") 
def amnbgh(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.text == "اتمام":
            bot.send_message(message.chat.id, "✅عملیات ثبت آیتم به اتمام رسید") 
        elif message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            pattern = r"^(.*) : (\d+)$"
            match = re.search(pattern, message.text)
            if match:
                mnb = match.group(1).strip()
                tda = int(match.group(2))
                if mnb in dra[user_id]['دارایی']['منبع غذایی']['غذاها']:
                    dra[user_id]['دارایی']['منبع غذایی']['غذاها'][mnb]['مقدار'] += tda
                else :
                    dra[user_id]['دارایی']['منبع غذایی']['غذاها'][mnb] ={'مقدار': tda}
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, f"✅{tda}{mnb} به دارایی اضافه شد") 
                bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
                bot.register_next_step_handler(message, amnbgh)
            else:
                bot.send_message(message.chat.id, "فرمت ورودی نادرست است. لطفاً دوباره امتحان کنید.")
                bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
                bot.register_next_step_handler(message, amnbgh) 
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
            bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
            bot.register_next_step_handler(message, amnbgh)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید") 
def amnbsn(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.text == "اتمام":
            bot.send_message(message.chat.id, "✅عملیات ثبت آیتم به اتمام رسید") 
        elif message.reply_to_message:
            user_id = str(message.reply_to_message.from_user.id)
            pattern = r"^(.*) : (\d+) (\d+)$"
            match = re.search(pattern, message.text)
            if match:
                mnb = match.group(1).strip()
                tda = int(match.group(2))
                tda2 = int(match.group(3))
                if mnb in dra[user_id]['دارایی']['منابع انسانی']['نیروی انسانی']:
                    dra[user_id]['دارایی']['منابع انسانی']['نیروی انسانی'][mnb]['mgd'] += tda
                    dra[user_id]['دارایی']['منابع انسانی']['نیروی انسانی'][mnb]['msr'] += tda2
                else :
                    dra[user_id]['دارایی']['منابع انسانی']['نیروی انسانی'][mnb] ={'mgd': tda}
                    dra[user_id]['دارایی']['منابع انسانی']['نیروی انسانی'][mnb] ={'msr': tda2}
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, f"✅{tda}{mnb} به دارایی اضافه شد") 
                bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
                bot.register_next_step_handler(message, amnbsn)
            else:
                bot.send_message(message.chat.id, "فرمت ورودی نادرست است. لطفاً دوباره امتحان کنید.")
                bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
                bot.register_next_step_handler(message, amnbsn) 
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
            bot.send_message(message.chat.id, "|❓|-نام و مقدار  آیتم مورد نظر را وارد نمایید") 
            bot.register_next_step_handler(message, amnbsn)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید") 
@bot.message_handler(commands=['ambhf'])
def ambh(message):
    user_id = message.from_user.id
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id in adl:
        bot.send_message(message.chat.id, "|❓|-لطفا روی پلیر مورد نظر ریپلای نموده و دستور را وارد کنید") 
        bot.register_next_step_handler(message, amnbsn2)
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
def amnbsn2(message):
    if message.text == "لغو":
        bot.send_message(message.chat.id, "|‼️|-عملیات لغو شد")
    elif message.reply_to_message:
        user_id = str(message.reply_to_message.from_user.id)
        player_data = dra[user_id]
        darai = player_data['دارایی']
        pattern = r"^(.*) (\d+)$"
        match = re.search(pattern, message.text)
        if match:
            mnb = match.group(1).strip()
            tda = int(match.group(2))
            if mnb == "افزایش":
                player_data['mhb'] += tda
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, f"✅محبوبیت {tda}واحد افزایش یافت") 
            elif mnb == "کاهش":
                player_data['mhb'] -= tda
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                bot.send_message(message.chat.id, f"✅محبوبیت {tda}واحد کاهش یافت") 
    else:
        bot.send_message(message.chat.id, "|‼️|-عملیات لغو شد")
@bot.message_handler(commands=['del'])
def up(message):
    user_id2 = message.from_user.id
    
    admins = bot.get_chat_administrators(message.chat.id)
    adl = []
    for admin in admins:
            adl.append(admin.user.id)
    if user_id2 in adl:
        if message.reply_to_message:
           user_id = str(message.reply_to_message.from_user.id)
           if user_id in dra:
                del dra[user_id]
                with open(DATA_FILE, 'w') as json_file:
                    json.dump(dra, json_file, indent=4)
                    bot.send_message(message.chat.id, "اطلاعات پلیر حذف شد")
           else:  
                bot.send_message(message.chat.id, "|‼️|-این شخص پلیر نیست")
        else:
            bot.send_message(message.chat.id, "لطفاً به یک پیام پاسخ دهید.")
    else:
        bot.send_message(message.chat.id, "|‼️|-شما ادمین نیستید")
bot.set_my_commands([
    telebot.types.BotCommand("start", "استفاده از ربات"),
    telebot.types.BotCommand("up", "به روز رسانی دارایی"),
    telebot.types.BotCommand("darai", "مشاهده دارایی"),
    telebot.types.BotCommand("afz",  "افزودن منابع" ),
    telebot.types.BotCommand("del", "حذف پلیر"),
    telebot.types.BotCommand("tft", "اعمال تلفات"),
    telebot.types.BotCommand("ambhf", "تغییر محبوبیت"),
    telebot.types.BotCommand("afmnb", "افزودن آیتم به دارایی"),
    telebot.types.BotCommand("add_player", "افزودن پلیر")
], scope=BotCommandScopeAllGroupChats())

if __name__ == '__main__':
    bot.polling()