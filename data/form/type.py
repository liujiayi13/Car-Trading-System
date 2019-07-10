from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class TypeModelForm(ModelForm):
    class Meta:
        model = models.Cartype
        fields = "__all__"
        widgets = {
            'type':forms.TextInput(attrs={'class':'form-control','placeholder':'类别'}),

        }
        error_messages = {
            'type':{
                'required':'类别不能为空'
            },
        }