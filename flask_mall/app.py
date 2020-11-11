from accounts.views import accounts
from mall.views import mall
from models import User, db

from flask import Flask, render_template, session, g

app = Flask(__name__)
app.config.from_object('conf.Config')
#使用ORM
db.init_app(app)
#注册蓝图对象
app.register_blueprint(accounts,url_prefix='/accounts')
app.register_blueprint(mall,url_prefix='/mall')


# app.config['WTF_SCRF_SECRET_KEY']='ALDKFJSLFJS123'
# app.config['SECRET_KEY']='ALDKFJSLFJS123'#可以相同，也可以只写这一个
#
# #文件上传目录
# app.config['UPLOAD_PATH']=os.path.join(os.path.dirname(__file__),'medias')


@app.before_request
def before_request():
    #如果有用户的话 设置到全局变量g里面去
    user_id=session.get('user_id',None)
    if user_id:
        user=User.query.get(user_id)
        print(user)
        g.user=user
        print(g.user.nickname)


@app.route('/')
def index():
    # 主页
    return render_template('index.html')