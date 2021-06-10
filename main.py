import re
from datetime import datetime
from time import sleep
from urllib.request import urlretrieve
import os
import flask
import uuid
from flask import Flask, request
from imgurpython import ImgurClient
from pyngrok import ngrok
from telebot import TeleBot, types
from telebot.types import Update
from answers import *
from config import bot_token, trading_group_link, private_group_id, free_group_id
#from db import add_exp_date_for_admin
from db import *
from fk import client
from keyboards import *
import getpass
from repost_n import repost

# from send_post import send_channel_post

b = TeleBot(bot_token)

app = Flask(__name__)

# from telethon import types

api_id = 1436469
api_hash = '455c8d612f5770543806033235d9d722'
group = 'https://t.me/joinchat/AAAAAFNTA80Oa2U6Aqk9TQ'

day_dict = {"ПН": "MON",
            "ВТ": "TUE",
            "СР": "WED",
            "ЧТ": "THU",
            "ПТ": "FRI",
            "СБ": "SAT",
            "ВС": "SUN"}

day_num = {"ПН": "1",
           "ВТ": "2",
           "СР": "3",
           "ЧТ": "4",
           "ПТ": "5",
           "СБ": "6",
           "ВС": "0"}


@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        b.process_new_updates([update])
        return '200'
    else:
        flask.abort(403)


user_data = {}
ADMINS = [445116305, 516703737, 669917374]


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.first_name = ''
        self.last_name = ''
        self.username = ''
        self.phone_number = 0
        self.email = ''
        self.plan = ''
        self.sub_msg = ''
        self.posting_id = ''
        self.post_id = ''
        self.post_type = ''
        self.post_time = ''
        self.post_img = ''
        self.post_videos = ''
        self.post_files = ''
        self.gif_url = ''
        self.chat_type = ''
        self.from_n = 0
        self.to_n = 5
        self.imgur = ''


def run_bot():
    try:
        print("bot started")
        print(b.get_webhook_info())
        b.remove_webhook()
        # tunnel = Thread(target=get_conn)
        # x = tunnel.start()
        conf = ngrok.conf
        conf.get_default().auth_token = '1k75h6t76R4ZpQSnlDVWgDLFPtl_zsWwN7rQrQrbAL4fJLYF'

        conn = ngrok.connect(5555)

        print(conn.public_url)

        https = ngrok.get_tunnels()
        print("\nTunnels:\n", https)

        b.set_webhook(conn.public_url.replace("http", "https"))
        print("\nWEBHOOK:", b.get_webhook_info())

        ngrok_process = ngrok.get_ngrok_process()
        b.send_message(445116305, f"bot started", reply_markup=index_key(445116305))

        app.run("localhost", port=5555)

        try:
            # Block until CTRL-C or some other terminating event
            ngrok_process.proc.wait()
            print("proc", ngrok_process)
        except KeyboardInterrupt:
            print("\nServer Stopped\n")
    except Exception as e:
        print("\nException:", e)
        sleep(5)
        print("restart bot")
        run_bot()

#def run_bot():
#    #try:
#    b.remove_webhook()
#    print("bot started")
#
#    b.polling(none_stop=True, interval=10)
#
#    #except Exception as err:
#    #    print("run bot error:", err)

def send_index(message=None, call=None):
    try:

        if message:
            user_id = message.from_user.id
            user_data[user_id] = User(user_id)

            try:

                b.delete_message(message.from_user.id, message.message_id - 1)
            except Exception as e:
                print("index no msg -1", e)
            if message.from_user.username:
                b.send_message(user_id, f'🔺Приветствую, <b>{message.from_user.first_name}</b>!'+ hello,
                               parse_mode="HTML", reply_markup=index_key(user_id))
            elif call.from_user.first_name:
                b.send_message(user_id, f'🔺Приветствую, <b>{message.from_user.first_name}</b>!'+ hello,
                               parse_mode="HTML", reply_markup=index_key(user_id))
        if call:
            user_id = call.message.chat.id
            user_data[user_id] = User(user_id)
            if call.from_user.username:
                b.send_message(user_id, f'🔺Приветствую, <b>{call.from_user.username}</b>!'+ hello,
                               parse_mode="HTML", reply_markup=index_key(user_id))

            elif call.from_user.first_name:
                b.send_message(user_id, f'🔺Приветствую, <b>{call.from_user.first_name}</b>!'+ hello,
                               parse_mode="HTML", reply_markup=index_key(user_id))

    except Exception as e:
        print("send_index ex:", e)

def send_index_akcii(message=None, call=None):
    try:
        if call:
            user_id = call.message.chat.id
            user_data[user_id] = User(user_id)
            if call.from_user.username:
                b.send_message(user_id, ans_akcii,
                               parse_mode="HTML", reply_markup=akcii(user_id))
            elif call.from_user.first_name:
                b.send_message(user_id, ans_akcii,
                               parse_mode="HTML", reply_markup=akcii(user_id))
    except Exception as e:
        print("send_index ex:", e)

def send_index_about(message=None, call=None):
    try:
        if call:
            user_id = call.message.chat.id
            user_data[user_id] = User(user_id)
            if call.from_user.username:
                b.send_message(user_id, ans_about,
                               parse_mode="HTML", reply_markup=about())
            elif call.from_user.first_name:
                b.send_message(user_id, ans_about,
                               parse_mode="HTML", reply_markup=about())
    except Exception as e:
        print("send_index ex:", e)

def send_index_navigate(message=None, call=None):
    try:
        if call:
            user_id = call.message.chat.id
            user_data[user_id] = User(user_id)
            if call.from_user.username:
                b.send_message(user_id, ans_navigate,
                               parse_mode="HTML", reply_markup=training())
            elif call.from_user.first_name:
                b.send_message(user_id, ans_navigate,
                               parse_mode="HTML", reply_markup=training())
    except Exception as e:
        print("send_index ex:", e)

def select_posting(user_id):
    b.send_message(user_id, "Рассылка", reply_markup=select_posting_key())


def send_free_channel(user_id):
    m = b.send_message(user_id, f"Введите текст для рассылки в канал <b>{b.get_chat(free_group_id).title}</b>:",
                       reply_markup=cancel_markup(),
                       parse_mode="HTML")
    b.register_next_step_handler(m, get_free_msg)


def send_private_channel(user_id):
    m = b.send_message(user_id, f"Введите текст для рассылки в канал <b>{b.get_chat(private_group_id).title}</b>:",
                       reply_markup=cancel_markup(),
                       parse_mode="HTML")
    b.register_next_step_handler(m, get_private_msg)


def send_news(user_id):
    m = b.send_message(user_id, "Введите текст для рассылки в личные сообщения:", reply_markup=cancel_markup())
    b.register_next_step_handler(m, get_sub_msg)


def get_free_msg(message):
    user_id = message.from_user.id

    if (message.text.__contains__("Отмена")) and (message.chat.type == 'private'):
        b.clear_step_handler_by_chat_id(user_id)
        send_index(message=message)
    else:
        try:
            user = user_data[user_id]
        except Exception as e:
            print(e)
            user_data[user_id] = User(user_id)
            user = user_data[user_id]

        user.sub_msg = message.text
        user.post_id = uuid.uuid1().time
        b.send_message(user_id, f"Текст сообщения:\n\n"
                                f"{user.sub_msg}", reply_markup=add_media_key(), parse_mode="HTML")


def get_private_msg(message):
    user_id = message.from_user.id

    if (message.text.__contains__("Отмена")) and (message.chat.type == 'private'):
        b.clear_step_handler_by_chat_id(user_id)
        send_index(message=message)
    else:
        try:
            user = user_data[user_id]
        except Exception as e:
            print(e)
            user_data[user_id] = User(user_id)
            user = user_data[user_id]

        user.sub_msg = message.text
        user.post_id = uuid.uuid1().time

        b.send_message(user_id, f"Текст сообщения:\n\n"
                                f"{user.sub_msg}", reply_markup=add_media_key(), parse_mode="HTML")


def get_sub_msg(message):
    user_id = message.from_user.id

    if (message.text.__contains__("Отмена")) and (message.chat.type == 'private'):
        b.clear_step_handler_by_chat_id(user_id)
        send_index(message=message)

    else:
        try:
            user = user_data[user_id]
        except Exception as e:
            print(e)
            user_data[user_id] = User(user_id)
            user = user_data[user_id]

        user.sub_msg = message.text
        user.post_id = uuid.uuid1().time

        b.send_message(user_id, f"Текст сообщения:\n\n"
                                f"{user.sub_msg}", reply_markup=add_media_key(), parse_mode="HTML")


def send_trading_plans(user_id):
    b.send_message(user_id, "🔺Для подключения к услуге «Торговые сигналы» выберите соответствующий тарифный план и следуйте инструкциям по оплате:", reply_markup=trading_prices(user_id))


@b.message_handler(content_types=["document"])
def handle_files(message):
    user_id = message.from_user.id
    user = user_data[user_id]
    document_id = message.document.file_id
    file_info = b.get_file(document_id)

    if not os.path.exists(f"./post_media/{user.post_id}"):
        os.mkdir(f"./post_media/{user.post_id}")
    if not os.path.exists(f"./post_media/{user.post_id}/documents"):
        os.mkdir(f"./post_media/{user.post_id}/documents")

    print(file_info)
    urlretrieve(f'http://api.telegram.org/file/bot{bot_token}/{file_info.file_path}',
                f"./post_media/{user.post_id}/" + file_info.file_path)

    user.post_files = f"./post_media/{user.post_id}/documents/"

    b.send_message(user_id, text='Файл успешно добавлен!', reply_markup=add_image_key())


@b.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.from_user.id
    user = user_data[user_id]

    file_info = b.get_file(message.photo[len(message.photo) - 1].file_id)
    print(file_info)

    if user.imgur:
        gur = ImgurClient("daafb00be8b8204", "da5907ccbec8b73fb32402261e68d9c4c7a61fbc")

        res = b.get_file_url(file_info.file_id)
        img_link = gur.upload_from_url(res).get('link')
        print("\nIMG link:", img_link)
        user.post_img = img_link
        b.send_message(user_id, "Картинка добавлена", reply_markup=send_sub_msg_key(user.chat_type))

    else:

        if not os.path.exists(f"./post_media/{user.post_id}"):
            os.mkdir(f"./post_media/{user.post_id}")
        if not os.path.exists(f"./post_media/{user.post_id}/photos"):
            os.mkdir(f"./post_media/{user.post_id}/photos")

        downloaded_file = b.download_file(file_info.file_path)

        src = f'./post_media/{user.post_id}/' + file_info.file_id + "." + file_info.file_path.split(".")[1]
        print("\nSRC", src)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        user.post_img = f"./post_media/{user.post_id}/photos/"

        b.send_message(user_id, "Фото добавлено", reply_markup=add_image_key())

class Repost:
    from_ = ''
    put = ''


@b.message_handler(content_types=["video"])
def handle_files(message):
    print("\n", message)
    user_id = message.from_user.id
    user = user_data[user_id]
    video_id = message.video.file_id
    print(video_id)
    file_info = b.get_file(video_id)

    if not os.path.exists(f"./post_media/{user.post_id}"):
        os.mkdir(f"./post_media/{user.post_id}")
    if not os.path.exists(f"./post_media/{user.post_id}/videos"):
        os.mkdir(f"./post_media/{user.post_id}/videos")

    print("\n", file_info)
    print("\n", file_info.file_path)
    urlretrieve(f'http://api.telegram.org/file/bot{bot_token}/{file_info.file_path}',
                f"./post_media/{user.post_id}/" + file_info.file_path)

    user.post_videos = f"./post_media/{user.post_id}/videos/"

    b.send_message(user_id, text='Видео успешно добавлено!', reply_markup=add_image_key())


@b.message_handler(content_types=['text'])
def get_text_msg(message):
    user_id = message.from_user.id
    print(message.from_user)
    print("\nMESSAGE:", message.text)
    try:

        if (message.text.__contains__("start")) and (message.chat.type == 'private'):
            user_data[user_id] = User(user_id)

            if message.from_user.username:
                b.send_message(user_id, f'🔺Приветствую, <b>{message.from_user.username}!</b>'+ hello,
                               parse_mode="HTML", reply_markup=index_key(user_id))
            else:
                b.send_message(user_id, f'🔺Приветствую, <b>{message.from_user.first_name}!</b>'+ hello,
                               parse_mode="HTML", reply_markup=index_key(user_id))
        if message.text == "send" and message.from_user.id in ADMINS and message.chat.type == "private":
            select_posting(user_id)

    except Exception as e:
        print("\nget_text_msg ex:", e)
        # b.send_message(user_id, text=e)


@b.callback_query_handler(func=lambda call: True)
def get_call(call):
    print('*' * 120)
    print("\nUser:", call.from_user)
    print("\nCall data:", call.data)
    print('*' * 120)
    user_id = call.from_user.id

    try:
        user = user_data[user_id]
    except Exception as e:
        print("user", e)
        user_data[user_id] = User(user_id)
        user = user_data[user_id]
    try:
        if call.data == 'index':
            send_index(call=call)
        elif call.data == 'return_akcii':
            send_index_akcii(call=call)
        elif call.data == 'return_about':
            send_index_about(call=call)
        elif call.data == 'return_navigate':
            send_index_navigate(call=call)
        #####################################################
        try:
            b.delete_message(user_id, call.message.message_id)
            print(f"{call.message.message_id} was deleted")
        except Exception as e:
            print("call_del ex", e)
        if call.data == 'trading':
            b.send_message(user_id, ans_trading,
                           reply_markup=confirm_key(), parse_mode="HTML")

        if call.data == 'training':
            b.send_message(user_id, ans_training, reply_markup=training(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'navigate':
            b.send_message(user_id, ans_navigate, reply_markup=sub_msg_key_navigate(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'network':
            b.send_message(user_id, ans_network, reply_markup=return_btn(),parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'teaching':
            b.send_message(user_id, ans_teaching, reply_markup=return_btn(), parse_mode="HTML")

        if call.data == 'suit':
            b.send_message(user_id, ans_suit, reply_markup=return_btn(), parse_mode="HTML")

        if call.data == 'akcii':
            b.send_message(user_id, ans_akcii, reply_markup=akcii(user_id), parse_mode="HTML")
        # ================================================== Меню Акции
        if call.data == 'add_sb':
            b.register_next_step_handler(b.send_message(user_id, 'Введите ID пользователя'), add_sb)

        if call.data == 'day_of_sub':
            b.send_message(user_id, ans_day_of_sub, reply_markup=confirm_key(),parse_mode="HTML")
        if call.data == 'cashback':
            b.send_message(user_id, ans_cashback, reply_markup=return_akcii(),parse_mode="HTML")
        if call.data == 'ad_in_vk':
            b.send_message(user_id, ans_ad_in_vk, reply_markup=return_akcii())
        if call.data == 'ad_in_insta':
            b.send_message(user_id, ans_ad_in_insta, reply_markup=return_akcii(),parse_mode="HTML")
        if call.data == 'invite_friends':
            b.send_message(user_id, ans_invite_friends, reply_markup=return_akcii(),parse_mode="HTML")
        # ==================================================
        if call.data == 'about':
            b.send_message(user_id, ans_about, reply_markup=about(), parse_mode="HTML")

        # ================================================== Меню О нас
        if call.data == 'about_us':
            b.send_message(user_id, ans_about_us, reply_markup=return_about_and_help(),parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'ads':
            b.send_message(user_id, ans_ads, reply_markup=return_about(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'trening':
            b.send_message(user_id, ans_trening, reply_markup=return_about(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'consult':
            b.send_message(user_id, ans_consult, reply_markup=return_about(), parse_mode="HTML",
                           disable_web_page_preview=False)


        #================================================

        if call.data == 'repost':
            b.send_message(user_id, 'Куда делать репост?', reply_markup=repost_put(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'repost_private_channel':
            Repost.put = 'private'
            b.send_message(user_id, 'Откуда брать пост?', reply_markup=repost_from(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'repost_free_channel':
            Repost.put = 'free'
            b.send_message(user_id, 'Откуда брать пост?', reply_markup=repost_from(), parse_mode="HTML",
                           disable_web_page_preview=False)

        if call.data == 'repost_vk':
            Repost.from_ = 'VK'
            b.send_message(user_id, 'Запуск скрипта')
            url_post = repost(Repost.from_)
            user.sub_msg = repost_vk + '\n' +'\n' + f'<a href="{url_post}">{url_post}</a>'
            if Repost.put == 'free':
                user.posting_id = free_group_id
            else:
                user.posting_id = private_group_id
            Repost.from_ = ''
            Repost.put = ''
            b.send_message(call.message.chat.id, 'Что сделать?', reply_markup=repost_send())

        if call.data == 'repost_insta':
            Repost.from_ = 'Instagram'
            b.send_message(user_id, 'Запуск скрипта')
            url_post = repost(Repost.from_)
            user.sub_msg = repost_insta + '\n' + '\n' + f'<a href="{url_post}">{url_post}</a>'
            if Repost.put == 'free':
                user.posting_id = free_group_id
            else:
                user.posting_id = private_group_id
            Repost.from_ = ''
            Repost.put = ''
            b.send_message(call.message.chat.id, 'Что сделать?', reply_markup=repost_send())

        if call.data == 'confirm':

            if call.from_user.username:
                user.username = call.from_user.username

            if call.from_user.first_name:
                user.first_name = call.from_user.first_name

            if call.from_user.last_name:
                user.last_name = call.from_user.last_name

            user_db = get_user(user_id)

            if not user_db or user_db.trial == "Yes":                  # if not user_db or user_db.trial == "Yes"

                m = b.send_message(user_id, "Введите ваш <b>номер телефона</b>:\n\n"
                                            "<i>Например: 78877554411</i>",
                                   reply_markup=get_phone_key(), parse_mode="HTML")
                b.register_next_step_handler(m, get_phone)

            else:
                send_trading_plans(user_id)

        if call.data == 'trading_begin':
            user.plan = call.data
            start_payment(user_id, plan=call.data.split("_")[-1], call=call)

        if call.data == 'trading_optimal':
            user.plan = call.data

            start_payment(user_id, plan=call.data.split("_")[-1], call=call)

        if call.data == 'trading_standart':
            user.plan = call.data

            start_payment(user_id, plan=call.data.split("_")[-1], call=call)

        if call.data == 'trading_premium':
            user.plan = call.data

            start_payment(user_id, plan=call.data.split("_")[-1], call=call)

        if call.data == 't_plans':
            try:
                b.delete_message(call.from_user.id, call.message.message_id - 2)
            except Exception as e:
                print("t plans -2", e)

            try:

                b.delete_message(call.from_user.id, call.message.message_id + 1)
            except Exception as e:
                print("t plans +1", e)
            try:

                b.delete_message(call.from_user.id, call.message.message_id + 2)

            except Exception as e:
                print("t plans +2", e)
            send_trading_plans(user_id)

        if call.data == 'trial':
            b.send_message(user_id, "Для подключения пробного периода нажмите на кнопку", reply_markup=get_trial(),
                           parse_mode="HTML")

        if call.data == 'get_trial':

            if call.from_user.username:
                user.username = call.from_user.username
            if call.from_user.last_name:
                user.last_name = call.from_user.last_name

            user.first_name = call.from_user.first_name

            user.plan = call.data.split("_")[-1]

            add_user(user_id,
                     phone_number=user.phone_number,
                     email=user.email,
                     first_name=user.first_name,
                     last_name=user.last_name,
                     username=user.username,
                     trial="Yes")

            add_trial(user_id, plan=user.plan)

            # group_link = b.export_chat_invite_link(group_id)
            #
            # print("\nGROUP_LINK:", group_link)
            #
            b.send_message(user_id, "Пробный период активирован\n\n"
                                    f"Ссылка на канал - {trading_group_link}")
            # sleep(60)
            # new_group_link = b.export_chat_invite_link(group_id)

            # print("\nNEW_GROUP_LINK:", new_group_link)
        if call.data == "send_sub":
            users_list = []
            if user.chat_type == 'send_private':
                for db_user in get_id_from_db():

                    try:
                        if user.gif_url:
                            b.send_message(db_user, user.sub_msg + "\n" + f"""<a href="{user.gif_url}">&#8203;</a>""" ,
                                           reply_markup=sub_msg_key(),
                                           parse_mode="HTML")
                            #b.send_animation(db_user, user.gif_url)
                            user.gif_url = None
                        else:
                            b.send_message(db_user, user.sub_msg,
                                           reply_markup=sub_msg_key(),
                                           parse_mode="HTML")
                        users_list.append(db_user)
                        sleep(20)
                    except Exception as e:
                        print(e)
                b.send_message(user_id, f"Сообщение успешно отправлено пользователям:\n{users_list}", reply_markup=cancel_btn())

            else:
                # send_channel_post(user.post_id)
                if user.imgur:
                    b.send_message(user.posting_id, user.sub_msg + "\n" + f"""<a href="{user.post_img}">&#8203;</a>""",reply_markup=sub_msg_key(),
                                   parse_mode="HTML")
                    b.send_message(user_id, "Пост отправлен!", reply_markup=select_posting_key())
                elif user.gif_url:
                    b.send_message(user.posting_id, user.sub_msg + "\n" + f"""<a href="{user.gif_url}">&#8203;</a>""",reply_markup=sub_msg_key(),
                                   parse_mode="HTML")
                    #b.send_animation(user.posting_id, user.gif_url)
                    b.send_message(user_id, "Пост отправлен!", reply_markup=select_posting_key())
                    user.gif_url = None

                else:
                    b.send_message(user.posting_id, user.sub_msg, parse_mode="HTML", disable_web_page_preview=True)
                    b.send_message(user_id, "Пост отправлен!", reply_markup=select_posting_key())

        if call.data == "edit_sub":
            m = b.send_message(user_id, "Введите текст для рассылки:", reply_markup=return_markup())
            b.register_next_step_handler(m, get_sub_msg)

        if call.data == "edit_private":
            m = b.send_message(user_id, "Введите текст для рассылки:", reply_markup=return_markup())
            b.register_next_step_handler(m, get_private_msg)

        if call.data == "edit_free":
            m = b.send_message(user_id, "Введите текст для рассылки:", reply_markup=return_markup())
            b.register_next_step_handler(m, get_free_msg)

        if call.data == "send_private":
            user.chat_type = "send_private"
            send_news(user_id)

        if call.data == "private_channel":
            user.chat_type = "private"
            user.posting_id = private_group_id
            send_private_channel(user_id)

        if call.data == "free_channel":
            user.chat_type = "free"
            user.posting_id = free_group_id
            send_free_channel(user_id)

        if call.data == "add_media":
            b.send_message(user_id, "Отправьте изображение или файл:", reply_markup=None)

        if call.data == "next_step":
            b.send_message(user_id, user.sub_msg,
                           disable_web_page_preview=True,
                           reply_markup=send_sub_msg_key(user.chat_type),
                           parse_mode="HTML")
        if call.data == "schedule":
            m = b.send_message(user_id, "Выберите, подходящий интервал:",
                               reply_markup=periodicity_markup())
            b.register_next_step_handler(m, get_period)

        if call.data == "all_posts":
            user.to_n = 0
            try:
                b.send_message(user_id, "Posts", reply_markup=list_posts_key(user.to_n))
            except Exception as e:
                b.send_message(user_id, "Посты еще не созданы!", reply_markup=select_posting_key())
        if call.data == "next_page":
            user.to_n += 1
            b.send_message(user_id, "Posts", reply_markup=list_posts_key(user.to_n))

        if call.data == "prev_page":
            user.to_n -= 1
            b.send_message(user_id, "Posts", reply_markup=list_posts_key(user.to_n))

        if call.data.__contains__("del_"):
            delete_post(call.data.split("_")[1])
            b.send_message(user_id, "Пост успешно удален!", reply_markup=select_posting_key())

        if call.data == "mailing":
            select_posting(call.message.chat.id)

        if call.data == "add_imgur":
            user.imgur = True
            b.send_message(user_id, "Отправьте картинку:", reply_markup=cancel_markup())

        if call.data == 'add_gif':
            m = b.send_message(user_id, "Отправьте ссылку на GIF:", reply_markup=cancel_markup())
            b.register_next_step_handler(m, get_gif)
    except Exception as e:
        print(e)
        print(e.args)
        # b.send_message(user_id, text=e)


def get_gif(message):
    global User
    user_id = message.from_user.id
    try:
        user = user_data[user_id]
    except Exception as e:
        print("user", e)
        user_data[user_id] = User(user_id)
        user = user_data[user_id]
    user.gif_url = message.text
    try:
        b.send_animation(message.chat.id, user.gif_url)
        b.send_message(message.chat.id, "GIF УСПЕШНО прикреплен", reply_markup=send_sub_msg_key(user.chat_type))
    except Exception as e:
        b.send_message(message.chat.id, 'Ошибка: '+str(e), reply_markup=cancel_markup())

add = {
    'user_id': None,
    'start_date': None,
    'end_date': None,
}
def add_sb(message):
    try:
        if message.text != add['user_id'] and int(message.text) != 4:
            add['user_id'] = message.text
        b.register_next_step_handler(b.send_message(message.chat.id, 'Введите сегодняшнюю дату (ввод даты гггг.мм.дд)'), add_st_date)
    except:
        b.register_next_step_handler(b.send_message(message.chat.id, 'Введите сегодняшнюю дату (ввод даты гггг.мм.дд)'), add_st_date)
def add_st_date(message):
    da = str(message.text).split('.')
    if len(da) == 3 and len(da[0])==4 and len(da[1])==2 and len(da[2])==2:
        pass
    else:
        b.register_next_step_handler(b.send_message(message.chat.id,'Ошибка, неверно указана дата. Попробуйте еще раз(Напишите okey)'),add_sb)
        return 'pass'
    add['start_date'] = message.text
    b.register_next_step_handler(b.send_message(message.chat.id, 'Введите дату окончания подключения (ввод даты гггг.мм.дд) '),add_end_date)
def check_days(a, b):
    import datetime
    a = a.split('.')
    b = b.split('.')
    aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
    cc = aa - bb
    dd = str(cc)
    print(dd.split()[0])
    return dd.split()[0]
def add_end_date(message):
    da = str(message.text).split(".")
    if len(da) == 3 and len(da[0])==4 and len(da[1])==2 and len(da[2])==2:
        pass
    else:
        b.register_next_step_handler(b.send_message(message.chat.id,'Ошибка, неверно указана дата. Попробуйте еще раз (Напишите okey)'),add_sb)
        return 'pass'
    add['end_date'] = message.text
    if int(check_days(add['end_date'],add['start_date'])) < 1:
        return b.send_message(message.chat.id,'Не верно написанная дата', reply_markup=return_btn())
    try:
        #db_user = get_user(add['user_id'])
        db_user = get_user(add['user_id'])
        if db_user:
            remove_exp_date(add['user_id'])
            session.commit()
        if not db_user:
            add_user(add['user_id'], 00000, 'nnnnnnn@gmail.com',
                 first_name='nnnnnnnn',
                 last_name='mmmmmmmm',
                 username='qqqqqqqq', trial="No")
        try:
            b.unban_chat_member(group, add['user_id'])
        except:
            pass
        add_exp_date_for_admin(add['user_id'], int(check_days(add['start_date'],add['end_date'])))
        b.send_message(message.chat.id, 'Пользователь успешно добавлен', reply_markup=return_btn())
        print("#"*100)
        print(add['user_id'])
        b.send_message(add['user_id'], f"Ссылка на канал - {trading_group_link}", reply_markup=return_btn())
    except Exception as ex:
        b.send_message(message.chat.id, 'Ошибка:' +str(ex), reply_markup=return_btn())

def get_period(message):
    user_id = message.from_user.id
    try:
        user = user_data[user_id]
    except Exception as e:
        print(e)
        user_data[user_id] = User(user_id)
        user = user_data[user_id]

    if message.text.__contains__("Сегодня"):
        user.post_type = 'today'
        m = b.send_message(user_id, "Укажите время публикации поста в формате чч:мм (0-23)\n\n"
                                    "Например 12:00")
        b.register_next_step_handler(m, get_time)

    elif message.text.__contains__("Ежедневный"):
        user.post_type = 'everyday'

        m = b.send_message(user_id, "Укажите время публикации поста в формате чч:мм (0-23)\n\n"
                                    "Например 12:00")
        b.register_next_step_handler(m, get_time)

    elif message.text.__contains__("Еженедельный"):
        user.post_type = 'every_week'

        m = b.send_message(user_id, "Укажите время и день публикации поста в формате чч:мм*DOW\n\n"
                                    "Например: 12:00*ПН или 12:00*ПН-ВТ-СР-ЧТ-ПТ")
        b.register_next_step_handler(m, get_time)

    elif message.text.__contains__("Ежемесячный"):
        user.post_type = 'every_month'

        m = b.send_message(user_id, "Укажите время и день публикации поста в формате чч:мм*DOM\n\n"
                                    "Например: 12:00*1 или 12:00*1-2-3-5-10")
        b.register_next_step_handler(m, get_time)
    else:
        m = b.send_message(user_id, "Неверный ввод\n\n"
                                    "Выберите интервал",
                           reply_markup=periodicity_markup())
        b.register_next_step_handler(m, get_period)


def get_time(message):
    user_id = message.from_user.id
    try:
        user = user_data[user_id]
    except Exception as e:
        print(e)
        user_data[user_id] = User(user_id)
        user = user_data[user_id]
    user.post_time = message.text
    if user.post_type == 'every_week':
        if not message.text.__contains__("-"):
            job = cron.new(
                command=f'. /home/admin_bot/blackratebot/env/bin/activate && cd /home/admin_bot/blackratebot/ && python3 send_post.py {user.post_id} && deactivate > log.txt',
                comment=str(user.post_id))

            try:
                day = day_dict.get(message.text.split("*")[1])
                print(day)
                job.dow.on(day)
                hour = message.text.split("*")[0].split(":")[0]
                print(hour)
                job.hour.on(hour)
                job.minute.on(message.text.split("*")[0].split(":")[1])
            except ValueError:
                m = b.send_message(user_id, "Введите корректное время (0-23)")
                b.register_next_step_handler(m, get_time)
            except Exception as e:
                print("everyday err:", e)

            cron.write_to_user(user=getpass.getuser())
            create_post(user_id=user_id,
                        group_id=user.posting_id,
                        post_id=user.post_id,
                        text=user.sub_msg,
                        time=user.post_time,
                        img=user.post_img,
                        video=user.post_videos,
                        file=user.post_files,
                        post_type=user.post_type
                        )

            b.send_message(user_id,
                           f"Пост {user.post_id}\n\n {user.sub_msg[:200]}...\n\nуспешно запланирован на {user.post_time}!",
                           reply_markup=mailing_btn())

        else:
            job = cron.new(
                command=f'. /home/admin_bot/blackratebot/env/bin/activate && cd /home/admin_bot/blackratebot/ && python3 send_post.py {user.post_id} && deactivate > log.txt',
                comment=str(user.post_id))

            days = message.text.split("*")[1].split("-")
            print("\nDAYS=", days)
            day_list = []
            try:
                for day in days:
                    day_list.append(day_num.get(day))
                    print(day)
                on_dow = ",".join(day_list)
                print("\nON:", on_dow)
                hour = message.text.split("*")[0].split(":")[0]
                minute = message.text.split("*")[0].split(":")[1]
                print(minute)
                if minute == "00":
                    minute = "0"

                job.setall(minute, hour, '*', '*', on_dow)
                print(job)
                cron.write()

            except ValueError:
                m = b.send_message(user_id, "Введите корректное время (0-23)")
                b.register_next_step_handler(m, get_time)

            create_post(user_id=user_id,
                        group_id=user.posting_id,
                        post_id=user.post_id,
                        text=user.sub_msg,
                        time=user.post_time,
                        img=user.post_img,
                        video=user.post_videos,
                        file=user.post_files,
                        post_type=user.post_type
                        )
            b.send_message(user_id,
                           f"Пост {user.post_id}\n\n {user.sub_msg[:200]}...\n\nуспешно запланирован на {user.post_time}!",
                           reply_markup=mailing_btn())

    elif message.text.__contains__("*") and user.post_type == "every_month":
        if not message.text.__contains__("-"):
            job = cron.new(
                command=f'. /home/admin_bot/blackratebot/env/bin/activate && cd /home/admin_bot/blackratebot/ && python3 send_post.py {user.post_id} && deactivate > log.txt',
                comment=str(user.post_id))
            try:
                job.dom.on(message.text.split("*")[1])
                job.hour.on(message.text.split("*")[0].split(":")[0])
                job.minute.on(message.text.split("*")[0].split(":")[1])
                print(job)
                cron.write()

            except ValueError:
                m = b.send_message(user_id, "Введите корректное время (0-23)")
                b.register_next_step_handler(m, get_time)

            create_post(user_id=user_id,
                        group_id=user.posting_id,
                        post_id=user.post_id,
                        text=user.sub_msg,
                        time=user.post_time,
                        img=user.post_img,
                        video=user.post_videos,
                        file=user.post_files,
                        post_type=user.post_type
                        )
            b.send_message(user_id,
                           f"Пост {user.post_id}\n\n {user.sub_msg[:200]}...\n\nуспешно запланирован на {user.post_time}!",
                           reply_markup=mailing_btn())

        else:
            job = cron.new(
                command=f'. /home/admin_bot/blackratebot/env/bin/activate && cd /home/admin_bot/blackratebot/ && python3 send_post.py {user.post_id} && deactivate > log.txt',
                comment=str(user.post_id))
            days = message.text.split("*")[1].replace("-", ",")
            print(days)
            try:
                hour = (message.text.split("*")[0].split(":")[0])
                minute = (message.text.split("*")[0].split(":")[1])
                job.setall(minute, hour, days, "*", "*")
                print(job)
                cron.write()

            except ValueError:
                m = b.send_message(user_id, "Введите корректное время (0-23)")
                b.register_next_step_handler(m, get_time)

            create_post(user_id=user_id,
                        group_id=user.posting_id,
                        post_id=user.post_id,
                        text=user.sub_msg,
                        time=user.post_time,
                        img=user.post_img,
                        video=user.post_videos,
                        file=user.post_files,
                        post_type=user.post_type
                        )
            b.send_message(
                user_id,
                f"Пост {user.post_id}\n\n {user.sub_msg[:200]}...\n\nуспешно запланирован на {user.post_time}!",
                reply_markup=mailing_btn())

    elif user.post_type == "today":
        print("\nUSER_POST ID:", user.post_id)
        job = cron.new(
            command=f'. /home/admin_bot/blackratebot/env/bin/activate && cd /home/admin_bot/blackratebot/ && python3 send_post.py {user.post_id} && deactivate > log.txt',
            comment=str(user.post_id))
        try:
            job.day.on(datetime.today().strftime("%d"))
            job.month.on(datetime.today().strftime("%m"))
            job.hour.on(int(message.text.split(":")[0]))
            job.minute.on(message.text.split(":")[1])
            cron.write()

        except ValueError:
            m = b.send_message(user_id, "Введите корректное время (0-23)")
            b.register_next_step_handler(m, get_time)

        create_post(user_id=user_id,
                    group_id=user.posting_id,
                    post_id=user.post_id,
                    text=user.sub_msg,
                    time=user.post_time,
                    img=user.post_img,
                    video=user.post_videos,
                    file=user.post_files,
                    post_type=user.post_type
                    )
        b.send_message(user_id,
                       f"Пост {user.post_id}\n\n {user.sub_msg[:200]}...\n\nуспешно запланирован на {user.post_time}!",
                       reply_markup=mailing_btn())

    elif user.post_type == "everyday":
        job = cron.new(
            command=f'. /home/admin_bot/blackratebot/env/bin/activate && cd /home/admin_bot/blackratebot/ && python3 send_post.py {user.post_id} && deactivate > log.txt',
            comment=str(user.post_id))
        try:
            job.hour.on(message.text.split(":")[0])
            job.minute.on(message.text.split(":")[1])
            cron.write()

        except ValueError:
            m = b.send_message(user_id, "Введите корректное время (0-23)")
            b.register_next_step_handler(m, get_time)

        create_post(user_id=user_id,
                    group_id=user.posting_id,
                    post_id=user.post_id,
                    text=user.sub_msg,
                    time=user.post_time,
                    img=user.post_img,
                    video=user.post_videos,
                    file=user.post_files,
                    post_type=user.post_type
                    )

        b.send_message(user_id,
                       f"Пост {user.post_id}\n\n {user.sub_msg[:200]}...\n\nуспешно запланирован на {user.post_time}!",
                       reply_markup=mailing_btn())

    cron.write(user=getpass.getuser())
    print("\nJOBS:\n")
    for j in cron:
        print(dir(j))
        print(j)


def get_phone(message):
    user_id = message.from_user.id
    b.delete_message(user_id, message.message_id)
    try:
        if message.text:
            if message.text.__contains__('Вернуться') or message.text.__contains__("start"):
                b.clear_step_handler_by_chat_id(message.chat.id)

                send_index(message=message)
            else:
                # b.delete_message(message.from_user.id, message.message_id)
                b.delete_message(message.from_user.id, message.message_id - 1)
                phone_number = message.text.replace("+", "")

                if not phone_number.isdigit() or len(phone_number) < 8:
                    back_msg = b.send_message(message.chat.id, "Неверный номер телефона!\n\n"
                                                               "Введите свой номер телефона: \n\n"
                                                               "<i>Например: 78877554411</i>",
                                              reply_markup=get_phone_key(),
                                              parse_mode="HTML")
                    b.register_next_step_handler(back_msg, get_phone)
                else:
                    user = user_data[user_id]
                    user.phone_number = phone_number

                    m = b.send_message(message.chat.id, text="Введите ваш email:", reply_markup=return_markup())
                    b.register_next_step_handler(m, get_email)

        else:
            phone_number = str(message.contact.phone_number).replace("+", "")
            user = user_data[user_id]
            user.phone_number = phone_number
            try:
                b.delete_message(message.from_user.id, message.message_id - 1)
            except Exception as e:
                print("in phone", e)
            m = b.send_message(message.chat.id, text="Введите ваш email", reply_markup=return_markup())
            b.register_next_step_handler(m, get_email)

    except Exception as e:
        print("get phone ex:", e)


def get_email(message):
    user_id = message.from_user.id
    if message.text.__contains__('Вернуться') or message.text.__contains__("start"):
        b.clear_step_handler_by_chat_id(message.chat.id)

        send_index(message=message)
    else:
        try:
            # b.delete_message(message.from_user.id, message.message_id)
            b.delete_message(message.from_user.id, message.message_id - 1)
        except Exception as e:
            print("in email", e)
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        print("get_email:", message.text)
        try:
            if re.search(regex, message.text):
                try:
                    b.delete_message(message.from_user.id, message.message_id)
                    # b.delete_message(message.from_user.id, message.message_id - 1)
                except Exception as e:
                    print("in email 2", e)
                print("Valid Email")
                user = user_data[user_id]
                user.email = message.text
                print(user.email)

                send_trading_plans(user_id)
            else:
                print("Invalid Email")
                try:
                    b.delete_message(message.from_user.id, message.message_id)
                    # b.delete_message(message.from_user.id, message.message_id - 1)
                except Exception as e:
                    print("in email 3", e)
                back_msg = b.send_message(message.chat.id, "Введите корректный email: ", reply_markup=return_markup())
                b.register_next_step_handler(back_msg, get_email)

        except Exception as e:
            print("get_email ex:", e)


def start_payment(user_id, plan, call):
    try:
        user = user_data[user_id]

        summa = f'{price_list.get(plan)}'

        payment_link = client.generate_payment_link(order_id=f'{user_id}', summ=summa,
                                                    email=f'{user.email}',
                                                    description=price_answers.get(plan))
        b.answer_callback_query(call.id, text=bonus_list.get(plan), show_alert=True)
        b.send_message(user_id, f"Вы выбрали тариф <b>{price_answers.get(plan)}</b>\n\n",
                       parse_mode="HTML",
                       reply_markup=payment_key(price=price_list.get(plan), payment_link=payment_link))

        key = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

        check_payment = types.KeyboardButton(text='Проверить оплату')
        cancel_btn = types.KeyboardButton('Вернуться')
        key.add(check_payment)
        key.add(cancel_btn)

        msg = b.send_message(user_id, text="Проверьте оплату", reply_markup=key)
        b.register_next_step_handler(msg, checkPay)

    except Exception as e:
        print("start_payment ex", e)


def checkPay(message):
    try:
        if message.text.__contains__('Вернуться') or message.text.__contains__("start"):
            try:
                b.delete_message(message.from_user.id, message.message_id)
                b.delete_message(message.from_user.id, message.message_id - 1)
            except Exception as e:
                print(e)
            send_index(message=message)
            b.clear_step_handler_by_chat_id(message.chat.id)
        else:
            user_id = message.from_user.id
            user = user_data[user_id]
            # pay_result = 'completed'
            print(message.from_user.username)
            if check__payment(user_id):
                try:
                    b.delete_message(message.from_user.id, message.message_id)
                    b.delete_message(message.from_user.id, message.message_id - 1)
                    # b.delete_message(message.from_user.id, message.message_id - 2)
                except Exception as e:
                    print("3 dell ex:", e)
                # Payment success
                b.send_message(message.chat.id, text='Оплата прошла успешно!')

                db_user = get_user(user_id)
                if db_user:
                    if db_user.trial == "Yes":
                        remove_exp_date(user_id)

                        db_user.delete()
                        session.commit()
                    elif db_user.trial == "No":
                        remove_exp_date(user_id)

                if not db_user:
                    add_user(user_id, user.phone_number, user.email,
                             first_name=user.first_name,
                             last_name=user.last_name,
                             username=user.username, trial="No")
                b.unban_chat_member(group, user_id)

                add_exp_date(user_id, user.plan)

                b.send_message(user_id, "Платеж успешно получен\n\n"
                                        f"Ссылка на канал - {trading_group_link}")

            # elif pay_result == 'new':
            #     # payment status NEW
            #     key = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            #
            #     check_payment = types.InlineKeyboardButton(text='Проверить оплату', callback_data='check_pay')
            #     cancel_btn = types.KeyboardButton('Вернуться')
            #     key.add(check_payment)
            #     key.add(cancel_btn)
            #     msg = b.send_message(message.chat.id, text='Оплата в обработке', reply_markup=key)
            #     b.register_next_step_handler(msg, checkPay)

            else:

                try:
                    b.delete_message(user_id, message.message_id)
                except Exception as e:
                    print(e)
                msg = b.send_message(message.chat.id, text="Оплата не найдена", reply_markup=check_pay_key())
                b.register_next_step_handler(msg, checkPay)

    except Exception as e:
        print(e)


b.enable_save_next_step_handlers(delay=2)
b.load_next_step_handlers()

if __name__ == '__main__':
    run_bot()
