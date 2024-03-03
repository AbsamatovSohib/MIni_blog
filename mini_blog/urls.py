from django.urls import path
from .views import FeaturedThisView

urlpatterns = [
    path("featured/", FeaturedThisView.as_view()),

]
