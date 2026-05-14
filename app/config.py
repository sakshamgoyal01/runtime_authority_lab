import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Runtime Authority Lab"

    # Intentionally insecure fallback
    JWT_SECRET = os.getenv("JWT_SECRET", "fallback-dev-secret")

    ADMIN_API_KEY = os.getenv(
        "ADMIN_API_KEY",
        "fallback-admin-key"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )

settings = Settings()