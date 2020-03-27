from django import forms
from django.core.exceptions import ObjectDoesNotExist
from register.models import User

class LoanForm(forms.Form):
    # 貸出用フォーム
    userID = forms.IntegerField(label='ユーザーID', initial=1)
    loan_day = forms.IntegerField(label='貸出日数')

    def clean_loan_day(self):
        loan_day = self.cleaned_data['loan_day']
        if loan_day < 1 :
            raise forms.ValidationError(
        '貸出日数は１日以上です'
        )
        return loan_day

    def clean(self):
        userID = self.cleaned_data.get('userID')
        try:
            userID = User.objects.get(id=userID)
            print('heraaaaaaaaaa')
        except ObjectDoesNotExist:
            print('validation error')
            raise forms.ValidationError('そのユーザーIDは存在しません')