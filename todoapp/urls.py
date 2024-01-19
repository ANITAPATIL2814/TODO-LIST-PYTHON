from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,customLoginView,RegisterPage
from todoapp import views
urlpatterns=[
    path('login/', customLoginView.as_view(),name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',TaskList.as_view(),name='task'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)