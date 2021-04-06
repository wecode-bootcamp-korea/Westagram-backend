import bcrypt
import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.checks import email_validation

class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        PASSWORD_LENGTH = 8
        try:
            if len(data['password']) < PASSWORD_LENGTH:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)

            if not  email_validation(data['email']):
                return JsonResponse({"message": "INVALID_EMAIL"}, status=400)

            if User.objects.filter(email=data['email']).exists()\
                    or User.objects.filter(name=data['name']).exists()\
                    or User.objects.filter(phone_number=data['phone_number']).exists():
                return JsonResponse({"message": "EXISTS_USER"}, status=400)

            User.objects.create(
                    email        = data['email'],
                    password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                    phone_number = data['phone_number'],
                    name    = data['name']
                    )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class Signin(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            if data['account']:
                if User.objects.filter(email=data['account']).exists():
                    Signin_User_Password = User.objects.get(email=data['account']).password
                elif User.objects.filter(name=data['account']).exists():
                    Signin_User_Password = User.objects.get(name=data['account']).password
                elif User.objects.filter(phone_number=data['account']).exists():
                    Signin_User_Password = User.objects.get(phone_number=data['account']).password
                else:
                    return JsonResponse({"message": "INVALID_USER"}, status=401)
            else:
                return JsonResponse({"message": "NO_VALUE_ERROR"}, status=400)
            
            if not data['password']:
                return JsonResponse({"message": "NO_VALUE_ERROR"}, status=400)

            if bcrypt.checkpw(data['password'].encode('utf-8'), Signin_User_Password.encode('utf-8')):
                return JsonResponse({"message": "SUCCESS"}, status=200)
            else:
                return JsonResponse({"message": "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
