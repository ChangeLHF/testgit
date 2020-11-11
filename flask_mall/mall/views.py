from functools import wraps

from flask import Blueprint, flash, redirect, url_for, render_template, request, abort, session

from forms import ProductEditForm
from models import Product, db

mall=Blueprint('mall',__name__,
                   template_folder='templates',
                   static_folder='static')

def login_required(viwe_func):
    """登录验证"""
    @wraps(viwe_func)
    def wrapper(*args,**kwargs):
        user_id=session.get('user_id',None)
        if not user_id:
            return redirect(url_for('accounts.login'))
        return viwe_func(*args,**kwargs)
    return wrapper

@mall.route('/product/add',methods=['GET','POST'])
def product_add():
    '''商品添加'''
    form=ProductEditForm()
    # 判断表单是否验证通过
    if form.validate_on_submit():
        # 保存到数据库
        data=form.data
        for item,value in data.items():
            print(item,":",value)
        product_obj=Product(
        # 商品名称
        name=data['name'],
        # 商品描述（富文本）
        content = data['content'],
        # 商品推荐语
        desc = data['desc'],
        # 类型
        types = data['types'],
        # 价格
        price = data['price'],
        # 原价
        origin_price = data['origin_price'],
        # 主图
        img = '/xxx.jpg',
        # 渠道
        channel = data['channel'],
        # 链接
        buy_link = data['buy_link'],
        # 商品状态
        status = data['status'],
        # 库存
        sku_count = data['sku_count'],
        # 剩余库存
        remain_count = data['remain_count'],
        # 浏览
        view_count = data['view_count'],
        # 评分
        score = data['score'],

        # 逻辑删除
        is_valid = data['is_valid'],
        # 排序
        reorder = data['reorder'],
        )
        db.session.add(product_obj)
        db.session.commit()
        flash("新增商品成功",'success')
        #成功跳转到商品列表里去
        return redirect(url_for('mall.product_list',page=1))

    else:
        # 消息提示
        flash("请修改页面中的错误，然后提交",'warning')
        print(form.errors)

    return render_template('product_add.html', form=form)



@mall.route('/product/list/<int:page>')
@login_required     #建议使用flask-login来代替
def product_list(page):
    # 商品列表
    page_size=3
    #搜索条件的查询
    name=request.args.get('name')
    print('name---',name)
    if name:
        page_data = Product.query.filter(Product.name.contains(name),Product.is_valid==False)\
            .paginate(page=page,per_page=page_size)
    else:
        page_data=Product.query.filter(Product.is_valid==False)\
            .paginate(page=page,per_page=page_size)

    return render_template('product_list.html', page_data=page_data)


@mall.route('/product/detail/<string:uid>')
def product_detail(uid):
    '''商品详情'''
    #todo 如果触发了404 就需要定制404页面
    prod_obj=Product.query.filter_by(uid=uid).first_or_404()
    print(prod_obj)
    return render_template('product_detail.html', prod_obj=prod_obj)


@mall.route('/product/edit/<string:uid>', methods=['GET','POST'])
def product_edit(uid):
    '''商品编辑'''
    #查询商品
    prod_obj=Product.query.filter_by(uid=uid,is_valid=False).first()
    if prod_obj is None:
        abort(404)
    form=ProductEditForm(obj=prod_obj)
    # 修改商品内容
    if form.validate_on_submit():
        # 保存到数据库
        prod_obj.name=form.name.data
        prod_obj.content=form.data['content']
        db.session.add(prod_obj)
        db.session.commit()
        flash('修改成功','success')
        return redirect(url_for('mall.product_list',page=1))
    else:
        print(form.errors)
    return render_template('product_edit.html', form=form, prod_obj=prod_obj)



@mall.route('/product/delete/<string:uid>',methods=['GET','POST'])
def product_delete(uid):
    '''商品删除'''
    prod_obj=Product.query.filter_by(uid=uid,is_valid=False).first()
    print(prod_obj)
    if prod_obj is None:
        return 'no'
    prod_obj.is_valid=True
    db.session.add(prod_obj)
    db.session.commit()
    return 'ok'
