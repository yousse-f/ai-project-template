import re

def analyze_input(user_input: str) -> list:
    """
    Analizza l'input utente e ritorna una lista di intenti identificati.
    Intenti possibili: 'wikipedia', 'calcolo', 'tempo'
    """
    user_input = user_input.lower().replace("’", "'")
    intents = []

    # === INTENTO: Wikipedia ===
    if any(kw in user_input for kw in ["chi è", "cos'è", "cosa significa", "spiegami", "definizione"]):
        # Spezza alla 'e' per evitare frasi troppo lunghe
        wiki_part = user_input.split(" e ")[0]
        
        # Rimuove frasi comuni e mantiene solo la keyword
        wiki_part = re.sub(r"(chi è|cos'è|cosa significa|spiegami|definizione di)", "", wiki_part).strip()
        intents.append(("wikipedia", wiki_part))

    # === INTENTO: Calcolo ===
    if any(op in user_input for op in ["+", "-", "*", "/", "quanto fa", "calcola", "somma", "moltiplica"]):
        intents.append(("calcolo", user_input))

    # === INTENTO: Tempo ===
    if any(word in user_input for word in ["che giorno", "che data", "che ora", "oggi", "adesso", "ora"]):
        intents.append(("tempo", user_input))

    # === Fallback: se non rileva nulla, prova Wikipedia
    if not intents:
        intents.append(("wikipedia", user_input))

    return intents
