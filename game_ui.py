import pygame

class GameUI:
    def __init__(self, quiz_manager, score_manager, screen):
        self.quiz_manager = quiz_manager
        self.score_manager = score_manager
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.current_question = self.quiz_manager.get_current_question()
        self.option_rects = []

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.update()
            self.draw()
            pygame.display.update()

    def handle_click(self, pos):
        for i, rect in enumerate(self.option_rects):
            if rect.collidepoint(pos):
                selected = self.current_question["options"][i]
                is_correct = self.quiz_manager.check_answer(selected)
                self.score_manager.update_score(is_correct)
                self.quiz_manager.next_question()
                self.current_question = self.quiz_manager.get_current_question()
                break

    def update(self):
        pass

    def draw(self):
        self.screen.fill((30, 30, 30))
        if self.current_question:
            self.option_rects = []
            question_text = self.font.render(self.current_question["question"], True, (255, 255, 255))
            self.screen.blit(question_text, (50, 50))

            for i, option in enumerate(self.current_question["options"]):
                rect = pygame.Rect(50, 150 + i * 60, 700, 40)
                pygame.draw.rect(self.screen, (70, 70, 70), rect)
                text = self.font.render(option, True, (255, 255, 255))
                self.screen.blit(text, (60, 160 + i * 60))
                self.option_rects.append(rect)
        else:
            final_text = self.font.render(f"Quiz completed! Score: {self.score_manager.get_score()}", True, (255, 255, 0))
            self.screen.blit(final_text, (50, 50))