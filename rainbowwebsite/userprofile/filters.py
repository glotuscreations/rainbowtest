import django_filters
from userprofile.models import UserProfiles

class UserProfilesFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfiles
        fields = ['gender', 'age', 'Nationality','preference', 'Country', 'City']
