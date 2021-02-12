import datetime
import dateutil
import requests
import telebot
import dateutil
from dateutil import parser


bot = telebot.TeleBot('telegramm api key')

massivepogodi = []
city_name = "Novosibirsk (RU)"
city_id = 1496747
API_key = 'openweather api key'
s_city = 0
lat = '54.862351'
lon = '82.995247'
a = datetime.datetime.today().strftime("%Y.%m.%d %H:%M:%S")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'lat': lat,
                           'lon': lon,
                           'units': 'metric',
                           'lang': 'ru',
                           'APPID': API_key})
print(res.request.url)
data = res.json()
for i in data['list']:
    words = str((i['dt_txt'],
                 '{0:+3.0f}'.format(i['main']['temp']),
                 i['weather'][0]['description']))
    massivepogodi.append(words)




@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет , посмотри /help')
    bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.reply_to(message,
                 f'Я умею показывать погоду около вашего дома! \n'
                 f' 1.Введите слово "погода". \n'
                 f' Что то еще {message.from_user.first_name} ?')


@bot.message_handler(commands=['weather'])
def start_messagess(message):
    bot.reply_to(message, f'Уже начал искать')
    for i in massivepogodi:

        # print(i)
        izm = i.replace('(', '').replace(')', '').replace(',', ' ').replace("'", "").split()
        izm2 = izm[0] + ' ' + izm[1] + ' ' + izm[2] + ' ' + izm[3].replace('небольшой', 'небольшой снегопадик') + ' '
        truedate = izm[0] + ' ' + izm[1]
        timevremia = izm2.split()[1]
        timedata = izm2.split()[0]
        parsed1 = dateutil.parser.parse(timedata + ' ' + timevremia)
        # print(parsed1)

        if parsed1 > dateutil.parser.parse(a):  ##>= если нужна дикая точность до часа
            if int(izm[2]) <= -30:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRmWAl9yKH90SPqRLLsyjE6pcYD7J6AAIGAANIODcYVHEZ3KEzBWQeBA')
            elif int(izm[2]) < -25:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRpWAl9yu3DfxMy4vKukHyByLi2qhwAAIcAANIODcYSGbhohJtpLYeBA')
            elif int(izm[2]) < -20:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRnGAl9yOe5wABOQvGlNtWEVGynsbyAwACCQADSDg3GMJ7f7AwNo-uHgQ')
            elif int(izm[2]) < -15:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRn2Al9yciPulg1buFxpobxyBaGoqiAAITAANIODcY5vToWlUaNZweBA')
            elif int(izm[2]) < -10:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRomAl9ym7laeByvFZ6eGPbtYWDv1aAAIYAANIODcYDMKPas2WF1oeBA')
            elif int(izm[2]) < -5:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRqGAl9y_LkzrRS_yGyzUHeyLv94BXAAIfAANIODcYAAHuybYauMQ0HgQ')
            elif int(izm[2]) < -0:
                print('holod')
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALRq2Al9zdsSOazmQLZSo25SpccspgJAAJAAANIODcYuIi8lbr1OWAeBA')
            print(izm2, ' > 12')
            bot.send_message(message.from_user.id, izm2)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'погода':
        bot.send_message(message.from_user.id, 'Посмотрим погодку ? /weather')



    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
