import setup
from Translator import Translator
from Transcribe import Transcribe

translator = Translator()
enTranscriber = Transcribe("en")
frTranscriber = Transcribe("fr")

print(frTranscriber.transcribe("Translation_2026-02-14 20-22.mp3"))
