from django.urls import path
from .views import SkateList, SkateDetail

urlpatterns = [
    path("", SkateList.as_view(), name="skate_list"),
    path("<int:pk>/", SkateDetail.as_view(), name="skate_detail")
]
