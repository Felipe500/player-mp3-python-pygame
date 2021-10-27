from pygame import mixer,mixer_music
from glob import glob
from os.path import dirname, join, basename
import os
from music_funcoes import *





#buscar directorios de musicas e pastas(path) 
#print(listdir('e:/Ar'))


varrer_mp3()


print(os.curdir.format("*.mp3"))

mixer.init(frequency=fre ,size=-16,channels=2,buffer=5996)  
while tocar==True:
    
     
    
    freq =mixer.get_init()    

    
    resp = str(input("Deseja ouvir  musicas pelo pygame? sim-s/não-n "))
    o = mixer.get_busy()
    
    """if o==0:
        parar=False
        while parar==False:
            mixer.quit()
            mmixe=mmixe+100
            fre = mmixe
            zn = mixer.get_busy()
            o = zn
5            
            mixer.pre_init(frequency=mmixe)
            musica = mixer_music.load(musicas[rodando])
            print("corrigindo audio, aguarde...")
            print(fre ,'  ','mixer',o)
        if o == 1:
            
            mixer.music.set_volume(volume)
            mixer_music.play()
            break
       
    """
   
    if resp == 'temp':
        tempo_segundos()
    
    if o ==0:
        print("erro na frequencia")
    if mixer_music == False:
        print("não legal")
    
    #iniciar audio
    if resp == 's' or resp == 'sim' or resp=='S':
        iniciar()    
        
    #encerrar audio        
    elif resp == 'n' or resp=='nao' or resp=='N':
        sair()
        tocar=False

    #PAUSAR AUDIO
    elif resp == 'p' or resp == 'P':
        pausar()
    #CONTINUAR    
    elif resp == 'c' or resp == 'C':
        continua()

    #Reiniciar
    elif resp == 'r' or resp == 'R':
        
        reinicio()  
    #AUMENTAR VOLUME
    elif resp == '=' or resp=='+':
       aumentar_vol()
        
    #ABAIXAR VOLUME
    elif resp == '_' or resp=='-':
        abaixar_vol()
        
    #EXIBIR VOLUME    
    elif resp == 'vol' or resp == 'volume':
        print('volume: ',str(volume))

    #AVANÇAR
    elif resp == '>':
        avancar()
            

     #voltar   
    elif resp == '<':
        voltar()

    #lista musicas   
    elif resp == 'mm':
        n=0
        for x in musicas:
            n=n+1
            print('musicas:',n,'°' ,x)
     #exibir número de musicas       
    elif resp == 'nn' or resp=='show':
        print('número de musicas: ',len(musicas))
    #procurar sintonia de frequencia de som 
    elif resp == 'fre':
        sintonizar_frequencia()
    #buscar por numeração na lista      
    elif resp == 'buscar' or resp == 'scaner' or resp=='iniciar' or resp=='start':
        procurar_p_numeracao()
          


    elif resp == 'helpe' or resp=='ajuda':
        print("......................")
