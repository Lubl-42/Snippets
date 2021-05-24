from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, NullBooleanSelect,EmailInput, PasswordInput, NumberInput
#from django import forms
from MainApp.models import Snippet, Comment, Account, Tarif, Elektro
from django.contrib.auth.models import User

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields= ['name', 'lang', 'code','visible']
        widgets = {
            'name': TextInput (attrs={"class": "form-control form-control-lg", "placeholder":"Название заметки"}),
            'lang': TextInput (attrs={"class": "form-control form-control-lg", "placeholder":"Тема кратко"}),
            'visible': NullBooleanSelect(attrs={"class": "form-control form-control-lg", "placeholder": "Публиковать да/нет"}),
            'code': Textarea (attrs={'cols':"96", 'rows':"10", 'placeholder':"Текст заметки"}),
                    }
        labels ={'name': ''}

class UserForm(ModelForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password']
        widgets = {
            'username': TextInput (attrs={"class": "form-control form-control-lg",
                                      "placeholder":"Имя автора"}),
            'email': EmailInput (attrs={"class": "form-control form-control-lg",
                                        "placeholder":"Email "}),
            'password': PasswordInput (attrs={'cols':"11", 'rows':"3", 'placeholder':"Пароль"}),
                    }
        #labels ={'name': 'Имя пользователя', 'email':'USER EMAIL ','password':'USER Password'}

        #def save (self,*args,**kvargs):
        #    kvargs['commit']=False
        #    user=super(UserForm, self).save(*args,**kvargs)
        #    user.is_active=True
        #    user.set_password(user.password)
        #    user.save()
        # функция позволяет заранее активировать пользователя и записать хеш пароля

class CommentForm (ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] #'author','snippet'
        widgets = {
        'text': Textarea(attrs={'cols': "96", 'rows': "3", 'placeholder': "Текст комментария"}),
        }


class AccountForm (ModelForm):
    class Meta:
        model = Account
        fields = ['amount','comment']
        widgets = {
        'amount' : NumberInput(attrs={"class": "form-control form-control-lg",
                                         "placeholder": "введите сумму прихода+ или расхода- по счету"}),
        'comment': TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Короткий комментарий"}),
        }


class TarifForm (ModelForm):
    class Meta:
        model = Tarif
        fields = ['tarif', 'comment']
        widgets = {
        'tarif' : NumberInput(attrs={"class": "form-control form-control-lg",
                                      "placeholder":"Новый тариф за 1 кВт.час"}),
        'comment': TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Короткий комментарий"})
        }

class ElektroForm (ModelForm):
    class Meta:
        model = Elektro
        fields = ['el_acc','comment']
        widgets = {
        'el_acc' : NumberInput(attrs={"class": "form-control form-control-lg",
                                         "placeholder": "введите текущее показание счетчика"}),
        'comment': TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Короткий комментарий"}),
        }