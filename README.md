# CarManagementSystem

这是一个用Django开发的二手车交易系统，
用户可以注册，登陆和注销，有三种用户，分别为买家，卖家和管理员。
卖家发布车辆出售信息，并且可删除或者编辑。
买家可以搜索车辆相关信息选择合适的车购买。
管理员可以对违规出售信息进行删除或者编辑。

要进入网页界面，请先从shell进入文件夹，
然后按顺序输入

`pip install django`

`pip install pymysql`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

要注册管理员，请输入

`python manage.py createsuperuser`

并输入用户名和密码（此时密码不可见）

再在浏览器中输入http://127.0.0.1:8000/data/login 即可注册登陆并访问网站！
