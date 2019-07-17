from data  import  models
from django.forms import ModelForm
from django import  forms
#校验输入的设备信息字段不能为空
class SellModelForm(ModelForm):
    class Meta:
        model = models.CarInfo
        fields = "__all__"
        widgets = {
            'carname':forms.TextInput(attrs={'class':'form-control','placeholder':'名称'}),
            'carfirm':forms.Select(attrs={'class':'form-control','placeholder':'经销商'}),
            'cartype':forms.Select(attrs={'class':'form-control','placeholder':'类别'}),
            'carsell':forms.TextInput(attrs={'class':'form-control','placeholder':'车主姓名'}),
            'carphone':forms.TextInput(attrs={'class':'form-control','placeholder':'电话'}),
            'carsize':forms.TextInput(attrs={'class':'form-control','placeholder':'价格'}),
            'carbetter':forms.TextInput(attrs={'class':'form-control','placeholder':'优惠'}),
            'carother':forms.TextInput(attrs={'class':'form-control','placeholder':'里程信息'}),
            'carage':forms.TextInput(attrs={'class':'form-control','placeholder':'车龄信息'}),
            'catstatus':forms.Select(attrs={'class':'form-control','placeholder':'成交状态'}),

        }
        error_messages = {
            'carname':{
                'required':'名称不能为空'
            },
            'carfirm': {
                'required': '经销商不能为空'
            },
            'cartype': {
                'required': '类别不能为空'
            },
            'carsell': {
                'required': '姓名不能为空'
            },
            'carphone': {
                'required': '电话不能为空'
            },
            'carsize': {
                'required': '价格不能为空'
            },
            'carbetter': {
                'required': '优惠不能为空'
            },
            'carother': {
                'required': '里程信息不能为空'
            },
            'carage': {
                'required': '车龄信息不能为空'
            },
            'catstatus': {
                'required': '成交状态不能为空'
            },
        }