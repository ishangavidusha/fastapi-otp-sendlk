from pydantic import BaseModel

class Token(BaseModel):
    token: str
    
class PhoneNumber(BaseModel):
    phone_number: str
    
class ValidateCode(Token):
    code: str
    
class Message(BaseModel):
    message: str