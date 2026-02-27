import streamlit as st
from openai import OpenAI
import os

# --- 1. SETUP & CONFIG ---

IMAGE_PATH = os.path.join("images", "PCOS.png", "3.png")
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# Initialize Groq client globally (outside function)
if GROQ_API_KEY:
    groq_client = OpenAI(
        base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY
    )
else:
    groq_client = None

#
MODELS = {
    "🚀 Llama 4 Scout (Best Overall)": "llama-4-scout",
    "⚡ Llama 3.1 8B (Fastest)": "llama-3.1-8b",
    "💪 Llama 3.3 70B (Most Capable)": "llama-3.3-70b",
    "🔧 Qwen 3 32B (Balanced)": "qwen-3-32b",
    "🌟 Llama 4 Maverick (Advanced)": "llama-4-maverick",
}


# --- 2. AI LOGIC ---
def ask_groq(query, model_choice="llama-3.1-8b"):
    """Get response from Groq API"""
    if not groq_client:
        return "Error: API Key is missing. Please check your configuration."

    try:
        # System Instruction for Cora
        system_prompt = """
        You are 'Cora', a specialized medical AI assistant for PCOS (Polycystic Ovary Syndrome).
        
        Rules:
        1. Only answer queries related to PCOS, hormonal health, and related metabolic issues.
        2. If the user asks about unrelated topics, politely say: 
           "I am Cora, your PCOS companion. I can only assist with questions regarding PCOS and hormonal health."
        3. Always include a short medical disclaimer at the end of long responses.
        4. Keep your tone supportive, clean, and professional.
        """

        response = groq_client.chat.completions.create(
            model=model_choice,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=0.9,
        )

        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        if "rate limit" in error_msg.lower():
            return "⚠️ I'm currently experiencing high demand. Please wait a moment and try again. (Rate limit reached - Groq's free tier gives 14,400 requests/day!)"
        else:
            return f"Cora is currently unavailable. Error: {error_msg}"


# --- 3. STREAMLIT UI ---
def app():
    st.title("🩺 Talk to Cora")

    # Display image if exists
    if os.path.exists(IMAGE_PATH):
        st.image(IMAGE_PATH, width=300)

    st.info("Ask Cora anything about PCOS symptoms, lifestyle, or medical terminology.")

    # Initialize chat history using session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat Input Section
    with st.form("chat_form", clear_on_submit=True):
        user_query = st.text_input("Type your message here:")
        submit_button = st.form_submit_button("Send to Cora")

    if submit_button and user_query:
        with st.spinner("Cora is typing..."):
            answer = ask_groq(user_query)

            st.session_state.chat_history.insert(0, ("You", user_query))
            st.session_state.chat_history.insert(0, ("Cora", answer))

    # Display chat history
    st.divider()
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.chat_message("user").write(message)
        else:
            st.chat_message("assistant", avatar="🌸").write(message)


if __name__ == "__main__":
    app()
