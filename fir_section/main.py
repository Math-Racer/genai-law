import streamlit as st
from logic import query_chromadb, get_llama_response
import webbrowser  # Import webbrowser globally

st.title("AI-Powered FIR Section Finder")
st.write("This app uses an advanced language model (LLaMA 3.2) and a comprehensive knowledge graph (vector database) to accurately generate act and section details.")

query = st.text_input("Describe the incident in detail:")

# query, was_translated = tamil(query)

if st.button("Find Relevant Sections"):
  # Get the closest documents using ChromaDB
  closest_pages = query_chromadb(query)

  # Show the retrieved documents (optional for debugging)

  # Generate a response using Ollama model
  response = get_llama_response(query, closest_pages)

  # if was_translated:
  #   response = translate_to_tamil(response)

  st.write("Relevant Sections:")
  st.write(response)

  with st.expander("Closest Documents"):
    for i, doc in enumerate(closest_pages):
      st.write(f"Document {i+1}: {doc}")

  # Add a button to navigate to another website, shown only after response
  if response:
    st.markdown("[Go draft the FIR](http://127.0.0.1:5000/?act1=IPC&section1=219&act2=IPC&section2=375)", unsafe_allow_html=True)
