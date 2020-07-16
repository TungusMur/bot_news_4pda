#Метод для настройки фильтра
def setting(off_on, message):
    if (message == "/all_news"):
        if (off_on['all'] == 'Вкл'):
            off_on['all'] = 'Выкл'
        elif (off_on['all'] == 'Выкл'):
            for news in off_on:
                off_on[news] = 'Выкл'
            off_on['all'] = 'Вкл'

    elif (message == "/phone_news"):
        if (off_on['phone'] == 'Вкл'):
            off_on['phone'] = 'Выкл'
        else:
            off_on['phone'] = 'Вкл'
            off_on['all'] = 'Выкл'

    elif (message == "/laptop_news"):
        if (off_on['laptop'] == 'Вкл'):
            off_on['laptop'] = 'Выкл'
        else:
            off_on['laptop'] = 'Вкл'
            off_on['all'] = 'Выкл'

    elif (message == "/audio_news"):
        if (off_on['audio'] == 'Вкл'):
            off_on['audio'] = 'Выкл'
        else:
            off_on['audio'] = 'Вкл'
            off_on['all'] = 'Выкл'

    elif (message == "/display_news"):
        if (off_on['display'] == 'Вкл'):
            off_on['display'] = 'Выкл'
        else:
            off_on['display'] = 'Вкл'
            off_on['all'] = 'Выкл'

    elif (message == "/pc_news"):
        if (off_on['pc'] == 'Вкл'):
            off_on['pc'] = 'Выкл'
        else:
            off_on['pc'] = 'Вкл'
            off_on['all'] = 'Выкл'

    elif (message == "/games_news"):
        if (off_on['games'] == 'Вкл'):
            off_on['games'] = 'Выкл'
        else:
            off_on['games'] = 'Вкл'
            off_on['all'] = 'Выкл'

    if ((off_on['games'] == 'Вкл') and (off_on['laptop'] == 'Вкл') and (off_on['audio'] == 'Вкл') and
        (off_on['display'] == 'Вкл') and (off_on['pc'] == 'Вкл') and (off_on['games'] == 'Вкл')):
            for news in off_on:
                off_on[news] = 'Выкл'
            off_on['all'] = 'Вкл'
    return off_on
