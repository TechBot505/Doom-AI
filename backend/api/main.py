import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st

load_dotenv()

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  return SQLDatabase.from_uri(db_uri)

def get_sql_chain(db):
    template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
        
        <SCHEMA>{schema}</SCHEMA>
        
        Conversation History: {chat_history}
        
        Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
        
        For example:
        Question: which 3 artists have the most tracks?
        SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
        Question: Name 10 artists
        SQL Query: SELECT Name FROM Artist LIMIT 10;
        
        Your turn:
        
        Question: {question}
        SQL Query:
        """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GEMINI_API_KEY"))
    
    def get_schema(_):
        return db.get_table_info()
    
    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage(content="Hello! I am a SQL Assistant. How can I help you?"),
    ]

st.set_page_config(page_title="Doom AI", page_icon="🤖")
st.title("Doom AI: Chat with MySQL")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using MySQL. Connect to the database and start chatting.")
    
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="rohit", key="Password")
    st.text_input("Database", value="retail_sales_db", key="Database")
    
    if st.button("Connect"):
        with st.spinner("Connecting to database...."):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )
            st.session_state["db"] = db
            st.success("Connected to database!")
    
for message in st.session_state["chat_history"]:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):    
            st.markdown(message.content)
        
user_query = st.chat_input("Type a message...")
if user_query is not None and user_query.strip() != "":
    st.session_state["chat_history"].append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.markdown(user_query)
        
    with st.chat_message("AI"):
        response = db.execute(user_query)
        st.markdown(response)
    st.session_state["chat_history"].append(AIMessage(content=response))