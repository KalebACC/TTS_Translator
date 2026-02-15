import whisper
import torch

class Transcribe:
  
  def __init__(self,lang: str):
    self.model = whisper.load_model("small")
    self.language = lang
    self.device = "cuda" if torch.cuda.is_available() else "cpu"
  
  def transcribe(self,file:str):
    result = self.model.transcribe(file,language = self.language)
    return result['text']
