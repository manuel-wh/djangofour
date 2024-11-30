try:
    # Try import settings_server.py for local purpose.
    from settings_server import *
except ImportError:
    # Doesn't matter if settings_server.py not exist.
    pass
