# 🌦️ Weather Agent using LangChain + Ollama

This project is a simple AI-powered weather assistant built using:

* LangChain Agents
* Ollama (local LLM - Llama 3.2)
* Python
* wttr.in (free weather API, no key required)

The agent takes a city name as input and returns real-time weather details.

---

## 🚀 Features

* Uses a **local LLM (Ollama)** → no OpenAI API needed
* Fetches **live weather data**
* Uses **LangChain agent + tools architecture**
* Simple CLI-based interaction

---

## 📦 Requirements

* Python 3.10+
* Ollama installed and running
* Internet connection (for weather API)

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install langchain langchain-ollama requests python-dotenv
```

### 4. Install & Run Ollama

Install from: https://ollama.com

Then pull the model:

```bash
ollama pull llama3.2
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then enter a city name:

```
Ask weather of a city: Mumbai
```

Example output:

```
Weather in Mumbai:
🌡️ Temperature: 32°C
🤒 Feels like: 36°C
💧 Humidity: 70%
🌥️ Condition: Partly cloudy
```

---

## 🧠 How It Works

1. User inputs a city name
2. LangChain agent processes the request
3. Agent decides to call `get_weather` tool
4. Tool fetches data from `wttr.in` API
5. Response is formatted and returned

---

## 📁 Project Structure

```
.
├── main.py          # Main script
├── .env             # Environment variables (optional)
├── README.md        # Project documentation
```

---

## 🔧 Code Highlights

### Weather Tool

```python
def get_weather(city: str) -> str:
```

* Calls `wttr.in`
* Parses JSON response
* Returns formatted weather info

---

### Agent Setup

```python
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
```

---

## 🛠️ Future Improvements

* Add multi-tool support (news, stocks, etc.)
* Build a web UI (Streamlit / React)
* Add caching for faster responses
* Add error handling for invalid cities

---

## 🧪 Example Ideas

Try asking:

* Delhi
* New York
* Tokyo
* London

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Your Name
