from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib.auth.models import User
from benutzeraccounts.models import Profile
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'first_name',
            }
        )
    )

    last_name = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'last_name',
            }
        )
    )

    email = forms.EmailField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'hidden',
                'name': 'email',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )

ACTIVITY_CHOICES= [
    ('', ''),
    ('Andere', 'Andere'),
    ('Asset Management', 'Asset Management'),
    ('Business Banking', 'Business Banking'),
    ('Corporate Banking', 'Corporate Banking'),
    ('General Management', 'General Management'),
    ('Investement Banking', 'Investement Banking'),
    ('Management Services', 'Management Services'),
    ('Private Banking', 'Private Banking'),
    ('Recht/Compliance', 'Recht/Compliance'),
    ('Retail (Private und KMU)', 'Retail (Private und KMU)'),
    ('Technologie', 'Technologie'),
    ('Wealth Management', 'Wealth Management'),
    ('Ehemalige Bankiers', 'Ehemalige Bankiers'),
]

RANK_CHOICES= [
    ('', ''),
    ('Area Director', 'Area Director'),
    ('Associate Director', 'Associate Director'),
    ('CEO', 'CEO'),
    ('CEO Asset Management', 'CEO Asset Management'),
    ('CEO and President of the Manangement', 'CEO and President of the Manangement'),
    ('CEO and Chariman of the Manangement', 'CEO and Chariman of the Manangement'),
    ('CFO', 'CFO'),
    ('CFO and Member of the Executive Board', 'CFO and Member of the Executive Board'),
    ('CIO', 'CIO'),
    ('COO', 'COO'),
    ('COO and Member of the Executive Board', 'COO and Member of the Executive Board'),
    ('Chairman', 'Chairman'),
    ('Chairman of the Board', 'Chairman of the Board'),
    ('Chairman of the Board of Directors', 'Chairman of the Board of Directors'),
    ('Compliance Officer', 'Compliance Officer'),
    ('Consultant', 'Consultant'),
    ('Deputy CEO', 'Deputy CEO'),
    ('Deputy CFO', 'Deputy CFO'),
    ('Deputy General Manager', 'Deputy General Manager'),
    ('Director', 'Director'),
    ('Director and Member of the extended Management', 'Director and Member of the extended Management'),
    ('Director, Member of the Management', 'Director, Member of the Management'),
    ('Director, Chairman of the Management', 'Director, Chairman of the Management'),
    ('Ehem. Bankier', 'Ehem. Bankier'),
    ('General Manager', 'General Manager'),
    ('Group Managing Director', 'Group Managing Director'),
    ('Head Group Legal & Tax', 'Head Group Legal & Tax'),
    ('Head Human Resources', 'Head Human Resources'),
    ('Head of Asia Pasific', 'Head of Asia Pasific'),
    ('Head of Europe', 'Head of Europe'),
    ('Head of Latin America', 'Head of Latin America'),
    ('Head of Middle East', 'Head of Middle East'),
    ('Head of Compliance', 'Head of Compliance'),
    ('Head of Legal and Compliance', 'Head of Legal and Compliance'),
    ('Head of Marketing', 'Head of Marketing'),
    ('Head of Operations', 'Head of Operations'),
    ('Head of Sales', 'Head of Sales'),
    ('Honorary Chairman', 'Honorary Chairman'),
    ('Insitutional Sales Manager', 'Insitutional Sales Manager'),
    ('Legal Counsel', 'Legal Counsel'),
    ('Managing Director', 'Managing Director'),
    ('Managing Director Senior Advisor', 'Managing Director Senior Advisor'),
    ('Memeber of Divisional Executive Board', 'Memeber of Divisional Executive Board'),
    ('Member of General Management', 'Member of General Management'),
    ('Member of the Board', 'Member of the Board'),
    ('Member of the Board of Directors', 'Member of the Board of Directors'),
    ('Member of the Executive Board', 'Member of the Executive Board'),
    ('Member of the Executive Comitee', 'Member of the Executive Comitee'),
    ('Member of the Group Executive Board', 'Member of the Group Executive Board'),
    ('Member of the Group Managing Board', 'Member of the Group Managing Board'),
    ('Member of the Management Comitee', 'Member of the Management Comitee'),
    ('Member of the Operations Comitee', 'Member of the Operations Comitee'),
    ('Partner', 'Partner'),
    ('President', 'President'),
    ('Regulatory Counsel', 'Regulatory Counsel'),
    ('Relationship Manager', 'Relationship Manager'),
    ('Senior Advisor', 'Senior Advisor'),
    ('Senior Consultant', 'Senior Consultant'),
    ('Senior Manager', 'Senior Manager'),
    ('Senior Partner', 'Senior Partner'),
    ('Senior Vice President', 'Senior Vice President'),
    ('Vice CEO', 'Vice CEO'),
    ('Vice Deputy Manager', 'Vice Deputy Manager'),
    ('Vice President', 'Vice President'),
    ('Vice-Chairman', 'Vice-Chairman'),
    ('Vice-Chairman of the Board', 'Vice-Chairman of the Board'),
]

class ProfileForm(forms.ModelForm):
    salutation = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'salutation',
                'autofocus': 'autofocus'
            }
        )
    )

    title = forms.CharField(max_length=30, required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'title',
                'placeholder': 'Prof. Dr.'
            }
        )
    )

    phone = PhoneNumberField(required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'name': 'phone',
                'placeholder': '+41581234578',
            }
        )
    )

    fax = PhoneNumberField(required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'name': 'fax',
                'placeholder': '+41581234579'
            }
        )
    )

    mobile = PhoneNumberField(required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'name': 'mobile',
                'placeholder': '+41761234578'
            }
        )
    )


    birthday = forms.CharField(required=False,
    widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'name': 'birthday',
            }
        )
    )

    departement = forms.CharField(max_length=30, required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'departement',
                'placeholder': 'IT'
            }
        )
    )

    rank = forms.CharField(max_length=30, required=False,
    widget=forms.Select(choices=RANK_CHOICES,
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'rank',

            }
        )
    )

    activity = forms.CharField(max_length=30, required=False,
    widget=forms.Select(choices=ACTIVITY_CHOICES,
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'activity',
            }
        )
    )

    institute = forms.CharField(max_length=50, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'institute',

            }
        )
    )

    class Meta:
        model = Profile
        fields = (
            'salutation',
            'title',
            'phone',
            'fax',
            'mobile',
            'birthday',
            'departement',
            'rank',
            'activity',
            'institute'
        )

    def clean_phone(self):       #Funktion zur Ueberwachung, ob Telefon und Fax unterschiedlich sind.
        phone = self.cleaned_data.get("phone")
        fax = self.cleaned_data.get("fax")
        if phone and fax and phone == fax:
            raise forms.ValidationError("") #Die Error-Message wird in den HTML-Dateien definiert
        return phone


class PasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )


    def clean_old_password(self):       #Funktion zur Ueberwachung, ob das alte Passwort korrekt eingegeben wurde.
        old_password = self.cleaned_data.get('old_password')
        cont = User.objects.filter(old_password=old_password)
        if cont.exists():
            raise forms.ValidationError("")  #Die Error-Message wird in den HTML-Dateien definiert
        return old_password

    def clean_password(self):       #Funktion zur Ueberwachung, ob Passwoerter uebereinstimmen.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("")  #Die Error-Message wird in den HTML-Dateien definiert
        return password2

ACTIVITY_CHOICES= [
    ('', ''),
    ('Andere', 'Andere'),
    ('Asset Management', 'Asset Management'),
    ('Business Banking', 'Business Banking'),
    ('Corporate Banking', 'Corporate Banking'),
    ('General Management', 'General Management'),
    ('Investement Banking', 'Investement Banking'),
    ('Management Services', 'Management Services'),
    ('Private Banking', 'Private Banking'),
    ('Recht/Compliance', 'Recht/Compliance'),
    ('Retail (Private und KMU)', 'Retail (Private und KMU)'),
    ('Technologie', 'Technologie'),
    ('Wealth Management', 'Wealth Management'),
    ('Ehemalige Bankiers', 'Ehemalige Bankiers'),
]

RANK_CHOICES= [
    ('', ''),
    ('Area Director', 'Area Director'),
    ('Associate Director', 'Associate Director'),
    ('CEO', 'CEO'),
    ('CEO Asset Management', 'CEO Asset Management'),
    ('CEO and President of the Manangement', 'CEO and President of the Manangement'),
    ('CEO and Chariman of the Manangement', 'CEO and Chariman of the Manangement'),
    ('CFO', 'CFO'),
    ('CFO and Member of the Executive Board', 'CFO and Member of the Executive Board'),
    ('CIO', 'CIO'),
    ('COO', 'COO'),
    ('COO and Member of the Executive Board', 'COO and Member of the Executive Board'),
    ('Chairman', 'Chairman'),
    ('Chairman of the Board', 'Chairman of the Board'),
    ('Chairman of the Board of Directors', 'Chairman of the Board of Directors'),
    ('Compliance Officer', 'Compliance Officer'),
    ('Consultant', 'Consultant'),
    ('Deputy CEO', 'Deputy CEO'),
    ('Deputy CFO', 'Deputy CFO'),
    ('Deputy General Manager', 'Deputy General Manager'),
    ('Director', 'Director'),
    ('Director and Member of the extended Management', 'Director and Member of the extended Management'),
    ('Director, Member of the Management', 'Director, Member of the Management'),
    ('Director, Chairman of the Management', 'Director, Chairman of the Management'),
    ('Ehem. Bankier', 'Ehem. Bankier'),
    ('General Manager', 'General Manager'),
    ('Group Managing Director', 'Group Managing Director'),
    ('Head Group Legal & Tax', 'Head Group Legal & Tax'),
    ('Head Human Resources', 'Head Human Resources'),
    ('Head of Asia Pasific', 'Head of Asia Pasific'),
    ('Head of Europe', 'Head of Europe'),
    ('Head of Latin America', 'Head of Latin America'),
    ('Head of Middle East', 'Head of Middle East'),
    ('Head of Compliance', 'Head of Compliance'),
    ('Head of Legal and Compliance', 'Head of Legal and Compliance'),
    ('Head of Marketing', 'Head of Marketing'),
    ('Head of Operations', 'Head of Operations'),
    ('Head of Sales', 'Head of Sales'),
    ('Honorary Chairman', 'Honorary Chairman'),
    ('Insitutional Sales Manager', 'Insitutional Sales Manager'),
    ('Legal Counsel', 'Legal Counsel'),
    ('Managing Director', 'Managing Director'),
    ('Managing Director Senior Advisor', 'Managing Director Senior Advisor'),
    ('Memeber of Divisional Executive Board', 'Memeber of Divisional Executive Board'),
    ('Member of General Management', 'Member of General Management'),
    ('Member of the Board', 'Member of the Board'),
    ('Member of the Board of Directors', 'Member of the Board of Directors'),
    ('Member of the Executive Board', 'Member of the Executive Board'),
    ('Member of the Executive Comitee', 'Member of the Executive Comitee'),
    ('Member of the Group Executive Board', 'Member of the Group Executive Board'),
    ('Member of the Group Managing Board', 'Member of the Group Managing Board'),
    ('Member of the Management Comitee', 'Member of the Management Comitee'),
    ('Member of the Operations Comitee', 'Member of the Operations Comitee'),
    ('Partner', 'Partner'),
    ('President', 'President'),
    ('Regulatory Counsel', 'Regulatory Counsel'),
    ('Relationship Manager', 'Relationship Manager'),
    ('Senior Advisor', 'Senior Advisor'),
    ('Senior Consultant', 'Senior Consultant'),
    ('Senior Manager', 'Senior Manager'),
    ('Senior Partner', 'Senior Partner'),
    ('Senior Vice President', 'Senior Vice President'),
    ('Vice CEO', 'Vice CEO'),
    ('Vice Deputy Manager', 'Vice Deputy Manager'),
    ('Vice President', 'Vice President'),
    ('Vice-Chairman', 'Vice-Chairman'),
    ('Vice-Chairman of the Board', 'Vice-Chairman of the Board'),
]

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'username',
            }
        )
    )

    first_name = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'first_name',
            }
        )
    )

    last_name = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'last_name',
            }
        )
    )

    email = forms.EmailField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'name': 'email',
            }
        )
    )

    password1 = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password1',
            }
        )
    )

    password2 = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password2',
            }
        )
    )

    salutation = forms.CharField(max_length=30, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'salutation',
                'autofocus': 'autofocus'
            }
        )
    )

    title = forms.CharField(max_length=30, required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'title',
                'placeholder': 'Prof. Dr.'
            }
        )
    )

    phone = PhoneNumberField(required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'name': 'phone',
                'placeholder': '+41581234578',
            }
        )
    )

    fax = PhoneNumberField(required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'name': 'fax',
                'placeholder': '+41581234579'
            }
        )
    )

    mobile = PhoneNumberField(required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'name': 'mobile',
                'placeholder': '+41761234578'
            }
        )
    )


    birthday = forms.CharField(required=False,
    widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'name': 'birthday',
            }
        )
    )

    departement = forms.CharField(max_length=30, required=False,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'departement',
                'placeholder': 'IT'
            }
        )
    )

    rank = forms.CharField(max_length=30, required=False,
    widget=forms.Select(choices=RANK_CHOICES,
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'rank',

            }
        )
    )

    activity = forms.CharField(max_length=30, required=False,
    widget=forms.Select(choices=ACTIVITY_CHOICES,
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'activity',
            }
        )
    )

    institute = forms.CharField(max_length=50, required=True,
    widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'institute',

            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'salutation',
            'title',
            'phone',
            'fax',
            'mobile',
            'birthday',
            'departement',
            'institute'
        )



    def clean_password(self):       #Funktion zur Ueberwachung, ob Passwoerter uebereinstimmen.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("") #Die Error-Message wird in den HTML-Dateien definiert
        return password2

    def clean_email(self):          #Funktion zur Ueberwachung, ob E-Mail vergeben ist.
        email = self.cleaned_data.get('email')
        check = User.objects.filter(email=email)
        if check.exists():
            raise forms.ValidationError("") #Die Error-Message wird in den HTML-Dateien definiert
        return email
