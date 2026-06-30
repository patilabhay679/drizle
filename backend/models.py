from pydantic import BaseModel, EmailStr, Field
from typing import Any


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


# ─── Onboarding Models ───

class OnboardingBusinessType(BaseModel):
    type: str = Field(default="", max_length=50)
    subtype: str = Field(default="", max_length=100)


class OnboardingBusinessDetails(BaseModel):
    legal_name: str = Field(default="", max_length=200)
    trading_name: str = Field(default="", max_length=200)
    registration_number: str = Field(default="", max_length=20)
    tax_id: str = Field(default="", max_length=20)
    emirates_id: str = Field(default="", max_length=20)
    website: str = Field(default="", max_length=200)
    phone: str = Field(default="", max_length=20)
    address: str = Field(default="", max_length=300)
    city: str = Field(default="", max_length=100)
    country: str = Field(default="UAE", max_length=100)


class OnboardingRepresentative(BaseModel):
    name: str = Field(default="", max_length=100)
    email: str = Field(default="", max_length=200)
    phone: str = Field(default="", max_length=20)
    job_title: str = Field(default="", max_length=100)


class OnboardingOwner(BaseModel):
    name: str = Field(default="", max_length=100)
    email: str = Field(default="", max_length=200)
    phone: str = Field(default="", max_length=20)
    nationality: str = Field(default="", max_length=100)
    ownership_pct: float = Field(default=0, ge=0, le=100)


class OnboardingExecutive(BaseModel):
    name: str = Field(default="", max_length=100)
    email: str = Field(default="", max_length=200)
    job_title: str = Field(default="", max_length=100)
    nationality: str = Field(default="", max_length=100)


class OnboardingProducts(BaseModel):
    description: str = Field(default="", max_length=500)
    industry: str = Field(default="", max_length=100)
    avg_ticket_size: float = Field(default=0, ge=0)
    expected_monthly_volume: int = Field(default=0, ge=0)
    target_markets: list[str] = Field(default_factory=list)


class OnboardingPublic(BaseModel):
    public_name: str = Field(default="", max_length=200)
    support_email: str = Field(default="", max_length=200)
    support_phone: str = Field(default="", max_length=20)
    support_url: str = Field(default="", max_length=200)
    terms_url: str = Field(default="", max_length=200)
    privacy_url: str = Field(default="", max_length=200)


class OnboardingBank(BaseModel):
    bank_name: str = Field(default="", max_length=100)
    account_name: str = Field(default="", max_length=200)
    account_number: str = Field(default="", max_length=20)
    iban: str = Field(default="", max_length=30)
    swift: str = Field(default="", max_length=15)


class OnboardingSecurity(BaseModel):
    two_factor_enabled: bool = False


class OnboardingExtras(BaseModel):
    referral_source: str = Field(default="", max_length=200)
    notes: str = Field(default="", max_length=1000)


class OnboardingData(BaseModel):
    business_type: OnboardingBusinessType = Field(default_factory=OnboardingBusinessType)
    business_details: OnboardingBusinessDetails = Field(default_factory=OnboardingBusinessDetails)
    representative: OnboardingRepresentative = Field(default_factory=OnboardingRepresentative)
    owners: list[OnboardingOwner] = Field(default_factory=list)
    executives: list[OnboardingExecutive] = Field(default_factory=list)
    products: OnboardingProducts = Field(default_factory=OnboardingProducts)
    public: OnboardingPublic = Field(default_factory=OnboardingPublic)
    bank: OnboardingBank = Field(default_factory=OnboardingBank)
    security: OnboardingSecurity = Field(default_factory=OnboardingSecurity)
    extras: OnboardingExtras = Field(default_factory=OnboardingExtras)


class OnboardingSaveModel(BaseModel):
    section: str
    data: Any


class OnboardingSubmitModel(BaseModel):
    pass
