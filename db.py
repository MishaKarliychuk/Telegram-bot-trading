import getpass
import shutil

from models import *
from sqlalchemy.orm.session import sessionmaker

from datetime import date
from dateutil.relativedelta import relativedelta
from crontab import CronTab
from answers import plan_exp

six_months = date.today() + relativedelta(months=+6)
try:
    cron = CronTab(user=getpass.getuser())
except:
    pass
Session = sessionmaker(bind=engine)
session = Session()


def add_user(user_id, phone_number, email, first_name=None, last_name=None, username=None, trial=None):
    try:
        user = Users(user_id, phone_number, email, first_name, last_name, username, trial)

        session.add(user)
        session.commit()

        print(user, "was added")
    except Exception as e:
        print("\nadd user ex:", e)


def get_user(user_id):
    try:
        user = session.query(Users).filter(Users.user_id == user_id).first()
        return user

    except Exception as e:
        print("get_user ex:", e)
        return None


def check_trial(user_id):
    try:
        db_user = session.query(Users).filter(Users.user_id == user_id).first()
        if db_user.trial == "Yes" or db_user.trial == "No":
            return True
        else:
            return False
    except Exception as e:
        print("\ncheck_trial:", e)


def get_id_from_db():
    try:
        id_list = []

        users_list = session.query(Users.user_id).filter(Users.user_id).all()
        # print("\nget_id_from_db:", users_list)

        for user_id in users_list:
            id_list.append(user_id[0])

        return id_list

    except Exception as e:
        print("\nget_user:", e)


def get_id_from_expire():
    try:
        id_list = []
        users_list = session.query(Subscribe_exp.user_id).all()
        # print("\nget_id_from_expire:", users_list)
        for user_id in users_list:
            id_list.append(user_id[0])

        return id_list

    except Exception as e:
        print("\nget_id_from_expire:", e)


def add_payment(user_id, phone, email, amount, int_id):
    payment = Payments(user_id, phone, email, amount, int_id)
    session.add(payment)
    session.commit()


def check__payment(user_id):
    try:
        payment = session.query(Payments).filter(Payments.user_id == user_id).first()
        session.commit()
        return payment
    except Exception as e:
        print("check_payment", e)


def remove_payment(user_id):
    try:
        payment = session.query(Payments).filter(Payments.user_id == user_id).delete()
        session.commit()
        return payment
    except Exception as e:
        print("remove_payment", e)


def add_exp_date(user_id, plan):
    try:
        remove_exp_date(user_id)
    except Exception as e:
        print(e)
    exp_day = date.today() + relativedelta(days=+plan_exp.get(plan))

    ten = date.today() + relativedelta(days=+plan_exp.get(plan) - 10)
    seven = date.today() + relativedelta(days=+plan_exp.get(plan) - 7)
    four = date.today() + relativedelta(days=+plan_exp.get(plan) - 4)
    one = date.today() + relativedelta(days=+plan_exp.get(plan) - 1)

    print(date.today(), ten, seven, four, one, exp_day)

    exp_date = Subscribe_exp(user_id=user_id,
                             ten=str(ten),
                             seven=str(seven),
                             four=str(four),
                             one=str(one),
                             exp_day=str(exp_day))
    session.add(exp_date)
    session.commit()

def add_exp_date_for_admin(user_id, plan):
    try:
        remove_exp_date(user_id)
    except Exception as e:
        print(e)
    exp_day = date.today() + relativedelta(days=+plan)

    ten = date.today() + relativedelta(days=+plan-10)
    seven = date.today() + relativedelta(days=+plan-7)
    four = date.today() + relativedelta(days=+plan-4)
    one = date.today() + relativedelta(days=+plan-1)

    print(date.today(), ten, seven, four, one, exp_day)

    exp_date = Subscribe_exp(user_id, str(ten), str(seven), str(four), str(one), str(exp_day))
    session.add(exp_date)
    session.commit()


def add_trial(user_id, plan):
    print(user_id, plan)
    if user_id in get_id_from_expire():
        print(user_id, "already in base")
    else:
        exp_day = date.today() + relativedelta(days=+plan_exp.get(plan))

        four = date.today() + relativedelta(days=+plan_exp.get(plan) - 4)
        one = date.today() + relativedelta(days=+plan_exp.get(plan) - 1)

        print(date.today(), four, one, exp_day)

        exp_date = Subscribe_exp(user_id=user_id, four=str(four), one=str(one), exp_day=str(exp_day))
        session.add(exp_date)
        session.commit()


def remove_exp_date(user_id):
    try:
        db_user = session.query(Subscribe_exp).filter(Subscribe_exp.user_id == user_id).delete()
        print(db_user)
        db_user.trial = 'expired'

        session.commit()
        if db_user == 1:
            print(user_id, "removed")
        elif db_user == 0:
            print("no user_id =", str(user_id))
    except Exception as e:
        print("no user_id =", str(user_id) + "\n", e)


def remove_trial_user(user_id):
    try:
        db_user = session.query(Users).filter(Users.user_id == user_id).first()

        db_user.trial = 'Expired'
        session.commit()
        print(user_id, "trial removed")

    except Exception as e:
        print("\nno user_id =" + str(user_id) + "\n", e)


def get_dates():
    return session.query(Subscribe_exp.user_id, Subscribe_exp.ten).all(), \
           session.query(Subscribe_exp.user_id, Subscribe_exp.seven).all(), \
           session.query(Subscribe_exp.user_id, Subscribe_exp.four).all(), \
           session.query(Subscribe_exp.user_id, Subscribe_exp.one).all(), \
           session.query(Subscribe_exp.user_id, Subscribe_exp.exp_day).all()


def create_post(user_id, group_id, post_id, text, time, img, video, file, post_type=None):
    post = Post(group_id=group_id,
                user_id=user_id,
                post_id=post_id,
                text=text,
                time=time,
                img=img,
                video=video,
                file=file,
                post_type=post_type)
    session.add(post)
    session.commit()
    print(post, "CREATED")


def get_post(post_id):
    try:
        # print("get_post_id", post_id, type(post_id))
        post = session.query(Post).filter(Post.post_id == int(post_id)).first()
        print("\nPOST:", post.__repr__())
        return post
    except Exception as e:
        print(f"\nPost {post_id}, not found:", e)


def get_posts(start=0, stop=5):
    posts = session.query(Post)[start:stop]
    # print(posts)
    if posts[0]:
        return posts
    else:
        return None


def get_all_posts():
    posts = session.query(Post).all()
    # print(posts)
    if posts[0]:
        return posts
    else:
        return None


def delete_post(post_id):
    try:

        post = session.query(Post).filter(Post.id == post_id).first()
        post_id = post.post_id
        shutil.rmtree(f"./post_media/{post_id}/", ignore_errors=True)
        session.delete(post)
        print("\nCRON_USER:", cron.user)
        job = cron.find_comment(str(post_id))
        res = cron.remove(job)
        print(res)
        cron.write(user=getpass.getuser())
        print()

        for j in cron:
            print(j)
        session.commit()

        print(f"\nPost {post_id} was deleted")

    except Exception as e:
        print(f"\nPost {post_id}, not found:", e)
