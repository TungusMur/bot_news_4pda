from aiogram import Bot, Dispatcher, executor, types
import asyncio


import config
import parse
import setting_off_on


BOT = Bot(config.token)
DP = Dispatcher(BOT)


chek_ready = False


off_on = {
    'all': "Вкл",
    'phone': "Выкл",
    'laptop': "Выкл",
    'audio': "Выкл",
    'display': "Выкл",
    'pc': "Выкл",
    'games': "Выкл"
}



@DP.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global user_id, new_item_id
    user_id = message.from_user.id
    name_user = message.from_user.username
    print(user_id)
    await BOT.send_message(user_id, f"-Добро пожаловать, {name_user}, это бот новостей посвящен сайта 4pda."
                                    "\n\n-Тут публикуютя новости таких тематик как: "
                                    "новости о играх, новости о технике(смартфонах, ПК, аудиотехние и т. д.) "
                                    "и тому подобное. "
                                    "\n\n-Чтобы начать получать новости по все темаматикам введите команду /go."
                                    "\n\n-Чтобы по подробней узнать о всех командах бота введите команду /help.")



@DP.message_handler(commands=['help'])
async def help_command(message):
    global user_id
    user_id = message.from_user.id
    await BOT.send_message(user_id,"\u2022/setting - настройка фильтрации, получаемых новостей"
                                   "\n\n\u2022/help - помощь в изучении основных команд бота"
                                   "\n\n\u2022/go - команда для начала получения потока новостей"
                                   "\n\n\u2022/stop - команда для приостановления потока новостей")



@DP.message_handler(commands=['go'])
async def go_command(message):
    global user_id, chek_ready, off_on
    user_id = message.from_user.id
    if(chek_ready):
        await BOT.send_message(user_id, "Вы уже получаете новости.")
    else:
        if ((off_on['all'] == 'Выкл') and (off_on['games'] == 'Выкл') and (off_on['laptop'] == 'Выкл') and
            (off_on['audio'] == 'Выкл') and (off_on['display'] == 'Выкл') and (off_on['pc'] == 'Выкл') and
            (off_on['games'] == 'Выкл')):
            off_on['all'] = 'Вкл'
        chek_ready = True
        await BOT.send_message(user_id, "Вы успешно начали получать новости.")
        for news in off_on:
            inf = parse.chek_off_on(news, off_on[news])
            if ((inf[4] != 0) and (parse.chek(inf[4], news))):
                await BOT.send_photo(user_id, photo=inf[0], caption=f"{inf[1]}\n\n{inf[2]}\n\n{inf[3]}",
                                     disable_notification=True)
        DP.loop.create_task(renewal(150))



@DP.message_handler(commands=['stop'])
async def stop_command(message):
    global user_id, chek_ready
    user_id = message.from_user.id
    if (chek_ready):
        chek_ready = False
        await BOT.send_message(user_id, "Вы приостановили поток получения новостей.")
    else:
        await BOT.send_message(user_id, "У вас итак приостановлен поток получения новостей.")



@DP.message_handler(commands=['setting'])
async def setting_command(message):
    global user_id, off_on
    if(chek_ready):
        await BOT.send_message(user_id,"Перед тем как перейти к настройкам приостоновте поток новостей командой /stop."
                                       "\nПосле настройки фильтрации новостей не забудьте прописать/go")
    else:
        user_id = message.from_user.id
        await BOT.send_message(user_id, f"Настройка фильтра новостей:"
                                        f"\n\n\u2022/all_news - получать все новости |{off_on['all']}|"
                                        f"\n\n\u2022/phone_news - получать новости о смартфонах|{off_on['phone']}|"
                                        f"\n\n\u2022/laptop_news - получать новости о ноутбуках |{off_on['laptop']}|"
                                        f"\n\n\u2022/audio_news - получать новости о аудиотехнике |{off_on['audio']}|"
                                        f"\n\n\u2022/display_news - получать новости о ТВ и мониторах |{off_on['display']}|"
                                        f"\n\n\u2022/pc_news - получать новости о ПК |{off_on['pc']}|"
                                        f"\n\n\u2022/games_news - получать новости о играх |{off_on['games']}|"
                                        "\n\n- Повторный вызов команды отключит поток новостей, который вы указали"
                                        "\n\n- Если вы включите все команды кроме /all_news, то это будет рассмативаться как команда /all_news"
                                        "\n\n- Если вы отключите все виды новостей, то это будет рассмативаться как команда /stop"
                                        "\n\n- После настройки фильтра не забудьте прописать команду /go")



@DP.message_handler(content_types=['text'])
async def text(message):
    global off_on, chek_ready
    if ((message.text.lower() == "/all_news") or (message.text.lower() == "/phone_news") or
        (message.text.lower() == "/laptop_news") or (message.text.lower() == "/audio_news") or
        (message.text.lower() == "/display_news") or (message.text.lower() == "/pc_news") or
        (message.text.lower() == "/games_news")):
            off_on = setting_off_on.setting(off_on, message.text.lower())
            if((off_on['all'] == 'Выкл') and (off_on['games'] == 'Выкл') and (off_on['laptop'] == 'Выкл') and
                (off_on['audio'] == 'Выкл') and (off_on['display'] == 'Выкл') and (off_on['pc'] == 'Выкл') and
                (off_on['games'] == 'Выкл')):
                    chek_ready = False
            await BOT.send_message(user_id, f"Настройка фильтра новостей:"
                                            f"\n\n\u2022/all_news - получать все новости |{off_on['all']}|"
                                            f"\n\n\u2022/phone_news - получать новости о смартфонах|{off_on['phone']}|"
                                            f"\n\n\u2022/laptop_news - получать новости о ноутбуках |{off_on['laptop']}|"
                                            f"\n\n\u2022/audio_news - получать новости о аудиотехнике |{off_on['audio']}|"
                                            f"\n\n\u2022/display_news - получать новости о ТВ и мониторах |{off_on['display']}|"
                                            f"\n\n\u2022/pc_news - получать новости о ПК |{off_on['pc']}|"
                                            f"\n\n\u2022/games_news - получать новости о играх |{off_on['games']}|"
                                            "\n\n- Повторный вызов команды отключит поток новостей, который вы указали"
                                            "\n\n- Если вы включите все виды новостей кроме /all_news, то это будет рассмативаться как команда /all_news"
                                            "\n\n- Если вы отключите все виды новостей, то это будет рассмативаться как команда /stop"
                                            "\n\n- После настройки фильтра не забудьте прописать команду /go")



async def renewal(time):
    global chek_ready
    while chek_ready:
            await asyncio.sleep(time)
            if (chek_ready == False):
                break
            for news in off_on:
                inf = parse.chek_off_on(news, off_on[news])
                if ((inf[4] != 0) and (parse.chek(inf[4], news))):
                    await BOT.send_photo(user_id, photo=inf[0], caption=f"{inf[1]}\n\n{inf[2]}\n\n{inf[3]}",
                                    disable_notification = True)



if __name__ == '__main__':
    executor.start_polling(DP, skip_updates=True)