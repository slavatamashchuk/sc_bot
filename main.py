import telebot
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
ds = commands.Bot(command_prefix="/", intents=intents)

@ds.command()
async def ping(ctx):
    await ctx.send('pong')


ds.run("******")
tg = telebot.TeleBot("*****")


@tg.message_handler(commands=["start"])
def start(message):
    tg.send_message(message.chat.id, "Slavcraft бот ввімкнений. Для допомоги у боті напишіть /help.")


@tg.message_handler(commands=["help"])
def start(message):
    tg.send_message(message.chat.id, """/start – уввімкнути бота.
/help – допомога у боті.
/about – інформація про бота.
/credits – творці бота.
/rules – правила Славкрафту.
/ip – ip Славкрафту.
/members. – лист усіх учасників СК.""")


@tg.message_handler(commands=["about"])
def start(message):
    tg.send_message(message.chat.id, "Цей бот того шоб у учасників Славкрафту був швидкий доступ до інформації.")


@tg.message_handler(commands=["credits"])
def start(message):
    tg.send_message(message.chat.id, "Цей бот створений slavchik'ом.")


@tg.message_handler(commands=["rules"])
def start(message):
    tg.send_message(message.chat.id, """Правила Славкрафту:


загальні

1. Неможно ображати.
2. Неможно спамити.
3. Неможно добавляти гравців в групу у Телеграмі чи сервер у Діскорді та на сервер у Майнкрафті без дозволу slavchik.
4. Запрещена проросійська діяльність.
5. Запрещена комуністична діяльність.
6. Запрещена нацистская/фашистская діяльність.
7. Ваш RP ні повинен нікому заважати.

Майнкрафт

1. Неможно гриферити.
2. Неможно красти.
3. Неможно будувати лаг машини.
4. Неможно пвпшиться без дозволу всіх участников пвп.
5. Не чятрепортети інших гравців.

creative-21

1. 25 блоків від спавна у звичайному світі не можуть нікому належати.
1. 25 блоків від координат 0, 0 у звичайному світі не можуть нікому належати.
3. 25 блоків від координат 0, 0 у пеклі не можуть нікому належати.
4. 25 блоків від координат 0, 0 в ендер світі не можуть нікому належати.
5. 25 блоків від обсідеаневої платформи де ми спавнемося у ендер світі не можуть нікому належати.

creative-18
1. 25 блоків від спавна у звичайному світі не можуть нікому належати.
2. 25 блоків від координат 0, 0 у звичайному світі не можуть нікому належати.
3. 25 блоків від координат 0, 0 у пеклі не можуть нікому належати.
4. 250 блоків від координат 0, 0 в ендер світі не можуть нікому належати.

Slavcraft 4

1. 25 блоків від спавна у звичайному світі не можуть нікому належати.
2. 25 блоків від координат 0, 0 у звичайному світі не можуть нікому належати.
3. 25 блоків від координат 0, 0 у пеклі не можуть нікому належати.
4. 250 блоків від координат 0, 0 в ендер світі не можуть нікому належати.
5. яйцо дракона не може нікому належати.""")


@tg.message_handler(commands=["ip"])
def start(message):
    tg.send_message(message.chat.id, """IP Славкрафту:

Лоббі: slavcraft.somerandom.xyz
creative-21: slavcraft.somerandom.xyz:25566
creative-18: slavcraft.somerandom.xyz:25567""")


@tg.message_handler(commands=["members"])
def start(message):
    tg.send_message(message.chat.id, """Лист всіх учасників Славкрафту:

1. slavchik
2. TEBSS
3. Savalio
4. salad_1939
5. MarkoAntonio11
6. joker497535
7. NancyCat1
8. 11_ArtemPR_22
9. Pla3ma
10. BLANK_est
11. Rich_The_Dog""")


tg.polling(none_stop=True)
