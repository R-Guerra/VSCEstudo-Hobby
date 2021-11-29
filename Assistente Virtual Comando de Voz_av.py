import speech_recognition as sr
import playsound
#from playsound import playsound 
from gtts import gTTS, tts
#import gtts
import random
import webbrowser
import pyttsx3
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import pyautogui



class Virtual_assit():
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        
        self.voice_data = ''

    def engine_speak(self, text):
        """
        fala da assitente virtual
        """
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()
        

    def record_audio(self, ask=""):


        with sr.Microphone() as source:
            if ask:
                print('Gravando...')
                self.engine_speak(ask)

            audio = self.r.listen(source,5 , 5)# pega dados de auido
            print('Analisando.')
            try:
                self.voice_data = self.r.recognize_google(audio) #converte audio para texto

            except sr.UnknownValueError:
                self.engine_speak('Repita.')

            except sr.RequestError:
                self.engine_speak('Desculpe chefe. Meu servidor está fora do ar.') # recognizer is not connected

            print(">>",self.voice_data.lower()) #imprime o que vc disse
            self.voice_data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_strig):
        audio_strig = str(audio_strig)
        tts = gTTS(text=audio_strig, lang='pt-br')
        r = random.randint(1,20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assit_name + ':', audio_strig)
        os.remove(audio_file)


    def there_exist(self, terms):
        """
        função para identificar se o termo existe
        """
        for term in terms:
            if term in self.voice_data:
                return True


    def respond(self, voice_data):
        if self.there_exist(['bom dia', 'bon gia', 'bongia', 'bojia', 'mangia', 
        'bone kia', 'bonekia', 'bon jia', 'oi', 'holy', 'boy', 'we', 'sasha', 'sacha', 'saxa',
        'bom dia sasha', 'bon gia sasha', 'bongia sasha', 'bojia sasha', 'mangia sasha', 'oi sahsa',
        'holy sasha', 'boy sasha', 'we sasha', 'mogea sash', 'mogea sasha', 'bougie massage',
        'borges ash', 'andouille sausage', 'mogia', 'mogea', 'acorda sasha', 'aquada sasha', 'vamos trabalhar',
        'aquada sasha vamos trabalhar', 'sasha acorda', 'oi sasha', 'boy sasha', 'we sasha']):
            greetigns = [f'Oi senhor {self.person}, o que iremos fazer hoje?',
                        'Olá chefe, como posso te ajudar?',
                        'Oi chefe, o que posso fazer pelo senhor?',
                        'Olá chefe, estou as ordens.']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)

        #google
        #if self.there_exist(['procure por', 'procuri por', 'bucuti', 'bucuti por', 'photo cory', 'bucuti cory',
        #'photo cody', 'but okuti', 'procula', 'roku reboot', 'blucora', 'bucuti pool']) and 'youtube' not in voice_data:
            #search_term = voice_data.split("por")[-1]
            #url =  "http://google.com/search?q=" + search_term
            #webbrowser.get().open(url)
            #self.engine_speak("aqui está o que eu encontrei sobre " + search_term + 'no google')
        if self.there_exist(['entra no google', 'entrar no google', 'anthony google', 'anthem google', 'oriental google',
        'abrir google', 'abre o google', 'amtrak google']):
            url =  "http://google.com/"
            webbrowser.get().open(url)
            self.engine_speak("Entrando no google")

        #Fechar Google
        if self.there_exist(['fechar google', 'fish google', 'fexar google', 'fischer google', 
        'official google', 'keisha google', 'fishal google']):
            self.engine_speak("Fechando Google")
            pyautogui.hotkey('ctrl', 'w')

        #youtube 
        if self.there_exist(['entra no youtube', 'entrar no youtube', 'oriental youtube',
        'abrir youtube', 'abre o youtube', 'anthem youtube', 'amtrak youtube', 'anthony youtube']):
            #search_term  = voice_data.split("por")[-1]
            #url = "http://www.youtube.com/results?search_query=" + search_term
            #self.engine_speak("aqui está o que eu encontrei sobre" + search_term + 'no youtube')
            url = url = "http://www.youtube.com/"
            webbrowser.get().open(url)
            self.engine_speak("Entrando no youtube")

        #Fechar Youtube
        if self.there_exist(['fechar youtube', 'fecha o youtube', 'fish o youtube', 'fischer o youtube',
        'official o youtube', 'keisha o youtube', 'fishal o youtube', 'fish youtube', 'fischer youtube',
        'official youtube', 'keisha youtube', 'fishal youtube', 'special youtube', 'fish on youtube',
        'fisher youtube', 'cheshire oil tube', 'fish are youtube' ]):
            self.engine_speak("Fechando youtube")
            pyautogui.hotkey('ctrl', 'w')


        #yahoo mail
        if self.there_exist(['entra no yahoo', 'antonia who', 'anthony yahoo', 'anthem yahoo', 'abre o yahoo', 'abrir yahoo'
        'yahoo', 'tell me who', 'antonia who', 'aguardiente aluno yahoo','oriental yahoo', 'abrir yahoo',
        'abrir o yahoo']):
            #search_term = voice_data.split("no")[-1]
            url = "https://br.yahoo.com/"
            webbrowser.get().open(url)
            self.engine_speak("Entrando no yahoo")
        
        #sap
        if self.there_exist(['open sap']):
            pass


assistent = Virtual_assit('Sasha', 'Guerra')

#iniciandosistema = ('Iniciando Sistema Sasha. Versão zero ponto um. Modelo em teste alpha')
#assistent.engine_speak(iniciandosistema)

#fraseinicial = ('Olá. Eu sou a Sasha. O protótipo de i a criado por Ruan Guerra.')
#assistent.engine_speak(fraseinicial)


while True:
    
    voice_data = assistent.record_audio('Escutando...')
    assistent.respond(voice_data)

    if assistent.there_exist(['hockey', 'okay', 'waukee', 'bucky', 'desligar', 'dish liga', 'desligar sistema', 'these liga', 'theseliga',
    'deja libre', 'dejalibre', 'disregard', 'disregard system', 'disregardsystem', 'disregard sistema', 'disregardsistema',
    'fisher system', 'fishersystem', 'fish assistant', 'fishassistant', 'fish osteoma', 'fishosteoma', 'disregard sistema', 'these legal system',
    'regal cinema', 'digital system', 'digital graphics tama', 'keisha system', 'keisha sistema', 'digital assistant', 'disney customer', 'vitalmed',
    'vai dormir vai', "i don't know if i",'why do women lie', 'little me by', 'vai dormir', 'lithinia weather', 'vital me', 'vital honey',
    'vitamin y', "why don't my wife", 'bible mirai', 'michael malloy', 'lego movie', 'little me']):
        msgs = [f'Ok chefe. Desligando', 'Desligando sistema', 'Ok. Tenha um bom dia, senhor', 'Entendido. Desligando sistema',
        'Entendido. Fechando sistema']
        msg = msgs[random.randint(0,len(msgs)-1)]
        assistent.engine_speak(msg)
        #assistent.engine_speak("Ok. Tenha um bom dia, senhor")
        break