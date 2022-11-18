from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import datetime
import yaml


app = Flask(__name__)
db = yaml.full_load(open('db.yml'))

#mysql://username:password@host:port/database_name
connection_str='mysql://'+db['mysql_user']+':'+db['mysql_password']+'@'+db['mysql_host']+'/'+db['mysql_db']
app.config['SQLALCHEMY_DATABASE_URI']=connection_str
print(connection_str)


db = SQLAlchemy(app)


class Visitor(db.Model):
    accessed_at=db.Column(db.Float,primary_key=True)
    user_id=db.Column(db.Integer)
    page_id=db.Column(db.Integer)

    def __init__(self,accessed_at,user_id,page_id):
        self.accessed_at=accessed_at
        self.user_id=user_id
        self.page_id=page_id




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        visitor=Visitor(datetime.datetime.now().timestamp(),1000,5)
        db.session.add(visitor)
        db.session.commit()
        print(Visitor.query.all())

