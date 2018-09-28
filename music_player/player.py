#MIGUEL GRANERO RAMOS


from pygame import mixer
from time import sleep
import os


config_name = 'config.ini'
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_name)

config_file = open(config_path, 'r+')

path = config_file.read()
print (config_file.read())
while path == '': #We check if the file is empty (maybe just created)
    #path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'music') #if you want you can put the music in a folder "music"
    path = input('\nPath for the music: ') 
    config_file.write(path) #We save the config, so we don't have to input the path every time

config_file.close()
valid_formats = ('mp3', 'ogg', 'wav') #These work for sure, others may also work.

mixer.init()
while(True):
    print('\n\n\t\t\tWELCOME TO MIKEPLAYER\n')

    print('Creating list of available music:  \n')
    
    
    files = os.listdir(path) #We read all the directoriesin path
    

    index = 0
    for fil in files:
        if fil.lower().endswith(valid_formats): #We check if the directories (files or folders) have the available format
            print ('[' + str(index) + ']:  ' + fil)
            index+=1
        else:
            files.remove(fil) #We filter the directories


    while True:
        print ('\nPlease select one track by introducing its index number:') #We ask the user to select one track
        try:
            s_track = int(input())
            if s_track >= 0 and s_track < index: #Check for errors
                break
            print('Track ' + str(s_track) + ' doesn`t exist')
        except ValueError:   
            print('Invalid Input')   

    p_track = os.path.join(path, files[s_track])

    print('Playing track ' + str(s_track) + ': ' + files[s_track])
    mixer.music.load(p_track)
    mixer.music.play()
    input('Press enter to stop...') #The music plays until the user presses ENTER
    mixer.music.stop()
