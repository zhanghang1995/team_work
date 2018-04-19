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
    getup = db.Column(db.String(100))
    breakfast = db.Column(db.String(100))
    readnews = db.Column(db.String(120))
    newspush = db.Column(db.String(120))
    cheat = db.Column(db.String(120))
    gowork = db.Column(db.String(120))
    work = db.Column(db.String(120))
    lunch = db.Column(db.String(120))
    lunchbreak = db.Column(db.String(120))
    workarrangement = db.Column(db.String(120))
    worksummary = db.Column(db.String(120))
    dinner = db.Column(db.String(150))
    eveactivities = db.Column(db.String(150))
    sleep = db.Column(db.String(120))
    time = db.relationship('Time', backref='author', uselist=False)



class Time(db.Model):
    __tablename__ = 'time'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.INTEGER,primary_key=True)
    breakfast_t = db.Column(db.String(120))
    readnews_t = db.Column(db.String(120))
    newspush_t = db.Column(db.String(120))
    cheat_t = db.Column(db.String(120))
    gowork_t = db.Column(db.String(120))
    work_t = db.Column(db.String(120))
    lunch_t = db.Column(db.String(120))
    workarrangement_t = db.Column(db.String(120))
    worksummary_t = db.Column(db.String(120))
    dinner_t = db.Column(db.String(120))
    seveactivities_t = db.Column(db.String(120))
    remind_id_t = db.Column(db.INTEGER,db.ForeignKey('remind.id'))


# if __name__ == "__main__":
#     db.create_all()
#     user = Test(
#         username="kingdom520",
#         password="king"
#     )
#     db.session.add(user)
#     db.session.commit()



