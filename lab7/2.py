import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont(None, 48)

mdir = "/Users/ajnelkosekova/Desktop/pp2/lab7/music"

if not os.path.exists(mdir):
    print(f"Error: Directory '{mdir}' not found.")
    pygame.quit()
    sys.exit()

music_files = [f for f in os.listdir(mdir) if f.endswith(('.mp3', '.wav'))]
music_files.sort()

current_music = 0
pygame.mixer.music.load(os.path.join(mdir, music_files[current_music]))

is_playing = False

def play_music():
    global is_playing
    pygame.mixer.music.play()
    is_playing = True

def pause_music():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

def next_music():
    global current_music, is_playing
    current_music = (current_music + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(mdir, music_files[current_music]))
    pygame.mixer.music.play()
    is_playing = True

def prev_music():
    global current_music, is_playing
    current_music = (current_music - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(mdir, music_files[current_music]))
    pygame.mixer.music.play()
    is_playing = True

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pause_music()
                else:
                    play_music()
            elif event.key == pygame.K_ESCAPE:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()

    screen.fill((255, 255, 255))
    text = font.render(music_files[current_music], True, (0, 0, 0))
    text_rect = text.get_rect(center=(width//2, height//2))
    screen.blit(text, text_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

