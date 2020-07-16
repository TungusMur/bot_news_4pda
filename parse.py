import requests
from bs4 import BeautifulSoup as BS

# Метод для получения информации о новости 
def get_inf(URL):
        global item_id
        HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                'accept': '*/*'}

        r = requests.get(URL, headers=HEADERS)
        soup = BS(r.text, 'html.parser')
        for item in soup.select(".post"):
                title = item.attrs['itemid']
                if(len(title) != 7):
                        item_id = title
                        break

        text = soup.find('article', class_="post", itemid=item_id).find('div', class_='description').find('p').get_text()
        header = soup.find('article', class_="post", itemid=item_id).find('div', class_='description').find('span', itemprop='name').get_text()
        img = 'https:' + soup.find('article', class_="post", itemid=item_id).find('img', itemprop='image').get('src')
        url = 'https:' + soup.find('article', class_="post", itemid=item_id).find('div', class_='description').find('a', rel='bookmark').get('href')
        print(item_id + 'новый id')
        return [img, header, text, url, item_id]

# Метод для проверки новой новости на сайте 
def chek(new_item_id, news):
    file = open('name_id\\' + news + '_id.txt', 'r')
    old_item_id = file.readline()
    print(old_item_id)
    if (old_item_id == new_item_id):
        file.close()
        return False
    else:
        file.close()
        file = open('name_id\\' + news + '_id.txt', 'w')
        file.write(new_item_id)
        file.close()
        return True

# Метод для просмотра фильтра
def chek_off_on(news, status):
    if ((news == 'all') and (status == 'Вкл')):
        URL = 'https://4pda.ru/'
        inf = get_inf(URL)
        return inf
    elif ((news == 'phone') and (status == 'Вкл')):
        URL = 'https://4pda.ru/tag/smartphones/'
        inf = get_inf(URL)
        return inf
    elif ((news == 'laptop') and (status == 'Вкл')):
        URL = 'https://4pda.ru/tag/notebooks/'
        inf = get_inf(URL)
        return inf
    elif ((news == 'audio') and (status == 'Вкл')):
        URL = 'https://4pda.ru/tag/audio/'
        inf = get_inf(URL)
        return inf
    elif ((news == 'display') and (status == 'Вкл')):
        URL = 'https://4pda.ru/tag/monitors/'
        inf = get_inf(URL)
        return inf
    elif ((news == 'pc') and (status == 'Вкл')):
        URL = 'https://4pda.ru/tag/pc/'
        inf = get_inf(URL)
        return inf
    elif ((news == 'games') and (status == 'Вкл')):
        URL = 'https://4pda.ru/games/'
        inf = get_inf(URL)
        return inf
    else:
        return [0, 0, 0, 0, 0]
