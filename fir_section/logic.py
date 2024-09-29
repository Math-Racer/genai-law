import chromadb
import ollama
import pypdf

def read_txt_file_to_string(file_path):
  try:
    with open(file_path, 'r') as file:
      content = file.read()
    return content
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None 


prompt_template = read_txt_file_to_string("prompt_template.txt")

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=r"C:\Users\vijay\Documents\MyPrograms\genai law\fir")
collection = client.get_or_create_collection("IPC")


# Fine-tuning with relevant data
def upload_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = pypdf.PdfReader(file)
        id = 0
        for page in pdf_reader.pages:
            # Generate a unique ID for each page
            doc_id = f"{file_path}{id}"
            
            # Check if the document with the same ID already exists in the collection
            existing_docs = collection.get(ids=[doc_id])
            
            if not existing_docs["ids"]:  # If the ID doesn't exist, add the document
                collection.add(
                    documents=[page.extract_text()],
                    ids=[doc_id]
                )
            id += 1


upload_pdf("indian-penal-code.pdf")


def query_chromadb(query, n_results=3):
    """
    Queries ChromaDB and returns the closest pages/documents.
    """
    closest_pages = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return closest_pages["documents"][0]


def get_llama_response(user_query, closest_pages):
    """
    Generates a response using the Ollama Llama model based on the closest pages.
    """
    complete_prompt = prompt_template + user_query
    response = ollama.chat(
        model="tinyllama",
        # model = " llama3.2",
        messages=[
            {
                "role": "system",
                "content": closest_pages[0]
            },
            {
                "role": "system",
                "content": closest_pages[1]
            },
            {
                "role": "system",
                "content": closest_pages[2]
            },
            {
                "role": "user",
                "content": complete_prompt
            }
        ]
    )
    return response["message"]["content"]
