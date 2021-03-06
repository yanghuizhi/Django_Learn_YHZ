### Django介绍说明

```
# 1、创建工程
>>> django-admin.py startproject 工程名 .      # 如果报错，则 django-admin 代替 django-admin.py 试试

# 2、创建应用 
>>> python manage.py startapp  app01           # 如果报错，则 django-admin.py startapp app_name

# 3、配置静态文件，project.settings.py
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 创建一些数据库表，在model创建
>>> python manage.py makemigrations     # 生成迁移文件
>>> python manage.py migrate    # 利用迁移文件生成表，就可以在数据库中查看

# 设置用户名和密码：（创建管理员）
>>> python manage.py createsuperuser            # 然后在网址后面加后缀 .../admin 进行登陆

# 启动说明：（三种方式）
>>> python manage.py runserver                     # 默认模式
>>> python manage.py runserver 8000                # 指定端口号
>>> python manage.py runserver 127.0.0.1:8000      # 指定地址
```

### Django目录说明
```
django-admin.py     # 是Django的一个用于管理任务的命令行工具；

Djangoyhz                             # 项目的容器 Django Project
    |-- Djangoyhz                     # 对整个程序进行配置，包含着你的项目，纯python包
        ┗━━ __init__.py             # 默认一个包文件
        ┗━━ settings.py             # 配置文件，包括数据库信息，调试标志以及其他一些工作的变量。
        ┗━━ urls.py                 # 映射项目中的路由和路径
        ┗━━ wsgi.py                 # 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。uwsgi+nginx
    |-- manage.py                      # 管理 Django 程序。
    |-- templates (自己创建的文件夹)    # 中的函数渲染templates中的Html模板，得到动态内容的网页，当然可以用缓存来提高速度。

APP
    |-- migrations       # Django会存储一些文件以跟踪你在models.py文件中创建的变更，用来保持数据库和models.py的同步。
        ┗━━ __init__.py
    |-- admin.py         # Django为我们提供了后台管理，包括数据库信息，调试标志以及其他一些工作的变量。
    |-- apps.py          # 这是应用程序本身的配置文件
    |-- models.py        # 定义Web应用程序数据实例的地方。models会由Django自动转换为数据库表。
    |-- tests.py         # 单元测试
    |-- views.py         # 这是我们处理Web应用程序请求(request)/响应(resopnse)周期的文件。
```


简单说一下使用：
    views：配置视图
        templates：配置网页，最终路径指向上面
    urls：指向前面的viwes
    然后启动服务

### 杂：
```
python -m django --version  # 查看版本
python manage.py test --verbosity=2  # 测试，0无输出，1正常输出，2详细输出

```

### 项目 VS 应用

项目和应用有啥区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

### 问题
如果在pycharm中启动manage.py失败，则请开启Edit configgurations，并在parameters里面设置脚本路径 比如 runserver 127.0.0.1:8000