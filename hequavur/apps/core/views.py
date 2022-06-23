from rest_framework import generics, status
from rest_framework.response import Response

from .permissions import IsAdmin
from .models import Department, Candidate
from .serializers import DepartmentSerializer, CandidateGETSerializer, CandidatePOSTSerializer, FileSerializer


class CandidateList(generics.ListAPIView):
    serializer_class = CandidateGETSerializer
    permission_classes = (IsAdmin,)

    def get_queryset(self):
        queryset = Candidate.objects.all().order_by('-create_date')
        return queryset


class CandidateCreate(generics.CreateAPIView):
    serializer_class = CandidatePOSTSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class FileDetail(generics.GenericAPIView):
    queryset = Candidate.objects.all()
    permission_classes = (IsAdmin,)
    serializer_class = FileSerializer

    def get(self, request, pk):
        candidate = self.get_object()
        if not candidate:
            return Response({'errors': 'that candidate was not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serialized_data = self.serializer_class(candidate)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        self.check_permissions(request)
        candidate = self.get_object()
        if candidate:
            serializer_data = self.serializer_class(
                candidate, request.data, partial=True)
            serializer_data.is_valid(raise_exception=True)
            serializer_data.save()
            return Response(
                {'data': serializer_data.data,
                    'message': 'File updated successfully'},
                status=status.HTTP_200_OK)
        return Response({
            'errors': 'that candidate was not found'
        }, status=status.HTTP_404_NOT_FOUND)
