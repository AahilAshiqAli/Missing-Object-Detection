from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(Q(email=email) | Q(username=email))
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            user_model().set_password(password)