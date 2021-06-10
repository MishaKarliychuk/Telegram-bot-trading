#!/usr/bin/python


from db import get_dates, remove_exp_date, remove_payment
from datetime import date
from telebot import TeleBot
from config import bot_token
from keyboards import update_subscribe

b = TeleBot(bot_token)


def check_exp_date():
    x = get_dates()

    for ten in x[0]:

        if ten[1] == str(date.today()):
            try:
                m = b.send_message(ten[0], f"Ваша подписка на канал по трейдингу заканчивается через 10 дней - "
                                           f"<b>{ten[1]}</b>\n\n"
                                           f"Чтобы продлить подписку - перейдите по ссылке",
                                   reply_markup=update_subscribe(), parse_mode="HTML")
                print(m.chat, m.text)
            except Exception as e:
                print(e)

    for seven in x[1]:
        if seven[1] == str(date.today()):
            try:
                m = b.send_message(seven[0], f"Ваша подписка на канал по трейдингу заканчивается через 7 дней - "
                                             f"<b>{seven[1]}</b>\n\n"
                                             f"Чтобы продлить подписку - перейдите по ссылке",
                                   reply_markup=update_subscribe(), parse_mode="HTML")
                print(m.chat, m.text)
            except Exception as e:
                print(e)

    for four in x[2]:
        if four[1] == str(date.today()):
            try:
                m = b.send_message(four[0],
                                   f"Ваша подписка на канал по трейдингу заканчивается через 4 дня - <b>{four[1]}</b>\n\n"
                                   f"Чтобы продлить подписку - перейдите по ссылке",
                                   reply_markup=update_subscribe(), parse_mode="HTML")
                print(m.text, m.chat)
            except Exception as e:
                print(e)

    for one in x[3]:
        if one[1] == str(date.today()):
            try:
                m = b.send_message(one[0],
                                   f"Ваша подписка на канал по трейдингу заканчивается завтра - <b>{one[1]}</b>\n\n"
                                   f"Чтобы продлить подписку - перейдите по ссылке",
                                   reply_markup=update_subscribe(), parse_mode="HTML")
                print(m.text, m.chat)
            except Exception as e:
                print(e)

    for exp_date in x[4]:
        if exp_date[1] == str(date.today()):
            remove_exp_date(exp_date[0])
            remove_payment(exp_date[0])
            try:
                b.kick_chat_member(-1001397949389, user_id=exp_date[0])
                print(exp_date[0], "was kicked!")
            except Exception as e:
                print("kick error =", e)
            try:
                m = b.send_message(exp_date[0], f"Ваша подписка на канал по трейдингу закончилась!\n\n"
                                                f"Чтобы купить подписку - перейдите по ссылке",
                                   reply_markup=update_subscribe(), parse_mode="HTML")
                print(m.text, m.chat)

            except Exception as e:
                print(e)


if __name__ == '__main__':
    check_exp_date()
