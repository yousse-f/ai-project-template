import datetime
import wikipedia
import openai
import spacy
import os
from typing import Optional
from dotenv import load_dotenv


# Carica modello italiano spaCy
nlp = spacy.load("it_core_news_sm")

# Carica variabili d'ambiente
load_dotenv()

# Imposta chiave API OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key


class WikipediaTool:
    def __init__(self, query: str):
        self.query = query

    def extract_entity(self, text: str) -> Optional[str]:
        """
        Estrae un'entità semantica (persona, organizzazione, luogo, ecc.) usando spaCy
        """
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ in ("PER", "ORG", "LOC", "MISC") and len(ent.text) > 3:
                return ent.text
        return None

    def run(self) -> str:
        entity = self.extract_entity(self.query)
        if not entity:
            return "[WikipediaTool Error] Nessuna entità trovata nell'input."

        try:
            wikipedia.set_lang("it")
            summary = wikipedia.summary(entity, sentences=2)
            return summary
        except Exception as e:
            return f"[WikipediaTool Error] {e}"


class CalculatorTool:
    def __init__(self, query: str):
        self.query = query

    def run(self) -> str:
        try:
            prompt = f"Rispondi solo con il risultato del seguente calcolo matematico: {self.query}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Sei una calcolatrice che restituisce solo il numero risultato."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message["content"].strip()
            return f"Il risultato di {self.query} è {result}."
        except Exception as e:
            return f"[CalculatorTool Error] {e}"


class TimeTool:
    def run(self) -> str:
        now = datetime.datetime.now()
        giorno = now.strftime("%A, %d %B %Y")
        ora = now.strftime("%H:%M")
        return f"Oggi è {giorno}, sono le {ora}."


# Mappa dei tool disponibili (stringa -> classe)
tool_registry = {
    "wikipedia": WikipediaTool,
    "calcolo": CalculatorTool,
    "tempo": TimeTool,
}
