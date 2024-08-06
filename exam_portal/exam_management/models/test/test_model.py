from django.db import models
from exam_management.models import User
from exam_management.models import Branch,Stream
from django.utils import timezone


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)
    has_sql = models.BooleanField(default=False)
    db_name = models.CharField(max_length=100, blank=True, null=True)
    sql_script = models.TextField(blank=True, null=True)
    stream = models.ManyToManyField(Stream,related_name='tests')
    branches = models.ManyToManyField(Branch, related_name='tests')

    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time