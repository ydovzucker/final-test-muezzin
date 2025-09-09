import speech_recognition as sr
from logger import Logger
logger = Logger.get_logger()
class AudioToText:
    def __init__(self):
        self.r = sr.Recognizer()

    def convert_audio_to_text(self,audio_file_path):
        with sr.AudioFile(audio_file_path) as source:
            # Load the audio data into memory
            audio_data = self.r.record(source)

#     # Recognize the speech using Google's Web Speech API (default)
        try:
            text = self.r.recognize_google(audio_data)
            print("Transcription: " + text)
            logger.info("translated audio to text")
        except sr.UnknownValueError:
            logger.error("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
