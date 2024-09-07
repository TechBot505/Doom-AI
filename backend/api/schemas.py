from pydantic import BaseModel

class dbModel(BaseModel):
    user: str
    password: str
    host: str
    port: str
    database: str
    
class ChatRequest(BaseModel):
    user_query: str
    
# {
#   "user": "root",
#   "password": "rohit",
#   "host": "localhost",
#   "port": "3306",
#   "database": "retail_sales_db"
# }