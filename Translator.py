from transformers import MarianMTModel, MarianTokenizer

class Translator:
  def __init__(self):
    self.en_fr_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    self.en_fr_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    self.fr_en_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
    self.fr_en_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
    self.en_fr_model.config.tie_word_embeddings = False
    self.fr_en_model.config.tie_word_embeddings = False

  def en_to_fr(self, text : str):
    inputs = self.en_fr_tokenizer(text, return_tensors="pt")
    output = self.en_fr_model.generate(**inputs)
    return self.en_fr_tokenizer.decode(output[0], skip_special_tokens=True)

  def fr_to_en(self, text : str):
    inputs = self.fr_en_tokenizer(text, return_tensors="pt")
    output = self.fr_en_model.generate(**inputs)
    return self.fr_en_tokenizer.decode(output[0], skip_special_tokens=True)
