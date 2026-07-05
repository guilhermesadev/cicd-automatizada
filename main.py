from fastapi import FastAPI

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Define a rota principal (raiz) com o método GET
@app.get("/")
def read_root():
    return {"message": "Hello World"}