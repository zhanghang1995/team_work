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
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    def __repr__(self):
        return "<User %r>"%self.username


#用于测试

# if __name__ == "__main__":
#     db.create_all()
#     user = Test(
#         username="kingdom",
#         password="king"
#     )
#     db.session.add(user)
#     db.session.commit()



