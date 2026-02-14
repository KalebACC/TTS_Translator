import setup
from Translator import Translator
from EnglishTTS import EnglishTTS
from FrenchTTS import FrenchTTS

translator = Translator()
enTts = EnglishTTS(voice="en-CA-ClaraNeural")
frTts = FrenchTTS(voice="fr-FR-DeniseNeural")

text = """
  Après avoir passé toute la matinée à courir d’un rendez-vous à l’autre,
  j’ai finalement décidé de faire une pause. Mon patron m’a dit qu’il allait
  “y jeter un coup d’œil”, ce qui, selon moi, signifie généralement que rien
  ne se passera. J’ai pris mon courage à deux mains et j’ai terminé la tâche,
  même si la situation ressemblait à une bombe à retardement.
  Vous savez comment c’est — plus facile à dire qu’à faire.
  """

frTts.frTTS(text)