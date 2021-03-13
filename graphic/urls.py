from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# urlpatterns = [
#     path('', views.graphic_list),
#     path('/<int:pk>/', views.graphic_detail)
# ]

urlpatterns = [
    path('', views.GraphicList.as_view()),
    path('<int:pk>', views.GraphicDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)