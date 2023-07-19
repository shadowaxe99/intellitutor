```python
import json
from src.ai_tools import AI_Tools

class TutorUpdates:
    def __init__(self):
        self.ai_tools = AI_Tools()
        self.tutor_data = {}
        self.student_data = {}

    def load_data(self):
        with open('tutor_data.json', 'r') as file:
            self.tutor_data = json.load(file)
        with open('student_data.json', 'r') as file:
            self.student_data = json.load(file)

    def update_tutor(self, tutor_id):
        tutor = self.tutor_data[tutor_id]
        students = [student for student in self.student_data.values() if student['tutor_id'] == tutor_id]
        for student in students:
            progress = self.ai_tools.track_progress(student['id'])
            tutor['students'][student['id']]['progress'] = progress
        with open('tutor_data.json', 'w') as file:
            json.dump(self.tutor_data, file)

    def run_updates(self):
        self.load_data()
        for tutor_id in self.tutor_data.keys():
            self.update_tutor(tutor_id)

if __name__ == "__main__":
    tutor_updates = TutorUpdates()
    tutor_updates.run_updates()
```