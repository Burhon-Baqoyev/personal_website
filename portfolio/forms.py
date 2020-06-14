from django.forms import ModelForm,TextInput,NumberInput,Textarea
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'phone':NumberInput(attrs={'class':'form-control'}),
            'message':Textarea(attrs={'class':'form-control'})
        }
    # name = forms.CharField(label='Your Name (required)', max_length=100,required=True,widget=forms.)
    # phone = forms.IntegerField(label='Your Phone (required)',required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    # message = forms.CharField(label='Your Message',required=True,widget=forms.Textarea(attrs={'class':'form-control'}))

    # class Meta:
    #     model = Message
    #     fields = ['name', 'phone', 'message']
