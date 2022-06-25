from django.urls import path
from .views import CandidateList, CandidateCreate, DepartmentList,\
    DepartmentDetail, FileDetail

urlpatterns = [
    path('department/', DepartmentList.as_view(), name='department'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    path('candidate/', CandidateList.as_view(), name='candidate'),
    path('candidate/create', CandidateCreate.as_view(), name='candidate-create'),
    path('file/<int:pk>/', FileDetail.as_view(), name='file-detail'),
]
