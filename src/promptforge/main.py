from promptforge.analyzer import analyze_input
from promptforge.planner import plan_tasks
from promptforge.executor import execute_tasks
from promptforge.composer import compose_response

def run_pipeline(user_input: str) -> str:
    # 1. Analizza input utente
    intents = analyze_input(user_input)

    # 2. Pianifica i task da eseguire
    tasks = plan_tasks(intents)

    # 3. Esegue i tool selezionati per ogni task
    results = execute_tasks(tasks)

    # 4. Compone la risposta finale
    final_response = compose_response(user_input, results)

    return final_response

# Per testing rapido via CLI
if __name__ == "__main__":
    while True:
        user_input = input("\nUtente: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("\n🧠 Agente:\n", run_pipeline(user_input))
