# bot_news_4pda
<h3> Предназначение бота </h3>
<p>Бот отправляет новости пользователям (пока код преднозначен для одного пользователя) с 4Pda.</p>

<h3>Функции бота:</h3>
<ol>
  <li>Бот принимает и отправляет сообщения из Telegram.</li>
  <li>Отправляет новости с сайта 4Pda.ru (А именно: заголов новости, краткое описание вместе с изображением).</li>
  <li>Бот предоставляет настройку фильтра новостей.</li>
  <li>Есть возможность приостановить  и возобновить прием новостей.</li>
</ol>

<h3>Требования:</h3>
<ol>
  <li>Необходим установленный python версии 3.8 или версии новей</li>
  <li>Токен для Telegram Bot API</li>
</ol>

<h3>Установка:</h3>
<ol>
  <li>Для начала необходимо получить token для Telegram Bot API. Как его получить можно ознакомиться здесь.</li>
  <li>После того, как вы получили бота можете его скачивать.  
    <pre>git clone https://github.com/TungusMur/bot_news_4pda</pre>
  </li>
  <li>Зайдите в папку с ботом:
    <pre>cd bot_news_4pda</pre>  
  </li>
  <li>Загрузите модули:
    <pre>pip install -r requirements.txt</pre>  
  </li>
  <li>После установки открываем и заполняем config.py:
    <pre>token = "Ваш токен бота"</pre>
  </li>
  <li>
    Запускаем, как обычно, командой python main.py
  </li>
</ol>
<h3>Доступные команды бота:</h3>
<pre>
  <code>• /setting - настройка фильтрации, получаемых новостей
  • /help - помощь в изучении основных команд бота
  • /go - команда для начала получения потока новостей
  • /stop - команда для приостановления потока новостей</code>
</pre>
<h3>Примечание:</h3>
  <p>На данный момент бот только для одного пользователя, так что в дальнейшем будет добавлена БД, для многопользовательского использования.</p>

