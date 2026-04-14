from langchain_ollama import ChatOllama
from langchain.agents import create_agent
import requests

from dotenv import load_dotenv
load_dotenv()


# Local model
model = ChatOllama(
    model="llama3.2:latest"
)

import requests

def get_weather(city: str) -> str:
    """Get weather for a given city (no API key needed)."""

    try:
        url = f"https://wttr.in/{city}?format=j1"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return f"Error: Unable to fetch weather ({response.status_code})"

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]

        return (
            f"Weather in {city}:\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"🤒 Feels like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌥️ Condition: {description}"
        )

    except Exception as e:
        return f"Error fetching weather: {str(e)}"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": input("Ask wheather of a city : ")}]}
)

print(response["messages"][-1].content)