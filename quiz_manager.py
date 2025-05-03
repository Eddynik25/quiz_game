import json

class QuizManager:
    def __init__(self, json_path, difficulty):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.questions = data.get(difficulty, [])
        
        self.current_index = 0

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def next_question(self):
        self.current_index += 1
        return self.get_current_question()

    def has_more_questions(self):
        return self.current_index < len(self.questions)

    def check_answer(self, user_answer):
        current_question = self.get_current_question()
        if current_question:
            return user_answer.strip().lower() == current_question["answer"].strip().lower()
        return False