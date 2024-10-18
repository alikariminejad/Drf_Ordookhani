from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.TodosListApiView.as_view()),
    path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinAPIView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinAPIView.as_view()),
    path('generics/', views.TodosGenericAPIView.as_view()),
    path('generics/<pk>', views.TodosGenericDetailView.as_view()),
]