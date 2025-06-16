def plan_tasks(intents: list) -> list:
    """
    Riceve una lista di intenti e assegna il tool corretto.
    Output: lista di dizionari con 'tool' e 'input'
    """
    tool_map = {
        "wikipedia": "WikipediaTool",
        "calcolo": "CalculatorTool",
        "tempo": "TimeTool"
    }

    tasks = []
    for intent_type, content in intents:
        tool_name = tool_map.get(intent_type)
        if tool_name:
            tasks.append({
                "tool": tool_name,
                "input": content
            })

    return tasks
