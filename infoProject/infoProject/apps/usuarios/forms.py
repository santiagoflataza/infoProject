from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from apps.perfil.models import Profile
from apps.rubros.models import Rubro

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email']
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
            }
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''
'''
def rubros():
    GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
)

    lista_temporal = list()
    todos = Rubro.objects.all()
    for i in todos:
        lista_temporal.append((i,i.nombre))
        print (str(i.id),str(i.nombre))
    tupla_temporal = tuple(lista_temporal)
    print(tupla_temporal)

    return GEEKS_CHOICES
'''
class ProfileUpdateForm(forms.ModelForm):
    rubro = forms.ChoiceField(choices=Rubro.objects.all())
    class Meta:
        model = Profile
        fields = ['image','aboutus','instagram','twitter','telefono','rubro']
        widgets = {
                'image':forms.FileInput(attrs={'class':'btn btn-primary mb-4'}),
                'instagram': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'aboutus': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'twitter': forms.TextInput(attrs={'class': 'form-control mb-4'}),
                'telefono': forms.TextInput(attrs={'class': 'form-control mb-4'}),

            }
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['image','aboutus','instagram','twitter','telefono','rubro']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''
