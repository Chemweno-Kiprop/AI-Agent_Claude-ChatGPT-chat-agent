from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
 
# --- Load environment variables ---
load_dotenv()

# --- Choose which LLM provider to use ---
# Options: "gemini", "claude", "openai"
PROVIDER = "gemini"   # to test different APIs

# --- GEMINI (Google Generative AI) ---
if PROVIDER == "gemini":
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("What is the meaning of life?")
    print("🤖 Gemini response:\n", response.text)

# --- CLAUDE (Anthropic) ---
elif PROVIDER == "claude":
    llm = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",  # or claude-3-opus
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    )
    response = llm.invoke("What is the meaning of life?")
    print("🧠 Claude response:\n", response.content)

# --- CHATGPT (OpenAI) ---
elif PROVIDER == "openai":
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # or gpt-4o
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    response = llm.invoke("What is the meaning of life?")
    print("💬 ChatGPT response:\n", response.content)

else:
    raise ValueError("Invalid PROVIDER selected. Use: gemini, claude, or openai.")
