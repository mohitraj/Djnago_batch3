from django import forms
class StudentRegistration(forms.Form):
	stuid=forms.CharField(label= "Roll Number", help_text="Fill it now", error_messages={'required': "fill the name here"})		# Here length is not required
	stuname=forms.CharField(label="Name: ")
	stupass =forms.CharField(label="Password : ")
	stmail = forms.EmailField(label= "Email ")

