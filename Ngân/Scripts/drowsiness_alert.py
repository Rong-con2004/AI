
# Alert functions: alarm and emergency email


# import packages
import pygame

def sound_alarm():
    """The function plays an alarm sound"""
    try:
        pygame.mixer.init()
        alarm_sound = pygame.mixer.Sound("../Data/alarm.wav")
        alarm_sound.play()
    except Exception as e:
        print(f"Error playing alarm sound: {e}")
