import pygame
from pynput.keyboard import Key, Listener

pygame.init()

song = 'fur_elise.txt'

sound_file = 'Piano'


def read_melody(filename):
    with open('Melody/{}'.format(filename)) as f:

        lines = f.readlines()

        for key in range(len(lines)):
            if lines[key][-1:] == '\n':
                lines[key] = lines[key][:-1]

        lines = " ".join(lines)
        lines = lines.split(" ")

        return lines

melody = read_melody(filename=song)


def sharp_cvtr(notes):

    if notes[0].lower() == 'g':
        notes = notes.replace(notes[0],chr(ord(notes[0])-6).lower())

    else:
        notes = notes.replace(notes[0],chr(ord(notes[0])+1).lower())

    notes = notes.replace('#','b')

    return notes


def key_press_event(key):

    for notes in range(len(melody)):
        sound = sound_file+'/'+melody[0].lower()+'.ogg'
        
        if melody[0][1] == '#':
            sound = sound_file+'/'+sharp_cvtr(melody[0]).lower()+'.ogg'
               
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(0)


    melody.append(melody[0])
    melody.pop(0)


obj = Listener(on_press=key_press_event)
obj.start()
obj.join()
