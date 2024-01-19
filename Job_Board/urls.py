from django.urls import path
from .views import index,detail

urlpatterns = [
    path("", index,name="home"),
    path("job/<int:pk>/", detail,name="job-detail"),
]
