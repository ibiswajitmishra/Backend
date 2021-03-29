from questions.api.views import QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', QuestionViewSet, basename='question')
urlpatterns = router.urls



# urlpatterns = [
#     path('',QuestionListView.as_view()),
#     path('create/',QuestionCreateView.as_view()),
#     path('<pk>/delete/',QuestionDeleteView.as_view()),
#     path('<pk>/update/',QuestionUpdateView.as_view()),
#     path('<pk>',QuestionDetailView.as_view())
# ]                                                               

# from django.urls import path
# from .views import (
#     QuestionListView,
#     QuestionDetailView,
#     QuestionCreateView,
#     QuestionDeleteView,
#     QuestionUpdateView
#     )
