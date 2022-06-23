import datetime

from rest_framework import serializers
from .models import Department, Candidate


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CandidateGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('full_name', 'date_of_birth', 'years_of_experience', 'department')


class CandidatePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

    def validate(self, data):
        if data['date_of_birth'] > datetime.date.today():
            raise serializers.ValidationError(
                {'date_of_birth': 'Invalid date,date must be prior/today (happy birthday)'})
        return data


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('resume',)
