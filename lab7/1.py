import pygame 
import sys
from datetime import datetime
import math 

pygame.init()
width, height = 800, 600
center = (400, 300)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
body = pygame.image.load('clock.png')
min_hand = pygame.image.load('min_hand.png')
sec_hand = pygame.image.load('sec_hand.png')

def rotate_image (image, angle, pivot):
        w, h = image.get_size()
        offset = pygame.math.Vector2(0, -height/2)
        rotated_image = pygame.transform.rotate(image, -angle)
        rotated_offset = offset.rotate(-angle)
        rect = rotated_image.get_rect(center=pivot +rotated_offset)
        return rotated_image, rect
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        body_rect = body.get_rect(center=center)
        screen.blit(body, body_rect)

        now = datetime.now()
        minutes = now.minute
        seconds = now.second

        m_angle = (minutes/60)*360
        s_angle = (seconds/60)*360

        right_hand_image, right_hand_rect = rotate_image(min_hand, m_angle, center)
        left_hand_image, left_hand_rect = rotate_image(sec_hand, s_angle, center)

        screen.blit(right_hand_image, right_hand_rect)
        screen.blit(left_hand_image, left_hand_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()