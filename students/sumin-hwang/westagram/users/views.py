import json
import re
import bcrypt
import jwt

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from users.models import User

PASSWORD_MINIMUM_LENGTH = 8

class SignUpView(View):
    def post(self, request):
        
        try:
            data = json.loads(request.body)
            mobile_number = data.get('mobile_number', None)
            email         = data.get('email', None)
            name          = data.get('name', None)
            nickname     = data.get('nickname', None)
            password      = data.get('password', None)
        
            mobile_number_form = re.compile('[0-9]{3}-[0-9]{3,4}-[0-9]{4}')
            email_form         = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

            if not (
                    mobile_number
                    and email
                    and name
                    and nickname
                    and password
                    ):
                return JsonResponse({'MESSAGE':'INVALID_KEY'}, status=400)
        
            if not mobile_number_form.match(str(mobile_number)):
                return JsonResponse({'MESSAGE':'INVALID_MOBILE_NUMBER'}, status=400)

            if not email_form.match(str(email)):
                return JsonResponse({'MESSAGE':'INVALID_EMAIL'}, status=400)

            if User.objects.filter(
                    Q(mobile_number = mobile_number) |
                    Q(email = email) |
                    Q(nickname = nickname)
                    ):
                return JsonResponse({'MESSAGE':'ALREADY_EXISTS'}, status=400)

            if len(data['password']) < PASSWORD_MINIMUM_LENGTH:
                return JsonResponse({'MESSAGE':'PASSWORD_VALIDATION_ERROR'}, status=400)

            password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            hashed_password = hashed_password.decode('utf-8')

            User.objects.create(
                    mobile_number = mobile_number,
                    email = email,
                    name = name,
                    nickname = nickname,
                    password = hashed_password,
                    )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        password      = data.get('password', None)
        mobile_number = data.get('mobile_number', None)
        email = data.get('email', None)
        nickname = data.get('nickname', None)

        user_queryset = User.objects.filter(password=password)

        if not ((mobile_number or email or nickname) and password):
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        
        if user_queryset.exists():
            if mobile_number:
                if not User.objects.filter(mobile_number = mobile_number) or not User.objects.filter(password=password):
                    return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
                else:
                    return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
            if email:
                if not User.objects.filter(email= email) or not User.objects.filter(password=password):
                    return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
                else:
                    return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
            if nickname:
                if not User.objects.filter(nickname = nickname) or not User.objects.filter(password = password):
                    return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)
                else:
                    return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
        else:
            return JsonResponse({'MESSAGE':'PASSWORD_ERROR'}, status=401)
