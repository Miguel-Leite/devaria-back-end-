from django.urls import path

from Api.App.Views import WelcomeView

from Api.App.Views import ModuleView
from Api.App.Views import CourseView

from Api import views

""" DEFINIDO AS ROTAS DA APLICAÇÃO """

urlpatterns = [
	
	path('', WelcomeView.apiOverview, name="api-overview"),
	path('getall/', CourseView.getCourseAndModule_view, name="get_module_course"),


	path('module/', ModuleView.ModuleList, name="module"),
	path('module_detail/<str:pk>/', ModuleView.ModuleDetail, name="module_detail"),
	path('module_create/', ModuleView.ModuleCreate, name="module_create"),
	path('module_update/<str:pk>/', ModuleView.ModuleUpdate, name="module_update"),
	path('module_delete/<str:pk>/', ModuleView.ModuleDelete, name="module_delete"),
	path('module_deleteall/<str:yes>/', ModuleView.deleteAll_view, name="module_delete_all"),

	path('course/', CourseView.CourseList, name="course"),
	path('course_detail/<str:pk>/', CourseView.CourseDetail, name="course_detail"),
	path('course_create/', CourseView.CourseCreate, name="course_create"),
	path('course_update/<str:pk>/', CourseView.CourseUpdate, name="course_update"),
	path('course_delete/<str:pk>/', CourseView.CourseDelete, name="course_delete"),
	path('course_deleteall/<str:yes>/', CourseView.deleteAll_view, name="course_delete_all"),
 
	path('auth/users/', views.getusers_view, name="users"),
	path('auth/user/details/<int:id>/', views.userDetail, name="user_details"),
	path('auth/user/create/', views.registration_view, name="user_create"),
	path('auth/user/update/<int:id>/', views.userUpdate, name="user_update"),
	path('auth/user/delete/<int:id>/', views.delete_view, name="user_delete"),
	path('auth/user/deleteall/<str:yes>/', views.deleteAll_view, name="user_delete_all"),

	
]

