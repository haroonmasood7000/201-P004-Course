from agents import Agent , Runner, AsyncOpenAI , OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os
set_tracing_disabled(disabled=True)

# 1. load the env into  enviroment
load_dotenv()
# 1.1 Extract the required keys
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

print(f"gemini_Api_key {gemini_api_key} \n Gemini Base url {gemini_base_url}")

# 2. Which LLM Service?
external_client: AsyncOpenAI =AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

# 3. Which LLM Model?
model_name:OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model='gemini-2.5-flash',
    openai_client=external_client
)

# 4. Creating the Agent

agent: Agent = Agent(name="AI Assitant", model=model_name)

# 5. running the agent

result = Runner.run_sync(starting_agent=agent, input="Give me Git-Repo to learn open-ai sdk with projects...")


print("Agent Response:\n ", result.final_output)

