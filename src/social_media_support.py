```python
import requests
from ai_tools import provide_support

def provide_social_media_support(student_data, tutor_data):
    # Define the social media platforms we will be providing support on
    social_media_platforms = ['Facebook', 'Twitter', 'Instagram']

    for platform in social_media_platforms:
        # Simulate sending a support message to the student on each platform
        message = provide_support(student_data, tutor_data)
        send_social_media_message(platform, message)

def send_social_media_message(platform, message):
    # This function simulates sending a message on a social media platform
    # In a real-world application, this would involve using the API of the respective platform

    print(f'Sending message on {platform}: {message}')

    # Simulate a successful message send with a status code of 200
    response = requests.Response()
    response.status_code = 200

    if response.status_code == 200:
        print(f'Successfully sent message on {platform}.')
    else:
        print(f'Failed to send message on {platform}.')
```