
# 🧠 PromptForge – Modular MCP Agent Framework

**PromptForge** è un agente AI modulare basato su architettura MCP (Multi-Component Prompting).  
Costruito in Python, utilizza un flusso a componenti per analizzare input, pianificare task, selezionare strumenti reali, eseguirli e generare risposte finali — tutto **senza richiedere LLM o chiavi API**.

---

## ✅ Funzionalità

- 🧠 **Analyzer**: rileva gli intenti dell'utente da testo naturale
- 🧾 **Planner**: definisce una sequenza di task
- 🛠 **Tool Executor**: esegue strumenti reali (Wikipedia, Calcolatrice, Data/Ora)
- 📦 **Tool reali**:
  - `WikipediaTool` → riassume concetti da Wikipedia
  - `CalculatorTool` → esegue operazioni aritmetiche
  - `TimeTool` → restituisce data/ora formattate
- 🧵 **Composer**: genera una risposta finale coerente

---

## 🗂 Struttura del modulo

src/promptforge/
├── analyzer.py # Estrae gli intenti
├── planner.py # Pianifica quali tool usare
├── tools.py # Tool reali Python
├── executor.py # Esegue i task selezionati
├── composer.py # Compone la risposta finale
├── main.py # Orchestratore MCP
├── prompts/ # Prompt modulari (placeholder per integrazione GPT)
│ ├── system.txt
│ ├── planner.txt
│ ├── tool_selector.txt
│ └── composer.txt

yaml
Copia
Modifica

---

## 🚀 Esecuzione da terminale

Assicurati di essere nella root del progetto `ai-project-template`, quindi lancia:

```bash
PYTHONPATH=src python src/promptforge/main.py
Esempio di input:

bash
Copia
Modifica
Cos'è l'intelligenza artificiale e che giorno è oggi?
🧪 Debug via Notebook
Puoi testare i singoli componenti del flusso nel file:

bash
Copia
Modifica
notebooks/test_promptflow.ipynb
Con cella tipo:

python
Copia
Modifica
from promptforge.main import run_pipeline
print(run_pipeline("Quanto fa 12 * 7 e chi ha inventato Python?"))
🔌 Dipendenze
Installa le librerie necessarie:

bash
Copia
Modifica
pip install wikipedia
(Se in futuro userai GPT: pip install openai python-dotenv)

📎 Esempi supportati
Input utente	Tool attivati
“Cos'è il machine learning e che giorno è oggi?”	WikipediaTool, TimeTool
“Quanto fa 12 * 23 e chi ha inventato Python?”	CalculatorTool, WikipediaTool
“Parlami di innovazione digitale”	WikipediaTool (fallback)

📐 Filosofia MCP
Multi-Component Prompting = orchestrazione manuale di moduli semantici

Ogni modulo (Analyzer, Planner, Tool Executor, Composer) può:

essere controllato direttamente

essere sostituito con un GPT prompt-based

essere testato singolarmente

Questa architettura è il cuore di tutti gli agenti intelligenti moderni.

🧱 Prossimi step consigliati
Integrazione GPT nel planner o composer

Nuovi tool: API meteo, PDF summarizer, AI model evaluator

Frontend live con Streamlit o FastAPI + WebSocket

Riconoscimento di intenti multipli e chaining di tool

👤 Autore
Creato da @yousse-f
Parte del percorso personale per diventare AI Engineer top-tier (estate 2025)

yaml
Copia
Modifica

---

✅ Appena lo incolli e salvi, `promptforge` è documentato come un modulo riusabile e dimostrabile da portfolio.

Scrivimi **"README salvato"** quando hai incollato,  
e decidiamo il prossimo step: debug, estensioni o Fase 2 (RAG).
