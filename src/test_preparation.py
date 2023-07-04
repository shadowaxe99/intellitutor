```python
import random
from src.ai_tools import AI_Tools

class TestPreparation:
    def __init__(self, student_data):
        self.student_data = student_data
        self.ai_tools = AI_Tools()

    def prepare_test(self, student_id):
        student = self.get_student(student_id)
        if not student:
            return "Student not found."

        test_preparation_material = self.ai_tools.generate_test_material(student)
        return test_preparation_material

    def get_student(self, student_id):
        for student in self.student_data:
            if student['id'] == student_id:
                return student
        return None

if __name__ == "__main__":
    student_data = [
        {"id": 1, "name": "John Doe", "grade": "9th grade", "subject": "Math"},
        {"id": 2, "name": "Jane Doe", "grade": "10th grade", "subject": "Science"},
    ]

    test_prep = TestPreparation(student_data)
    print(test_prep.prepare_test(1))
```