from django.conf.urls import url,include
from django.contrib import admin
from  data.views import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', home.index),

    url(r'^login/', home.login),
    url(r'^register/', home.register),

    url(r'^selllist/', home.selllist),
    url(r'^search/', home.search),
    url(r'^buy/(\d+)/', home.buy),

    url(r'^addsell/', home.addsell),
    url(r'^editsell/(\d+)/', home.editsell),
    url(r'^delsell/(\d+)/', home.delsell),





    url(r'^buylist/', home.buylist),

    url(r'^carlist/', home.carlist),
    url(r'^editcar/(\d+)/', home.editcar),
    url(r'^delcar/(\d+)/', home.delcar),


    url(r'^typelist/', home.typelist),
    url(r'^addtype/', home.addtype),
    url(r'^edittype/(\d+)/', home.edittype),
    url(r'^deltype/(\d+)/', home.deltype),
    url(r'^firmlist/', home.firmlist),
    url(r'^addfirm/', home.addfirm),
    url(r'^editfirm/(\d+)/', home.editfirm),
    url(r'^delfirm/(\d+)/', home.delfirm),


    url(r'^userlist/', home.userlist),
    url(r'^adduser/', home.adduser),
    url(r'^edituser/(\d+)/', home.edituser),
    url(r'^deluser/(\d+)/', home.deluser),




    url(r'^menulist/', home.menulist),
    # url(r'^editmenu/(\d+)/', home.editmenu),
    url(r'^delmenu/(\d+)', home.delmenu),

]