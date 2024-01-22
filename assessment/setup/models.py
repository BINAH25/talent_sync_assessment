from django.db import models


class SetupPerm(models.Model):

    class Meta:
        managed = False
        default_permissions = ()
        permissions = [

            ('create_post', 'Can Create Post'),
            ('view_post',   'Can View Post'),
            ('update_post', 'Can Update Post'),
            ('delete_post', 'Can Delete Post'), 
            
        ]
