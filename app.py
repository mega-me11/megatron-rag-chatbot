import subprocess

if __name__ == "__main__":
    subprocess.run(["streamlit", "run", "streamlit_app.py"])
    
    
    
#User → Llama3 → answer = general mode
#User → query → embeddings → Chroma → context → Llama3 → answer = PDF mode