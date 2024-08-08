import pygame
pygame.init()
font = pygame.font.Font(None,20)

def debug(label, info, y=10, x=10):
    # Проверяем, является ли info списком
    if isinstance(info, list):
        # Преобразуем элементы списка в строку и округляем их, если это возможно
        info = [round(elem, 5) if isinstance(elem, (float, int)) else elem for elem in info]
        # Соединяем элементы списка в строку через запятую
        info = ', '.join(map(str, info))
    elif isinstance(info, (float, int)):
        # Если это число, округляем до одного десятичного знака
        info = round(info, 5)

    display_surface = pygame.display.get_surface()
    # Используем f-строку для более читаемого вывода
    debug_surf = font.render(f"{label}: {info}", True, 'white')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)