from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import AIMessage, HumanMessage
from mysql_chat import get_response, init_database
from groq_pdf_chat import get_pdf_text, get_text_chunks, get_vector_store, user_input
from schemas import dbModel, ChatRequest

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable for storing chat history, database connection info, and database
chat_history: list = [AIMessage(content="Hello! I am a SQL Assistant. How can I help you?")]
database_data: dbModel = None
data = None
save_to = None

@app.post("/api/connect-to-db")
async def connect_to_db(db: dbModel):
    global database_data, data
    try:
        database_data = db
        data = init_database(db)
        return {"message": "Connection Established! You can now start querying the database.."}
    except Exception as e:
        return {"status": "Error connecting to database", "error": str(e)}
    
@app.post("/api/get-response")
async def get_response_api(request: ChatRequest):
    global chat_history
    try:
        chat_history.append(HumanMessage(content=request.user_query))
        response = get_response(request.user_query, data, chat_history)
        print(response)
        chat_history.append(AIMessage(content=response))
        return {"response": response}
    except Exception as e:
        return {"status": "Error getting response", "error": str(e)}

@app.post("/api/upload-file")
async def upload_file(file: UploadFile):
    global save_to
    try:
        pdf = await file.read()
        save_to = f"uploads/{file.filename}"
        with open(save_to, "wb") as f:
            f.write(pdf)
            text = get_pdf_text(save_to)
            text_chunks = get_text_chunks(text)
            get_vector_store(text_chunks)
        return {"status": "File uploaded successfully", "filename": file.filename}
    except Exception as e:
        return {"status": "Error uploading file", "error": str(e)}

@app.post("/api/get-ai-response")
def get_ai_response(request: ChatRequest):
    if save_to is None:
        raise HTTPException(status_code=400, detail="No file uploaded")
    try:
        response = user_input(request.user_query)
        return {"response": response}
    except Exception as e:
        return {"status": "Error getting response", "error": str(e)}