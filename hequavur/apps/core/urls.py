from django.urls import path
from .views import CandidateList, CandidateCreate, DepartmentList,\
    DepartmentDetail, FileDetail

urlpatterns = [
    path('department/', DepartmentList.as_view()),
    path('department/<int:pk>/', DepartmentDetail.as_view()),
    path('candidate/', CandidateList.as_view()),
    path('candidate/create', CandidateCreate.as_view()),
    path('file/<int:pk>/', FileDetail.as_view()),
]
