from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    name: str = Field(min_length=1, max_length=100)
    company: str | None = None


class LoginModel(BaseModel):
    email: str
    password: str


class UpdateProfileModel(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    company: str | None = None


class ChangePasswordModel(BaseModel):
    current_password: str
    new_password: str = Field(min_length=6)


class ForgotPasswordModel(BaseModel):
    email: EmailStr


class ResetPasswordModel(BaseModel):
    token: str
    new_password: str = Field(min_length=6)


class ContactModel(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    email: EmailStr
    company: str | None = None
    phone: str | None = None
    message: str = Field(min_length=1, max_length=5000)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    merchant: dict


class CreatePayLinkModel(BaseModel):
    amount: float | None = Field(None, ge=0)
    currency: str = "AED"
    description: str | None = Field(None, max_length=500)
    is_static: bool = False
    is_recurring: bool = False
    recurring_interval: str | None = None


class InviteUserModel(BaseModel):
    email: EmailStr
    role: str = "member"


class SupportTicketModel(BaseModel):
    subject: str = Field(min_length=1, max_length=200)
    category: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=5000)
    priority: str = "normal"


class PublicSupportTicketModel(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    email: EmailStr
    subject: str = Field(min_length=1, max_length=200)
    category: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=5000)
