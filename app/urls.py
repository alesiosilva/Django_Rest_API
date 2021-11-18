# Routers para criar e disponibilizar automaticamente viewsets
from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls

# Padrão de urls para acessar views
'''
from django.urls import path
from app import views

urlpatterns = [
    # Views antigas para gerir objects via GET/POST na API
    # path('', views.todo_list),
    # path('<int:pk>', views.todo_detail_change_and_delete),

    # APIViews para gerir objects na API
    path('', views.TodoListAndCreate.as_view()),
    path('<int:pk>', views.TodoDetailChangeAndDelete.as_view()),
]
'''