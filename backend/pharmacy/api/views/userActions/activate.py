from base64 import urlsafe_b64decode
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.encoding import force_str

from pharmacy.api.views.userActions.token.token_generator import TokenGenerator
from rest_framework.views import APIView


class Activate(APIView):
    def get(self, request, uidb64, token):
        if uidb64 and token == None:
            return HttpResponse("Invalid URL")
        print("serving a request")
        tokenCheck = TokenGenerator()
        user = User.objects
        try:
            uid = force_str(urlsafe_b64decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None
        if user is not None and tokenCheck.check_token(user, token):
            if user.is_active is not True:
                user.is_active = True
                user.save()
                return HttpResponse("User has been activated")
        else:
            return HttpResponse("Activation link is invalid!")
