from fastapi import FastAPI, HTTPException
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st
from mysql_chat import get_response, init_database
from schemas import dbModel, ChatRequest

app = FastAPI()

# Global variable for storing chat history, database connection info, and database
chat_history: list = [AIMessage(content="Hello! I am a SQL Assistant. How can I help you?")]
database_data: dbModel = None
data = None
    
@app.get("/")
def init_db():
    print(database_data)
    return {"Hello": "World"}

@app.post("/api/connect-to-db")
async def connect_to_db(db: dbModel):
    global database_data, data
    try:
        database_data = db
        data = init_database(db)
        return {"status": "Connected to database!"}
    except Exception as e:
        return {"status": "Error connecting to database", "error": str(e)}
    
@app.post("/api/get-response")
async def get_response_api(request: ChatRequest):
    global chat_history
    if database_data is None:
        raise HTTPException(status_code=400, detail="Database not connected")
    try:
        chat_history.append(HumanMessage(content=request.user_query))
        print(request.user_query)
        response = get_response(request.user_query, data, chat_history)
        print(response)
        chat_history.append(AIMessage(content=response))
        return {"response": response}
    except Exception as e:
        return {"status": "Error getting response", "error": str(e)}