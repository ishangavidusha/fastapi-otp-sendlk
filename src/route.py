from fastapi import APIRouter
from src.controller import send_verify_code, validate_code
from src.schema import PhoneNumber, ValidateCode, Token, Message

router = APIRouter(prefix="/code")

@router.post("/send", response_model=Token)
def send_verify_code_handler(phone_number: PhoneNumber):
    token = send_verify_code(phone_number.phone_number)
    return Token(token=token)

@router.post("/validate", response_model=Message)
def validate_code_handler(validate: ValidateCode):
    message = validate_code(validate.token, validate.code)
    return Message(message=message)