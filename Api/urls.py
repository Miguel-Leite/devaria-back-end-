from django.urls import path

from Api.App.Views import WelcomeView

from Api.App.Views import ModuleView
from Api.App.Views import CourseView

from Api import views

""" DEFINIDO AS ROTAS DA APLICAÇÃO """

urlpatterns = [
	
	path('', WelcomeView.apiOverview, name="api-overview"),


	path('module/', ModuleView.ModuleList, name="module"),
	path('module_detail/<str:pk>/', ModuleView.ModuleDetail, name="module_detail"),
	path('module_create/', ModuleView.ModuleCreate, name="module_create"),
	path('module_update/<str:pk>/', ModuleView.ModuleUpdate, name="module_update"),
	path('module_delete/<str:pk>/', ModuleView.ModuleDelete, name="module_delete"),

	path('course/', CourseView.CourseList, name="course"),
	path('course_detail/<str:pk>/', CourseView.CourseDetail, name="course_detail"),
	path('course_create/', CourseView.CourseCreate, name="course_create"),
	path('course_update/<str:pk>/', CourseView.CourseUpdate, name="course_update"),
	path('course_delete/<str:pk>/', CourseView.CourseDelete, name="course_delete"),

	# path('auth/users/', UserView.UserList, name="user"),
	path('auth/user/create/', views.registration_view, name="create"),

	# path('teste/', views.HelloWorld.as_view()),

	# path('auth/user/create/', RegisterAPI.as_view(), name='register'),
	# path('auth/user/login/', LoginAPI.as_view(), name='login'),
	# path('auth/user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('auth/user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

