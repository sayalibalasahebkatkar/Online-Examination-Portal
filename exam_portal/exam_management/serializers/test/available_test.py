from rest_framework import serializers
from django.utils import timezone
from exam_management.models import Test,Student,StudentTest
from exam_management.serializers import StudentSerializer
from rest_framework.exceptions import NotFound

class AvailableTestSerializer(serializers.ModelSerializer):
    is_eligible = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    student = StudentSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(source='student', read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'name', 'start_time', 'end_time', 'is_open', 'is_eligible', 'status', 'student_id','student']

    def get_student(self):
        student_id = self.context.get('student_id')
        print('student id : ',student_id)
        if not student_id:
            return None
        try:
            return Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return None
        
    def get_is_eligible(self, obj):
        if obj.is_open:
            return True
        student = self.get_student()
        if not student:
            return False
        
        studenttest = StudentTest.objects.filter(student=student.id, test=obj.id).exists()
        if studenttest:
            return True        
        return False
    
    def get_status(self, obj):
        now = timezone.now()
        if now < obj.start_time:
            return "Upcoming"
        elif obj.is_active:
            return "Ongoing"
        else:
            return "Completed"
        