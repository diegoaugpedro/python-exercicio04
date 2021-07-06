from django import forms


class FormularioPessoa(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobrenome = forms.CharField(label='Sobrenome', max_length=100)
    idade = forms.IntegerField(label='Idade')

    ESCOLARIDADE_CHOICES = [
        ("NI", "Não informado"),
        ("EF", "Ensino Fundamental"),
        ("EM", "Ensino Médio"),
        ("ES", "Ensino Superior"),
    ]

    escolaridade = forms.ChoiceField(label='Escoloridade', choices = ESCOLARIDADE_CHOICES)
    depto = forms.CharField(label='Departamento')


class FormularioEditarDepartamento(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    novo_departamento = forms.CharField(
    label='Novo departamento', max_length=100)


class FormularioDeletarPessoa(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
