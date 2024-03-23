from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from AppFinance.models import Avatar

class form_ingreso (forms.Form): #este formulario no esta siendo utilizado, ya que el crud completo del 
   #models Ingreso se esta utilizando vistas basadas en clases.

   fecha= forms.DateField()
   importe= forms.IntegerField()
   categoria = forms.CharField(max_length=60)
   descripcion= forms.CharField(max_length=60)

class form_egreso (forms.Form): #este formulario no esta siendo utilizado, ya que el crud completo del 
   #models Ingreso se esta utilizando vistas basadas en clases.

   fecha= forms.DateField()
   importe= forms.IntegerField()
   categoria = forms.CharField(max_length=60)
   descripcion= forms.CharField(max_length=60)

class Registro_Usuario(UserCreationForm):

   email = forms.EmailField()
   password1 = forms.CharField(label = 'contraseña', widget = forms.PasswordInput)
   password2 = forms.CharField(label = 'repetir contraseña', widget = forms.PasswordInput)

   class Meta:
      model = User
      fields = ['username','email','first_name','last_name','password1','password2']

class Editar_Usuario(UserCreationForm):

   email = forms.EmailField()
   password1 = forms.CharField(label = 'contraseña', widget = forms.PasswordInput)
   password2 = forms.CharField(label = 'repetir contraseña', widget = forms.PasswordInput)

   class Meta:
      model = User
      fields = ['email','first_name','last_name','password1','password2']

class form_Avatar(forms.Form):
      imagen = forms.ImageField()
