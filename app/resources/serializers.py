from app.models.student import StudentModel
from app.ma import ma

class StudentSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'course')

student_schema = StudentSchema()
student_schema = StudentSchema(many=True)