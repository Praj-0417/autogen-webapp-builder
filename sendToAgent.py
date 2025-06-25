import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

def callAgentAPI(agent_id, user_input):
    """
    Calls the agent.ai API for the given agent_id with user input.
    Returns the JSON response or raises an error.
    """
    API_KEY = os.getenv("AGENT_API_KEY")
    if not API_KEY:
        raise ValueError("❌ AGENT_API_KEY not found in environment variables!")

    url = "https://api-lr.agent.ai/v1/action/invoke_agent"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "id": agent_id,
        "user_input": user_input
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error calling agent '{agent_id}': {e}")
        return {"error": str(e)}


# Example usage:
if __name__ == "__main__":
    agent = "orchestrate-tech"
    prompt = "Build a simple portfolio website"
    result = callAgentAPI(agent, prompt)
    print(json.dumps(result, indent=2))
