import os
def robo_speaker():
    print("Welcome to RoboSpeaker 1.1 Created by Sandhya")
    while True:
         x=input("Enter what you want to speak:")
         if x.lower()=='exit':
              print("Exiting Robospeaker.Goodgbye")
              break
         os.system(f"powershell -c Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')")
              
if __name__=="__main__":
     robo_speaker()