from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class FirmModelForm(ModelForm):
    class Meta:
        model = models.Carfirm
        fields = "__all__"
        widgets = {
            'firm':forms.TextInput(attrs={'class':'form-control','placeholder':'厂商'}),

        }
        error_messages = {
            'firm':{
                'required':'厂商不能为空'
            },
        }