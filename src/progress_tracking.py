```python
import json
from datetime import datetime

# Importing shared schemas
from ai_tools import StudentSchema, TutorSchema

# Shared variables
student_data = {}
tutor_data = {}

# DOM Element IDs
progress_track = "progress_track"

# Message Names
ProgressUpdate = "ProgressUpdate"

# Function to track progress
def track_progress(student_id, tutor_id, progress_data):
    try:
        # Validate student_id and tutor_id
        if student_id not in student_data or tutor_id not in tutor_data:
            raise ValueError("Invalid student_id or tutor_id")

        # Update student's progress
        student_data[student_id]['progress'].append({
            'tutor_id': tutor_id,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'progress_data': progress_data
        })

        # Notify tutor about the progress
        update_tutor(tutor_id, student_id, progress_data)

        # Send progress update message
        send_message(ProgressUpdate, {
            'student_id': student_id,
            'tutor_id': tutor_id,
            'progress_data': progress_data
        })

        return True
    except Exception as e:
        print(f"Error in tracking progress: {str(e)}")
        return False

# Function to update tutor about student's progress
def update_tutor(tutor_id, student_id, progress_data):
    try:
        # Validate tutor_id
        if tutor_id not in tutor_data:
            raise ValueError("Invalid tutor_id")

        # Update tutor's data
        tutor_data[tutor_id]['student_progress'].append({
            'student_id': student_id,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'progress_data': progress_data
        })

        return True
    except Exception as e:
        print(f"Error in updating tutor: {str(e)}")
        return False

# Function to send message
def send_message(message_name, data):
    try:
        # Convert data to JSON
        json_data = json.dumps(data)

        # Send message
        print(f"{message_name}: {json_data}")

        return True
    except Exception as e:
        print(f"Error in sending message: {str(e)}")
        return False
```