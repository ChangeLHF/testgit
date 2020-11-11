
from flask import Blueprint, redirect, url_for, session, render_template, flash, g

from forms import LoginForm
from models import User

accounts=Blueprint('accounts',__name__,
                   template_folder='templates',
                   static_folder='static')



@accounts.route('/user/login', methods=['GET','POST'])
def login():
    '''用户登录'''
    form=LoginForm()
    if form.validate_on_submit():
        #获取用户输入的用户名和密码
        username=form.username.data
        password=form.password.data
        print(username,password)
        #查询数据库中的用户名和密码进行匹配
        user=User.query.filter_by(username=username,password=password).first()
        if user is None:
            flash('输入用户名或密码错误','danger')
        else:
            session['user_id']=user.id
            flash('欢迎回来','success')
            return redirect(url_for('index'))
    else:
        print(form.errors)

    return render_template('login.html', form=form)

@accounts.route('/logout')
def logout():
    """退出登录"""
    g.user=None
    session['user_id']=None
    flash('成功退出登录','success')
    return redirect(url_for('accounts.login'))