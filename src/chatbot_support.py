```python
from ai_tools import AIChatbot

class ChatbotSupport:
    def __init__(self):
        self.chatbot = AIChatbot()

    def provide_support(self, user_query):
        response = self.chatbot.get_response(user_query)
        return response

    def handle_common_questions(self, user_query):
        common_questions = {
            "How does the tutor matching work?": "Our AI-powered tools match students with tutors based on their specific needs.",
            "How is progress tracked?": "We provide automated progress tracking, enabling both students and tutors to monitor student progress and identify areas for improvement.",
            "How does the payment process work?": "We use AI-powered tools to automate the payment process, ensuring that payments are processed quickly and securely."
        }

        if user_query in common_questions:
            return common_questions[user_query]
        else:
            return self.provide_support(user_query)
```