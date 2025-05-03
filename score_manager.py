class ScoreManager:
    def __init__(self):
        self.score = 0

    def update_score(self, is_correct):
        if is_correct:
            self.score += 1

    def get_score(self):
        return self.score
        