from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exam_management import views

router = DefaultRouter()
router.register(r'admins', views.AdminViewSet)
router.register(r'streams', views.StreamViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'colleges', views.CollegeViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'options', views.OptionViewSet)
router.register(r'fill-in-the-blank-answers', views.FillInTheBlankAnswerViewSet)
router.register(r'student-tests', views.StudentTestViewSet)
router.register(r'student-answers', views.StudentAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
