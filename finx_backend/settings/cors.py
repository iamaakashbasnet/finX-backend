from finx_backend.env import env

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False

BASE_BACKEND_URL = env.str("DJANGO_BASE_BACKEND_URL", default="http://localhost:8000")
BASE_FRONTEND_URL = env.str("DJANGO_BASE_FRONTEND_URL", default="http://localhost:3000")

# Use regex to allow localhost with subdomains (for development)
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://(\w+\.)?localhost:3000$",  # Matches localhost:3000 and subdomains
]

# Use whitelist for specific origins (production)
CORS_ORIGIN_WHITELIST = env.list(
    "DJANGO_CORS_ORIGIN_WHITELIST",
    default=[BASE_FRONTEND_URL]
)
