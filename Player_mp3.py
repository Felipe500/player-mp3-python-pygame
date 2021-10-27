5
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from sys import path
path.append("arquivos")
from variaveis import *
from music_funcoes import * 
from pygame import mixer,mixer_music
from os.path import  basename


from kivy.properties import StringProperty, ObjectProperty, NumericProperty

play = False
n1 = 0
som =  ObjectProperty(None, allownone=True)

#Classe de controle
class RootWidget(FloatLayout):
    
    sound = ObjectProperty(None, allownone=True)
    nome_e = mixer_music.get_endevent() 
    print("evento: ",nome_e)





    def posicao2(self):
        posicao_atual = self.ids.barra.value
        posicao_atual += 1
        #while tocando==True:
        self.ids.barra.value = posicao_atual

 

    #def contador(self):
        

        #Clock.schedule_interval(self.imprimir2, 1)
        
    
    def inicio(self):
        if not mixer.get_init():
            varrer_mp3()
            mp3 = iniciar()

        posicao_time = posicao()
        #self.id.tempo2.text = str(pos2)
        #self.ids.tempo.text = 'str(p)'
        #self.posicao2()
        print("contador: ",posicao_time)
        return posicao_time 
        


    def play_musica(self):
        global play
        global n1
           
        nome = play_pause()
        print("situacao--",nome)
        
        self.ids.play_pause.text =nome['botao']
        self.ids.nmusica.text = nome['musica']
   
    def proximo(self):
        nome_musica = avancar()
        self.ids.nmusica.text = nome_musica
        


    def retrocer(self):
        nome_musica = voltar()
        self.ids.nmusica.text = nome_musica

    def confi_voll(sefl,x):
        print("novo voulume",x)
        config_volume(x)

class Player_mp3App(App):
     
     def build(self):
         global fre
         varrer_mp3()
         mp3 = iniciar()

         #print("Duracao: ",mp3)
         #RootWidget.contador(RootWidget)

     def imprimir(dt):

         print("tempo") 
     
     

if __name__ == '__main__':
    Player_mp3App().run()
