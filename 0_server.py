# import streamlit as st
# from openai import OpenAI
# from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

# model_name = "google/flan-t5-small"
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# st.title("ChatGPT-like clone")

# # Set OpenAI API key from Streamlit secrets
# client = OpenAI(api_key="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")

# # Set a default model
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)


# # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         stream = client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )
#         response = st.write_stream(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response})


import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "teknium/Mistral-Trismegistus-7B"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

st.title("Hugging Face Chatbot (Mistral)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Prepare input for the model
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs.to(model.device), max_length=150)  # Adjust max_length as needed
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})