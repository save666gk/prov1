from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(user_signed_up)
def add_to_custom_group_allauth(sender, request, user, **kwargs):
    common_group = Group.objects.get(name='common')
    user.groups.add(common_group)
