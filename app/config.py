from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Environment
    environment: str = "development"
    debug: bool = True
    
    # Database
    database_url: str = "sqlite:///./o2c_billing.db"
    
    # SAP Integration
    sap_api_base_url: str = "https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap"
    sap_api_key: str = "7NIOHGBmJSnemCSSAKsf9FgBWGAUCwxO"
    sap_timeout: int = 30
    sap_retries: int = 3
    
    # Application
    app_title: str = "O2C Billing Portal"
    app_version: str = "1.0.0"
    
    # Security (placeholder)
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Features
    enable_mock_data: bool = True
    enable_debug_mode: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()