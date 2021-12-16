import json
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from django.contrib.auth.models import User

@require_POST
def register_view(request):
	email = json.loads(request.POST['email'])
	return email
	# user = User.objects.create_user(email, password)
 #    user.first_name = first_name
 #    user.last_name = last_name
 #    user.save()

 #    return JsonResponse({'created': user })

