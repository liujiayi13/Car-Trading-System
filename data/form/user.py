from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class UserModelForm(ModelForm):
    class Meta:
        model = models.UserManager
        fields = "__all__"
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'密码'}),
            'usertype':forms.TextInput(attrs={'class':'form-control','placeholder':'用户类型'}),

        }
        error_messages = {
            'username':{
                'required':'姓名不能为空'
            },
            'password': {
                'required': '密码不能为空'
            },
            'usertype': {
                'required': '用户类型不能为空'
            },
        }