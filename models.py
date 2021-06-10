from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
DBengine = "sqlite:///data.db"

engine = create_engine(DBengine, connect_args={'check_same_thread': False})
Base = declarative_base(bind=engine)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    username = Column(String(100))
    phone_number = Column(Integer)
    email = Column(String(100))
    trial = Column(String(20))

    def __init__(self, user_id, phone_number, email, first_name=None, last_name=None, username=None, trial=None, *args,
                 **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.trial = trial

    def __repr__(self):
        return f"""<user_id = {self.user_id}, username = {self.username}, 
                first_name = {self.first_name}, last_name = {self.last_name},
                phone = {self.phone_number}, email = {self.email}, trial = {self.trial}>"""


class Payments(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    phone = Column(String(20))
    email = Column(String(100))
    amount = Column(Integer)
    int_id = Column(Integer)

    def __init__(self, user_id, phone, email, amount, int_id, *args, **kwargs):
        super(Payments, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.phone = phone
        self.email = email
        self.amount = amount
        self.int_id = int_id

    def __repr__(self):
        return f"<Payment: user_id = {self.user_id}>, phone = {self.phone}," \
               f" email = {self.email}, amount = {self.amount}"


class Subscribe_exp(Base):
    __tablename__ = 'subscribe'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    ten = Column(String(10))
    seven = Column(String(10))
    four = Column(String(10))
    one = Column(String(10))
    exp_day = Column(String(10))

    def __init__(self, user_id, ten=None, seven=None, four=None, one=None, exp_day=None, *args, **kwargs):
        super(Subscribe_exp, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.ten = ten
        self.seven = seven
        self.four = four
        self.one = one
        self.exp_day = exp_day

    def __repr__(self):
        return f"user_id = {self.user_id}"


# class Action(Base):
#     __tablename__ = 'Actions'
#     id = Column(Integer, primary_key=True)
#     symbol = Column(String(20))
#     members = Column(String(1000))
#     post_id = Column(Integer, ForeignKey('Posts.id'))
#
#     def __init__(self, symbol):
#         self.symbol = symbol
#
#     def __repr__(self):
#         return f"<Post({self.post_id}, {self.symbol})>"


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    post_id = Column(Integer)
    tg_post_id = Column(Integer)
    group_id = Column(String(255))
    text = Column(String(4096))
    images_path = Column(String(1000))
    video_path = Column(String(1000))
    file_path = Column(String(1000))
    # act = relationship("Action")
    time = Column(String(20))
    post_type = Column(String(20))

    def __init__(self, group_id, user_id, post_id, text, time, img, video, file, post_type=None):
        self.user_id = user_id
        self.post_id = post_id
        self.group_id = group_id
        self.text = text
        self.images_path = img
        self.video_path = video
        self.file_path = file
        self.time = time
        self.post_type = post_type

    def __repr__(self):
        return f"\n<Post_id: {self.post_id}\n" \
               f"TG_GROUP_ID: {self.group_id}\n" \
               f"Time: {self.time}\n" \
               f"TEXT: {self.text}\n" \
               f"IMG: {self.images_path}\n" \
               f"VIDEO: {self.video_path}\n" \
               f"TIME: {self.time}\n" \
               f"DOCS: {self.file_path}\n" \
               f"POST TYPE: {self.post_type}>\n"


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
    img_path = Column(String(500))


Base.metadata.create_all(bind=engine)