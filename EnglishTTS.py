import asyncio
from datetime import datetime
import edge_tts

class EnglishTTS:
  def __init__(self, voice: str = "en-US-JennyNeural"):
    self.voice = voice

  async def _tts_async(self, text: str, filename: str):
    communicate = edge_tts.Communicate(text, self.voice)
    await communicate.save(filename)

  def enTTS(self, text: str, filename: str = None):
    if filename is None:
      timestamp = datetime.now().strftime("%Y-%m-%d %H-%M")
      filename = f"Translation_{timestamp}.mp3"
    asyncio.run(self._tts_async(text, filename))
    print(f"Translation Complete: saved as {filename}")
