from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from django.contrib.auth.models import Group


@receiver(post_save,sender = User)
def create_user_profile(sender,created,instance,**kwargs):
    usr_group = Group.objects.get(name = "User")
    auth_group = Group.objects.get(name = "Author")
    
    if created:
        instance.groups.add(usr_group)

    if instance.is_author:
        instance.groups.add(auth_group,usr_group)
    else:
        instance.groups.remove(auth_group)


        
        

