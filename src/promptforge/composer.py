def compose_response(user_input: str, results: list) -> str:
    """
    Combina i risultati ottenuti dai tool in una risposta coerente per l'utente.
    """
    if not results:
        return "Non sono riuscito a trovare una risposta utile."

    response = "Ecco cosa ho trovato:\n\n"
    for result in results:
        response += f"- {result}\n"

    return response.strip()
