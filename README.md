# DOOM AI: Intelligent Chat
Welcome to **Doom AI**, an intelligent chat platform that allows users to interact with both **PDF files** and **MySQL databases** using natural language. The system leverages advanced AI models to interpret user queries and provide meaningful responses based on the provided documents or database. This project is built to be highly responsive, supporting all devices, and includes light/dark mode functionality for enhanced user experience.

![Screenshot (581)](https://github.com/user-attachments/assets/dc5760cb-f248-4d0e-9432-8d5812de5997)

## Features
* **Chat with PDFs:** Upload PDF files and ask questions. The system intelligently parses the document and answers user queries.

![Screenshot (580)](https://github.com/user-attachments/assets/a5931a60-fa00-4882-ada0-149f677417a3)

* **Chat with MySQL Databases:** Connect to your MySQL database, query it using natural language, and receive responses in human-readable format.

![Screenshot (579)](https://github.com/user-attachments/assets/4f643056-25a0-4c22-8e3d-377e363121c2)

* **Responsive Design:** Optimized for all devices (mobile, tablet, desktop).
* **Light/Dark Mode:** User interface available in both light and dark themes.
* **AI-Driven Responses:** Uses Groq Llama and Gemini models for AI-based query processing.

![Screenshot (577)](https://github.com/user-attachments/assets/d877e216-3272-4995-9b54-d52ff6c61d86)

* **Contextual Chat:** Maintains chat history to provide continuous, context-aware conversation.

## Tech Stacks
### Frontend
* Next.js (v14)
* Tailwind CSS
* TypeScript
* ShadCN UI

### Backend
* Python
* FastAPI
* Langchain
* FAISS Index (Vector Database)
* Gemini API
* Groq Llama Model

## Project Architecture
### Chat with MySQL Databases
1. **User Database Input:** The user enters database credentials (hostname, username, password) and database name on the frontend.
2. **Connection Establishment:** The credentials are sent to a FastAPI endpoint, which establishes a connection to the MySQL database.
3. **Schema Extraction:** Upon successful connection, the schema of the database is extracted.
4. **Natural Language Query:** The user inputs a query in natural language on the frontend, which is sent to the backend.
5. **Query Generation:** The natural language query is passed to the Gemini model, along with the database schema, to generate a MySQL query.
6. **Query Execution:** The generated query is executed on the database.
7. **Result Translation:** The query results are sent to the Gemini model, which converts them back to natural language.
8. **Response:** The natural language response is sent to the frontend and displayed to the user.
9. **Contextual Chat:** The chat history is maintained and fed into the model to ensure that the conversation retains context over time.

### Chat with PDF Files
1. **PDF Upload:** The user uploads a PDF file, which is sent to a FastAPI endpoint.
2. **Text Extraction:** The PDF is processed, and the text is extracted.
3. **Chunking:** The extracted text is broken into manageable chunks and stored in a vector database (FAISS).
4. **User Query:** The user enters a query on the frontend, which is sent to the backend.
5. **Context Retrieval:** The query is used to perform a cosine similarity search on the vector database to extract relevant chunks of the document.
6. **AI Response:** The user query and document context are passed to the Groq Llama model, which generates a response.
7. **Response Delivery:** The AI-generated response is sent back to the frontend and displayed to the user.

## Future Scope
* **Data Persistence:** Implement the functionality to upload all necessary data (such as chat history and extracted PDF data) into a database for long-term storage.
* **Cloud Vector Database:** Add support for a cloud-based vector database to store the document embeddings and facilitate more scalable and efficient querying.
* **Website Deployment:** Deploy the website on a cloud platform like AWS, Google Cloud, or Vercel to make it publicly accessible.
* **Multiple Document Chat:** Enhance the platform to allow users to upload and query multiple documents at once, improving the versatility of the tool.

## Local Setup
### Prerequisites
* Node.js (for frontend)
* Python 3.8+ (for backend)
* MySQL (for database chat functionality)

### Environment Variables
You will need to configure the following environment variables in your `.env` file:
```bash
# Backend
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_llama_api_key
```

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/TechBot505/doom-ai
   ```
2. Navigate to the backend directory:
   ```bash
   cd backend
   ```
3. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Unix-based systems
   venv\Scripts\activate  # For Windows
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Navigate into api directory:
   ```bash
   cd api
   ```
6. Run the FastAPI backend server:
   ```bash
   uvicorn main:app --reload
   ```
7. Open the fastapi routes on localhost 8000:
   ```bash
   http://localhost:8000/docs
   ```

### Frontend Setup
1. In a new terminal, navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install the required dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
4. Open the development server in a browser:
   ```bash
   http://localhost:3000/
   ```

## Contributing
We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Open a pull request.




