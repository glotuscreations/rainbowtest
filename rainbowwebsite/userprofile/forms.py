from userprofile.models import UserProfiles
from django import forms


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfiles
        fields = ('gender', 'age', 'Nationality','image', 'height', 'weight', 'description', 'lookingfor', 'preference',
        'Country', 'City', 'hobbies', 'profession')

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

class ContactForm(forms.Form):
    Username = forms.CharField(required=True)
    Reason = forms.CharField(required=True, max_length=200)
    Explanation = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
