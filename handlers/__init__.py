from .start import router as start_router
from .help import router as help_router
from .profile import router as profile_router
from .chat import router as chat_router
from .payments import router as payments_router
from .admin import router as admin_router

__all__ = [
    "start_router",
    "help_router",
    "profile_router",
    "chat_router",
    "payments_router",
    "admin_router",
]