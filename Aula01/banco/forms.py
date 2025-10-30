from django import forms
from .models import Area, Instrutor, Publico, Cursos

class AreaForms(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class InstrutorForms(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome']

class PublicoForms(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']


class CursosForms(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = 'titulo', 'descricao','vagas','instrutor','area','publicos',

        widgets = {
            'area': forms.RadioSelect(),
            'publicos': forms.SelectMultiple(),
            'Instrutor': forms.RadioSelect()
        }