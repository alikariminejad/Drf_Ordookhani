from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodosViewSetAPIView)

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.TodosListApiView.as_view()),
    path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinAPIView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinAPIView.as_view()),
    path('generics/', views.TodosGenericAPIView.as_view()),
    path('generics/<pk>', views.TodosGenericDetailView.as_view()),
    path('viewsets/', include(router.urls)),
]