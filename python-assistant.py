

import pyttsx3 # text to speech conversion library 
import datetime # required for making a wish in accordance with time
import speech_recognition as sr
import wikipedia # for queries reated to wikipedia



engine = pyttsx3.init('sapi5')  #opject creation for microsoft voice recognition API's
voices = engine.getProperty('voices') # for getting the details of the current voice
#print(voices)
print(voices[0].id) # this will print 'ZIRA FOR 1 ' and 'DAVID FOR 0'
engine.setProperty('voice', voices[0].id) # changing the index, changing the voices , 1 for female and 0 for male



def speak(audio):

	engine.say(audio)
	engine.runAndWait()

def timewish():
	hour = int(datetime.datetime.now().hour)  # from 0 to 24
	
	if hour>=0 and hour<12:
		speak("GOOD MORNING DEAR!! HAVE A BEAUTIFUL AND EFFICIENT WORKING DAY TODAY")
	
	elif hour>=12 and hour<16:
		speak("GOOD AFTERNOON DEAR!! HAVE A AN INSPIRING AFTERNOON!!")

	else:
		speak("WISHING YOU A VERY GOOD EVENING DEAR!! HAVE A WONDERFUL EVENING AHEAD AND MAY YOU END YOUR DAY WITH A ")

	#speak("I AM JARVIS , PLEASE TELL ME HOW MAY I HELP YOU ")


def takecommand():
	# it takes the input from microphone from the user and  a string will be the output

	r = sr.Recognizer() # this command will help us in recognizing the audio

	with sr.Microphone() as source:
		print("I am Listening.........!!")
		#r.pause_threshold() = 1 # a gap of 1 second
		audio = r.listen(source)


  try:
	  print("Recognizing...")    
	    query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
	    print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query



if __name__ == "__main__":

	timewish()
	# logic for execution of the task to be performed
	while True:
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query, sentences=2) 
			speak("According to Wikipedia")
			print(results)
			speak(results)
			#speak('Searching your query over Wikipedia........')
			#query = query.replace("wikipedia", "")
			#results = wikipedia.summary(query, sentences=5)
			#speak("According to WIKIPEDIA ")
			#speak(results)			
	
	
	#speak("how aree you ")
