from django.contrib.auth.base_user import BaseUserManager

class AuthorManager(BaseUserManager):
    def create_user(self, username, password=None, displayName=None, github=None, **other_fields):
        #print("create user called")
        if not username:
            raise ValueError('username is needed')
        if not password:
            raise ValueError('password is needed')
        user = self.model(username=username, displayName=displayName, github=github, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password=None, **other_fields):
        other_fields.setdefault('is_active', 'True')
        other_fields.setdefault('is_staff', 'True')
        other_fields.setdefault('is_superuser', 'True')

        return self.create_user(username, password, **other_fields)