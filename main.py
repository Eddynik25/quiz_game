import pygame
from quiz_manager import QuizManager
from score_manager import ScoreManager
from game_ui import GameUI

def show_menu(screen, title, options):
    font = pygame.font.Font(None, 50)
    screen.fill((0, 0, 0))
    title_surf = font.render(title, True, (255, 255, 255))
    screen.blit(title_surf, (200, 50))

    buttons = []
    for i, (label, value) in enumerate(options):
        text = font.render(label, True, (255, 255, 255))
        rect = text.get_rect(center=(400, 150 + i * 100))
        buttons.append((rect, value))
        screen.blit(text, rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for rect, value in buttons:
                    if rect.collidepoint(mouse_pos):
                        return value

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quiz Game")

    category = show_menu(screen, "Choose a category", [("History", "history"), ("Science", "science")])
    difficulty = show_menu(screen, "Choose a difficulty", [("Easy", "easy"), ("Intermediate", "intermediate"), ("Difficult", "difficult")])

    json_path = f"ressources/questions/{category}.json"
    quiz_manager = QuizManager(json_path, difficulty)
    score_manager = ScoreManager()
    game_ui = GameUI(quiz_manager, score_manager, screen)

    game_ui.run()
    pygame.quit()

if __name__ == "__main__":
    main()