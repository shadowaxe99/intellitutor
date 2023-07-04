```python
from src.ai_tools import AI_Tool
from src.student_data import StudentSchema

class CollegeCounseling:
    def __init__(self):
        self.ai_tool = AI_Tool()
        self.student_data = StudentSchema()

    def counsel_college(self, student_id):
        student = self.student_data.get_student(student_id)
        if not student:
            return "Student not found"

        college_advice = self.ai_tool.generate_college_advice(student)
        return college_advice

college_counseling = CollegeCounseling()

def counsel_college(student_id):
    return college_counseling.counsel_college(student_id)
```