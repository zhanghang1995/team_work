#coding:utf8

from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = "user_info"
    __table_args__ = {"useexisting": True}
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.INTEGER,primary_key=True)
    username = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    phone = db.Column(db.String(100),unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow())
    uuid = db.Column(db.String(255),unique=True)

    def __repr__(self):
        return "<User %r>"%self.username

class Test(db.Model):
    __tablename__ = 'test'
    __table_args__ = {"useexisting": True}
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    def __repr__(self):
        return "<User %r>"%self.username
    def check_pwd(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

#用于测试
class Remind(db.Model):
    __tablename__ = 'life_remind'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.INTEGER,primary_key=True)
    getup = db.Column(db.time)
    breakfast = db.Column(db.varchar(150))
    readnews = db.Column(db.varchar(120))
    newspush = db.Column(db.varchar(120))
    cheat = db.Column(db.text)
    gowork = db.Column(db.text)
    work = db.Column(db.text)
    lunch = db.Column(db.varchar(150))
    lunchbreak = db.Column(db.time)
    workarrangement = db.Column(db.text)
    worksummary = db.Column(db.text)
    dinner = db.Column(db.varchar(150))
    eveactivities = db.Column(db.varchar(150))
    sleep = db.Column(db.time)
    time = db.relationship('Time', backref='author', uselist=False)



class Time(db.Model):
    __tablename__ = 'time'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.INTEGER,primary_key=True)
    breakfast_t = db.Column(db.time)
    readnews_t = db.Column(db.time)
    newspush_t = db.Column(db.time)
    cheat_t = db.Column(db.time)
    gowork_t = db.Column(db.time)
    work_t = db.Column(db.time)
    lunch_t = db.Column(db.time)
    workarrangement_t = db.Column(db.time)
    worksummary_t = db.Column(db.time)
    dinner_t = db.Column(db.time)
    seveactivities_t = db.Column(db.time)
    remind_id_t = db.Column(db.INTEGER,db.ForeignKey('remind.id'))


# if __name__ == "__main__":
#     db.create_all()
#     user = Test(
#         username="kingdom520",
#         password="king"
#     )
#     db.session.add(user)
#     db.session.commit()



