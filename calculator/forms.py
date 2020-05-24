from django import forms
from .models import Subject
import pandas
class SubjectSelectForm(forms.ModelForm):
    class Meta:
        model = Subject
        field = ['subject_year','subject_category','subject_title']
    def conver_csv(category,semester)
        csv_data = pandas.read_csv("./major/ict_15_1.csv",header=None,encoding='CP949')
        for num in range(1,len(csv_data)):
            print(csv_data[0][num])

    widget = {
        'subject_year': forms.ChoiceField(
            attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.
        ),
    }
