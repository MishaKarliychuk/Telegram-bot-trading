#!/usr/bin/python


import sys
import os

from config import bot_token
from db import get_post, delete_post, cron
from telebot.types import InputMediaPhoto, InputMediaDocument, InputMediaVideo
from telebot import TeleBot
b = TeleBot(bot_token)


def send_channel_post(post_id):
    post = get_post(int(post_id))
    medias = []
    print("\nLEN str:", len(post.text))

    if post.images_path and not post.images_path.startswith("https"):

        cat_names = os.walk(f'./post_media/{post.post_id}/photos/')
        for name in cat_names:
            for n, item in enumerate(name[2]):
                print(n, item)
                file_path = f"./post_media/{post.post_id}/photos/{item}"
                file = open(file_path, 'rb')
                if n == 0:
                    medias.append(InputMediaPhoto(media=file, caption=post.text, parse_mode="HTML"))
                else:
                    medias.append(InputMediaPhoto(media=file, caption=None, parse_mode="HTML"))
                # file.close()
            print("\nIMAGE medias:", medias)

            b.send_media_group(post.group_id, medias)
            medias.clear()

            if post.file_path:
                cat_names = os.walk(f'./post_media/{post.post_id}/documents/')
                for name in cat_names:
                    for n, item in enumerate(name[2]):
                        file_path = f"./post_media/{post.post_id}/documents/{item}"
                        file = open(file_path, 'rb')
                        medias.append(InputMediaDocument(media=file, caption=None))
                try:
                    b.send_media_group(post.group_id, medias)
                except Exception as e:
                    print("\nSend files err:", e)
                medias.clear()
    elif post.images_path.startswith("https"):

        b.send_message(post.group_id, post.text + "\n" + f"""<a href="{post.images_path}">&#8203;</a>""",
                       parse_mode="HTML")

    elif post.video_path:
        cat_names = os.walk(f'./post_media/{post.post_id}/videos/')
        for name in cat_names:
            for n, item in enumerate(name[2]):
                print("\nVideo N", n)
                file_path = f"./post_media/{post.post_id}/videos/{item}"
                file = open(file_path, 'rb')
                if not post.images_path and n == 0:
                    medias.append(InputMediaVideo(media=file, caption=post.text))

                elif not post.images_path and n > 1:
                    medias.append(InputMediaVideo(media=file, caption=None))
                elif post.images_path:
                    medias.append(InputMediaVideo(media=file, caption=None))

        print("\nIMAGE + VIDEO medias:", medias)

        b.send_media_group(post.group_id, medias)
        medias.clear()

        if post.file_path:
            cat_names = os.walk(f'./post_media/{post.post_id}/documents/')
            for name in cat_names:
                for n, item in enumerate(name[2]):
                    file_path = f"./post_media/{post.post_id}/documents/{item}"
                    file = open(file_path, 'rb')
                    medias.append(InputMediaDocument(media=file, caption=None))
            try:
                b.send_media_group(post.group_id, medias)
            except Exception as e:
                print("\nSend files err:", e)
            medias.clear()

    elif post.file_path and not post.images_path:
        cat_names = os.walk(f'./post_media/{post.post_id}/documents/')
        for name in cat_names:
            for n, item in enumerate(name[2]):
                file_path = f"./post_media/{post.post_id}/documents/{item}"
                file = open(file_path, 'rb')
                if n == 0:
                    medias.append(InputMediaDocument(media=file, caption=post.text, parse_mode="HTML"))
                else:
                    medias.append(InputMediaDocument(media=file, caption=None, parse_mode="HTML"))

        b.send_media_group(post.group_id, medias)
        medias.clear()

    else:
        b.send_message(post.group_id, post.text, parse_mode="HTML", disable_web_page_preview=True)


if __name__ == '__main__':
    send_channel_post(post_id=sys.argv[1])
    post = get_post(int(sys.argv[1]))

    if post.post_type == "today":
        delete_post(post.id)
        cron.remove_all(comment=post.post_id)
        cron.write()