from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, FloatField, \
    TextAreaField, SelectField, BooleanField, TimeField, PasswordField

import constants


class ProductEditForm(FlaskForm):
    """新增商品表单"""

    # 商品名称
    name = StringField(label='商品名称',render_kw={
        'class' : 'form-control',
        'placeholder':'请输入商品名称'
    },description='商品名称不超过200字')
    # 商品描述（富文本）
    content = TextAreaField(label='商品描述',render_kw={
        'class' : 'form-control',
        'placeholder':'请输入商品描述'
    },description='')
    # 商品推荐语
    desc = StringField(label='商品推荐语',render_kw={
        'class' : 'form-control',
        'placeholder':'请输入商品推荐语'
    },description='')
    # 类型
    types = SelectField(label='类型',
        choices=(constants.PRODUCT_TYPES),
        render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 价格
    price = IntegerField(label='价格',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 原价
    origin_price = FloatField(label='原价',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 主图
    img = FileField(label='主图')
    # 渠道
    channel = StringField(label='渠道',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 链接
    buy_link = StringField(label='链接',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 商品状态
    status = SelectField(label='商品状态',
        choices=(constants.PRODUCT_STATUS),
        render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 库存
    sku_count = IntegerField(label='库存',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 剩余库存
    remain_count = IntegerField(label='剩余库存',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 浏览
    view_count = IntegerField(label='浏览次数',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 评分
    score = IntegerField(label='评分',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')

    # 逻辑删除
    is_valid = BooleanField(label='逻辑删除')
    # 排序
    reorder = IntegerField(label='排序',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 创建时间
    created_at = TimeField(label='创建时间',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')
    # 最后修改的时间
    updated_at = TimeField(label='最后修改时间',render_kw={
        'class' : 'form-control',
        'placeholder':''
    },description='')


class LoginForm(FlaskForm):
    """登录表单"""
    username=StringField(label='用户名',render_kw={
        'class': 'form-control',
        'placeholder': '请输入用户名'
    })
    nickname=StringField(label='昵称')
    password=PasswordField(label='密码',render_kw={
        'class': 'form-control',
        'placeholder': '请输入密码'
    })

    def validate_username(self ,field):
        username=field.data
        #todo 验证
        return username