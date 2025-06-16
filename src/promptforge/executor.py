from promptforge.tools import WikipediaTool, CalculatorTool, TimeTool

def execute_tasks(tasks: list) -> list:
    """
    Esegue ogni task usando il tool corretto e raccoglie i risultati.
    """
    tool_classes = {
        "WikipediaTool": WikipediaTool,
        "CalculatorTool": CalculatorTool,
        "TimeTool": TimeTool
    }

    results = []
    for task in tasks:
        tool_class = tool_classes.get(task["tool"])
        if not tool_class:
            results.append(f"[Errore] Tool '{task['tool']}' non trovato.")
            continue

        tool = tool_class(task["input"])
        output = tool.run()
        results.append(output)

    return results
