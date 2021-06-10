from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from answers import *
from db import get_user, get_posts, get_all_posts
from config import vk,trading_group_link

index_btn = InlineKeyboardButton("↪️ Вернуться", callback_data="index")

def return_akcii():
    key = InlineKeyboardMarkup()
    but7 = InlineKeyboardButton(text='↪️ Вернуться', callback_data='return_akcii')
    key.add(but7)
    return key

def return_about():
    key = InlineKeyboardMarkup()
    but7 = InlineKeyboardButton(text='↪️ Вернуться', callback_data='return_about')
    key.add(but7)
    return key

def return_about_and_help():
    key = InlineKeyboardMarkup()
    but6 = InlineKeyboardButton(text='▪Поддержка пользователей▪️', url='t.me/bkrtboss')
    but7 = InlineKeyboardButton(text='↪️ Вернуться', callback_data='return_about')
    key.add(but6)
    key.add(but7)
    return key


ADMINS = [445116305, 516703737, 669917374, 697342273]

def training():
    key = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text='▪Подписаться на канал▪', url='https://t.me/bkrtfree')
    but2 = InlineKeyboardButton(text='▪Навигация на канале▪', callback_data="navigate")
    key.add(but1)
    key.add(but2)
    key.add(index_btn)
    return key

def navigate():
    navigate_btns = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text='Обратная связь в топике группы ВК',url=vk)
    but2 = InlineKeyboardButton(text='Мы в соцсетях', callback_data='network')
    navigate_btns.add(but1)
    navigate_btns.add(but2)
    navigate_btns.add(index_btn)
    return navigate_btns

def about():
    key = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text='О нас📓', callback_data='about_us')
    but2 = InlineKeyboardButton(text='Реклама📝', callback_data='ads')
    but3 = InlineKeyboardButton(text='Тренинги🎯', callback_data='trening')
    but4 = InlineKeyboardButton(text='Онлайн консультации📲', callback_data='consult')
    but5 = InlineKeyboardButton(text='🔸Поддержка пользователей🔸', url='t.me/bkrtboss')
    key.add(but1)
    key.add(but2)
    key.add(but3)
    key.add(but4)
    key.add(but5)
    key.add(index_btn)
    return key

def akcii(message):
    key = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text='🔹Добавить пользователя🔹', callback_data='add_sb')
    but2 = InlineKeyboardButton(text='🔹Дни за подписку🔹', callback_data='day_of_sub')
    but3 = InlineKeyboardButton(text='🔹Кешбек за подписку🔹', callback_data='cashback')
    but4 = InlineKeyboardButton(text='🔹Реклама нашего бота в ВК🔹', callback_data='ad_in_vk')
    but5 = InlineKeyboardButton(text='🔹Реклама нашего бота в Инсте🔹', callback_data='ad_in_insta')
    but6 = InlineKeyboardButton(text='🔹Приведи друга🔹', callback_data='invite_friends')
    but7 = InlineKeyboardButton(text='🔹Формуляр с акциями🔹', url='https://yadi.sk/i/k1aMYs9idbpS3w')
    if message in ADMINS:
        key.add(but1)
    key.add(but2)
    key.add(but3)
    key.add(but4)
    key.add(but5)
    key.add(but6)
    key.add(but7)
    key.add(index_btn)
    return key

def add_media_key():
    key = InlineKeyboardMarkup(row_width=1)

    add_imgur = InlineKeyboardButton(text="🖼 Добавить картинку", callback_data="add_imgur")
    add_gif = InlineKeyboardButton(text="🖼 Добавить GIF", callback_data="add_gif")
    y_add_btn = InlineKeyboardButton(text="Добавить изображения/документы", callback_data="add_media")
    no_add_btn = InlineKeyboardButton(text="Перейти далее ➡️", callback_data="next_step")

    key.add(add_imgur, add_gif,y_add_btn, no_add_btn)
    return key


def add_image_key():
    key = InlineKeyboardMarkup(row_width=1)
    y_add_btn = InlineKeyboardButton(text="🖼 Добавить изображение/документ", callback_data="add_media")
    no_add_btn = InlineKeyboardButton(text="Перейти далее ➡️", callback_data="next_step")

    key.add(y_add_btn, no_add_btn)
    return key


def mailing_btn():
    key = InlineKeyboardMarkup(row_width=1)

    key.add(InlineKeyboardButton("✉️ Рассылка", callback_data="mailing"),
            InlineKeyboardButton("📤 Все посты", callback_data="all_posts"))
    return key


def return_btn():
    key = InlineKeyboardMarkup()

    key.add(index_btn)
    return key


def periodicity_markup():
    key = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    key.add("Сегодня", "Ежедневный")
    key.add("Еженедельный", "Ежемесячный")
    return key


def cancel_markup():
    key = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    cancel_btn = KeyboardButton(text='↩️ Отмена')

    key.add(cancel_btn)
    return key



def return_markup():
    key = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    cancel_btn = KeyboardButton(text='↩️ Вернуться')

    key.add(cancel_btn)
    return key


def check_pay_key():
    key = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    check_payment = KeyboardButton(text='Проверить оплату')
    cancel_btn = KeyboardButton('Вернуться')
    key.add(check_payment)
    key.add(cancel_btn)
    return key


def payment_key(price, payment_link):
    key = InlineKeyboardMarkup()

    pay_btn = InlineKeyboardButton(text=f"Оплатить {price}(free-kassa)", url=payment_link)
    plans = InlineKeyboardButton("Выбрать другой тариф ↩️", callback_data="t_plans")
    key.add(pay_btn)
    key.add(plans)
    key.add(index_btn)
    return key


def index_key(user_id):
    key = InlineKeyboardMarkup()

    trading = InlineKeyboardButton(text="Торговые сигналы  💹", callback_data="trading")
    training = InlineKeyboardButton("Торговые идеи 👤", callback_data="training")
    teaching = InlineKeyboardButton("Обучение трейдингу  💻", callback_data="teaching")
    suit = InlineKeyboardButton("Индивидуальный Инвест Портфель  📈", callback_data="suit")
    akcii = InlineKeyboardButton("Акции 🎁", callback_data="akcii")
    about = InlineKeyboardButton("О Нас I Доп. Услуги I Контакты  📝", callback_data="about")
    help_ = InlineKeyboardButton(text='▪Поддержка пользователей▪️', url='t.me/bkrtboss')
    key.add(trading)
    key.add(training)
    key.add(teaching)
    key.add(suit)
    key.add(akcii)
    key.add(about)
    key.add(help_)    
    if user_id in ADMINS:
        key.add(InlineKeyboardButton("✉️ Рассылка", callback_data="mailing"),
                InlineKeyboardButton("✉️ Репост", callback_data="repost")
                )
    return key

def repost_put():
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton("Приватный канал💰", callback_data="repost_private_channel"),
        InlineKeyboardButton("Бесплатный канал📈", callback_data="repost_free_channel"),
        InlineKeyboardButton("↪️ Вернуться", callback_data="index")

    )

    return key

def repost_from():
    key = InlineKeyboardMarkup()
    key.add(InlineKeyboardButton("VK", callback_data="repost_vk"),
            InlineKeyboardButton("Instagram", callback_data="repost_insta"),
            InlineKeyboardButton("↪️ Вернуться", callback_data="index")
            )
    return key

def repost_send():
    key = InlineKeyboardMarkup(row_width=1)

    confirm = InlineKeyboardButton("📩 Отправить", callback_data="send_sub")
    schedule = InlineKeyboardButton("⏱ Запланировать", callback_data="schedule")
    key.add(confirm)
    key.add(schedule)
    return key

def confirm_key():
    key = InlineKeyboardMarkup()

    confirm = InlineKeyboardButton("Перейти к оплате ☑️", callback_data="confirm")
    # trial = InlineKeyboardButton(price_answers.get("trial"), callback_data="trial")

    key.add(confirm)
    # if not get_user(user_id):
    #     key.add(trial)
    key.add(index_btn)
    return key


def get_phone_key():
    key = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_phone = KeyboardButton(text="📲 Отправить номер телефона ", request_contact=True)
    cancel_btn = KeyboardButton(text='↩️ Вернуться')

    key.add(button_phone)
    key.add(cancel_btn)
    return key


def trading_prices(user_id):
    key = InlineKeyboardMarkup()
    # trial = InlineKeyboardButton(price_answers.get("trial"), callback_data="trial")

    # try:
    #     if not get_user(user_id):
    #         key.add(trial)
    # except Exception as e:
    #     print(e)
    begin_btn = InlineKeyboardButton(price_answers.get("begin"), callback_data="trading_begin")
    optimal_btn = InlineKeyboardButton(price_answers.get("optimal"), callback_data="trading_optimal")
    standart_btn = InlineKeyboardButton(price_answers.get("standart"), callback_data="trading_standart")
    premium_btn = InlineKeyboardButton(price_answers.get("premium"), callback_data="trading_premium")

    key.add(begin_btn)
    key.add(optimal_btn)
    key.add(standart_btn)
    key.add(premium_btn)
    key.add(index_btn)

    key.add()
    return key


def get_trial():
    key = InlineKeyboardMarkup()
    get_trial_btn = InlineKeyboardButton("Подтвердить пробный период", callback_data="get_trial")
    key.add(get_trial_btn)
    key.add(index_btn)
    return key


def update_subscribe():
    key = InlineKeyboardMarkup()
    key.add(InlineKeyboardButton("Купить подписку", "https://t.me/bkrtbot"))
    key.add(InlineKeyboardButton("Перейти в меню", callback_data="index"))
    return key


def sub_msg_key():
    key = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Бот помощник 🤖", callback_data="index")
    but2 = InlineKeyboardButton("🔻VK", url='vk.com/bkrt_inc')
    but3 = InlineKeyboardButton("🔹Instagram", url='https://www.instagram.com/bkrt_inc/')
    but4 = InlineKeyboardButton("Навигация на канале📝", callback_data="navigate")
    but5 = InlineKeyboardButton("Акции🎁", callback_data="akcii")
    but6 = InlineKeyboardButton("🔸Поддержка пользователей🔸", url='t.me/bkrtboss')
    key.add(but1)
    key.add(but2)
    key.add(but3)
    key.add(but4)
    key.add(but5)
    key.add(but6)
    return key

def sub_msg_key_navigate():
    key = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Бот помощник 🤖", callback_data="index")
    but2 = InlineKeyboardButton("🔻VK", url='vk.com/bkrt_inc')
    but3 = InlineKeyboardButton("🔹Instagram", url='https://www.instagram.com/bkrt_inc/')
    but4 = InlineKeyboardButton("Навигация на канале📝", callback_data="navigate")
    but5 = InlineKeyboardButton("Акции🎁", callback_data="akcii")
    but6 = InlineKeyboardButton("🔸Поддержка пользователей🔸", url='t.me/bkrtboss')
    but7 = InlineKeyboardButton(text='↪️ Вернуться', callback_data='return_navigate')
    key.add(but1)
    key.add(but2)
    key.add(but3)
    key.add(but4)
    key.add(but5)
    key.add(but6)
    key.add(but7)
    return key


def send_sub_msg_key(chat_type):
    key = InlineKeyboardMarkup(row_width=1)

    confirm = InlineKeyboardButton("📩 Отправить", callback_data="send_sub")
    schedule = InlineKeyboardButton("⏱ Запланировать", callback_data="schedule")
    edit = InlineKeyboardButton("✏️ Редактировать", callback_data="edit_sub")

    if chat_type == "private":
        edit = InlineKeyboardButton("✏️ Редактировать", callback_data="edit_private")

    elif chat_type == "free":
        edit = InlineKeyboardButton("✏️ Редактировать", callback_data="edit_free")

    cancel = InlineKeyboardButton("Отмена", callback_data="index")

    key.add(confirm, schedule, edit, cancel)
    return key


def select_posting_key():
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton("Приватный канал💰", callback_data="private_channel"),
        InlineKeyboardButton("Бесплатный канал📈", callback_data="free_channel"),
        InlineKeyboardButton("📬 Личное сообщение", callback_data="send_private"),
        InlineKeyboardButton("📤 Все посты", callback_data="all_posts"),
        InlineKeyboardButton("↪️ Вернуться", callback_data="index")

    )

    return key



def list_posts_key(n):
    key = InlineKeyboardMarkup()

    next_page_btn = InlineKeyboardButton("Вперед ➡️", callback_data="next_page")
    prev_page_btn = InlineKeyboardButton("⬅️ Назад", callback_data="prev_page")
    count = len(get_all_posts())
    print("COUNT", count)
    pages = []
    page = []
    for i in range(0, count, 5):
        page.append(i)

    for i in page:
        x = i + 5
        s = [i, x]
        pages.append(s)

    posts = get_posts(pages[n][0], pages[n][1])

    for post in posts:
        key.add(
            InlineKeyboardButton(post.text[:20], callback_data=post.id),
            InlineKeyboardButton(post.time, callback_data=f"call"),

            InlineKeyboardButton("❌", callback_data=f"del_{post.id}")
        )

    if n == 0 and count > 5:
        key.add(next_page_btn)

    elif len(pages) == n + 1:
        key.add(prev_page_btn)

    elif n != 0 and count > 5:
        key.add(prev_page_btn, next_page_btn)

    key.add(InlineKeyboardButton("✉️ Рассылка", callback_data="mailing")
            )
    return key
