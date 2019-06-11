# main中的urls.py处理网站的所有链接
from django.urls import path
from . import views


app_name = "main"

# 处理链接跳转的函数写在views.py中
urlpatterns = [
    path("", views.home, name="home"),  # 主页
    path("lost/", views.lost, name="lost"),  # 发布寻物信息的页面
    path("found/", views.found, name="found"),  # 发布捡到物品信息的页面
    path("register/", views.register, name="register"),  # 注册页面
    path("log_in/", views.log_in, name="log_in"),  # 登录页面
    path("log_out/", views.log_out, name="log_out"),  # 登录页面
    path("user_center/", views.user_center, name="user_center"),  # 个人中心页面
    path("info_edit/", views.info_edit, name="info_edit"),  # 个人信息编辑页面
    path("change_password", views.change_password, name="change_password"),  # 修改密码
    path("passage_manage/", views.passage_manage, name="passage_manage"),  # 个人消息管理页面
    path("publish_lost/", views.publish_lost, name="publish_lost"),  # 发布丢失物品信息的页面
    path("publish_found/", views.publish_found, name="publish_found"),  # 发布捡到物品信息的页面
    path("item_return/<forloop_counter>", views.item_return, name="item_return"),  # 归还物品，同时作用于lost和found
]
