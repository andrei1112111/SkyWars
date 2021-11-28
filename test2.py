import cv2
import pygame

pygame.init()
cap = cv2.VideoCapture('video.mp4')
pygame.mixer.music.load("sound.mp3")
success, img = cap.read()
shape = img.shape[1::-1]
wn = pygame.display.set_mode(shape)
clock = pygame.time.Clock()
pygame.mixer.music.play()

while success:
    clock.tick(24)
    success, img = cap.read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            success = False
    wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
    pygame.display.update()

pygame.quit()
