from pygame import mixer,mixer_music,USEREVENT,event
from os.path import dirname, join, basename
from glob import glob
from variaveis import *
from sys import platform
import time

tocar = True

def varrer_mp3():
        global nmusicas
        global musicas
        global rodando
        if len(musicas)>0:
                musicas.clear()
                print('limpando lista')
        #varrer pasta
        """
        curdir = dirname(__file__)
        for filename in glob(join(curdir, "D:/Projetos e programas tecnico em informática/SYSTEM/AR/multimidia", '*.mp3')):
            #contar numero de musicas
            nmusicas = nmusicas + 1
            #nome da musica
            print(nmusicas,'°',basename(filename[:-4]).replace('_', ' '))
            #exibir caminhos de musicas
            #print(filename)
            #adicionar a lista de reprodrução
            musicas.append(filename)
            """
        if 'linux' in platform:
                print("""
                _____________________///////
                PLataforma Linux @_@
                --------------------- 
                """)
                try:
                        curdir2 = dirname(__file__)
                        for filename2 in glob(join(curdir2, "/media/the_felipe/Arquivos2/musicas", '*.mp3')):
                            #contar numero de musicas
                            nmusicas = nmusicas + 1
                            #nome da musica
                            print(nmusicas,'°',basename(filename2[:-4]).replace('_', ' '))
                            #exibir caminhos de musicas
                            #print(filename2)
                            #adicionar a lista de reprodrução
                            musicas.append(filename2)
                        if musicas.count==0:
                                 pass

                except:
                       print("Diretórios de músicas não encontrados!...");
        if 'win' in platform:
            print("""
                _____________________=====
                PLataforma WINDOWS @_@
                --------------------- 
                """)
            
            

            try:
                curdir2 = dirname(__file__)
                for filename2 in glob(join(curdir2, "D:/musicas", '*.mp3')):
                    #contar numero de musicas
                    nmusicas = nmusicas + 1
                    #nome da musica
                    print(nmusicas,'°',basename(filename2[:-4]).replace('_', ' '))
                    #exibir caminhos de musicas
                    #print(filename2)
                    #adicionar a lista de reprodrução
                    musicas.append(filename2)

            except:
            
                print("Diretórios de músicas não encontrados!...")
            
            print(platform)    
        print("player mp3 inicializado...") 
                


def inicio():
        global rodando
        global fre
        freq =mixer.get_init()    
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])
        global resp
        resp = str(input("Deseja ouvir  musicas pelo pygame? sim-s/não-n "))
        print(os.get_exec_path(musicas))
       
def inicializar():
        mixer.init(frequency=fre ,size=-16,channels=2,buffer=5996)
        musica = mixer_music.load(musicas[rodando])
        mp3 = mixer.Sound(musicas[rodando])
        mixer.music.set_volume(volume)
        
def iniciar():
        global rodando
        global volume
        global fre
        global musicas
        global inicializou
        global MUSIC_END
        mixer.init(frequency=44100 ,size=-16,channels=2,buffer=5996)
        tocando = mixer_music.get_busy()
        MUSIC_END = 777

        mixer.music.set_endevent(MUSIC_END)
        if tocando==False:
                
                        
                print(mixer.get_init())
                x = mixer_music.get_busy()
                print(musicas[rodando])
                musica = mixer_music.load(musicas[rodando])

                mp3 = mixer.Sound(musicas[rodando])
                pos3 = time.strftime("%H:%M:%S", time.gmtime(mp3.get_length())) 

                mixer_music.set_volume(volume)
                mixer_music.play()
                mixer.music.pause()

                return pos3

        else:
            mp3 = mixer.Sound(musicas[rodando])
            pos3 = time.strftime("%H:%M:%S", time.gmtime(mp3.get_length())) 
            print("já inicializado")
            return pos3
        
        
                
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',basename(musicas[rodando]))
        
def sair():
      
        try:
                mixer_music.stop()
                mixer.quit()
                print("Encerrando music_x player.....")
                
        
        except:
                print("deseja sair mesmo...N/S ou s/n ")
                print("Encerrando music_x player.....")
                
        
def pausar():
    mixer.music.pause()
    print("(PAUSE)")
def continua():
    mixer_music.unpause()

def posicao():
    global MUSIC_END
    print('evento: ',mixer_music.get_endevent())
    
        
    
    #print('vvv',event.get())    
    #print("duração: ",mixer_music.get_length())
    #print("length",a.get_length())
    if mixer.music.get_busy():
        #mp3 = mixer.Sound(musicas[rodando])
        pos2 = time.strftime("%H:%M:%S", time.gmtime(mixer.music.get_pos() / 1000))
        #pos3 = time.strftime("%H:%M:%S", time.gmtime(mp3.get_length())) 
        #pos =str(datetime.timedelta(mixer.music.get_pos() / 1000))
        #print(str(mixer.Sound.get_length(musicas[r'de: ', pos3)

        
        return pos2
    else:
       
        #mp3 = mixer.Sound(musicas[rodando])
        pos2 = time.strftime("%H:%M:%S", time.gmtime(mixer.music.get_pos() / 1000))
        #pos3 = time.strftime("%H:%M:%S", time.gmtime(mp3.get_length())) 
        #print('posicao: ', pos2)
        #print('de: ', pos3)
        
        return pos2


def play_pause():
    nome_musica = basename(musicas[rodando][:-4]).replace('_', ' ')
    situacao = {}
    tocando = mixer_music.get_busy()
    pos = posicao()
    if tocando==False:
        botao = 'Pause'
        situacao = nome_musica + ' - Tocando'
        mixer_music.unpause()
        print("Musica tocando")
        situacao = {'botao':botao,'musica':situacao}
        print("posicao : ", pos)
        return situacao

    else:
        botao = 'Play'
        situacao = nome_musica + ' - Pause'
        mixer_music.pause()
        print("Musica em parad")
        situacao = {'botao':botao,'musica':situacao}
        return situacao

def reinicio():
    mixer_music.rewind()        
    
def aumentar_vol(voll):
    global volume
    volume=self.value
    if volume>1:
            volume=1
            mixer_music.set_volume(volume)
            print('volume: ',str(volume))
    else:
            mixer_music.set_volume(volume)
            print('volume: ',str(volume))

def config_volume(valor):
    
    valor
    mixer_music.set_volume(valor)
    print('volume: ',str(valor))

        
def abaixar_vol(voll):
    global volume
    volume = voll
    if volume<0:
            volume=0
            mixer_music.set_volume(volume)
            print('volume: ',str(volume))
    else:
            vol = mixer.music.set_volume(volume)
            print('volume: ',str(volume))

def avancar():
    #definir a variavel que vai ser usada global na função    
    global rodando
    global musicas
    global fre
    global nome_musica
    musica_atual =''
    try:
        mixer_music.stop
        
        rodando=rodando+1
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])
        nome_musica = basename(musicas[rodando][:-4]).replace('_', ' ')
        print("nome: ",nome_musica)
        

        

    except:
        print("retorno...")
        
        rodando = 0
            
        mixer_music.stop
            
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])
        nome_musica = basename(musicas[rodando][:-4]).replace('_', ' ')
        print("nome: ",nome_musica)
    return nome_musica


def voltar():
    global rodando
    global musicas
    global music_x
    global fre
    global nome_musica
    if rodando<=0:
        music_x = 0
        mixer_music.stop
        l = len(musicas)
        rodando=l-1
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])
        nome_musica = basename(musicas[rodando][:-4]).replace('_', ' ')

        print("nome: ",nome_musica)


    else:
        music_x = 0
        mixer_music.stop
        rodando=rodando-1
        musica = mixer_music.load(musicas[rodando])
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])
        nome_musica = basename(musicas[rodando][:-4]).replace('_', ' ')
        print("nome: ",nome_musica)

    return nome_musica
        
        
def sintonizar_frequencia():
        global rodando
        global volume
        global musicas
        global fre
        fre = int(input("Digite o número da frequência... "))
        
      
           
        mixer.quit()
        mixer.init(frequency=fre)
        musica = mixer_music.load(musicas[rodando])
        mixer.music.set_volume(volume)
        mixer_music.play()
        print("frequênci atual:  ",fre)    
        print(rodando+1,' ',musicas[rodando])

def procurar_p_numeracao():
        music_x = int(input("digite o número da música: "))
        
       
        if music_x>len(musicas):
            print("musica não esta na lista ")
            print("total de musicas listadas: ",len(musicas))
        try:
            rodando = music_x-1
            mixer.quit()
            mixer.init(frequency=fre)
            musica = mixer_music.load(musicas[rodando])
            mixer.music.set_volume(volume)
            mixer_music.play()
            print("frequênci atual:  ",fre)    
            print(rodando+1,' ',musicas[rodando])
        except:
            print("não listado...")
        
def tempo_segundos():
        temp = mixer_music.get_pos()
        print(temp)


