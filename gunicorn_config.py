# Import required modules
import os
import multiprocessing

# Binding
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Worker Settings
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120
keepalive = 120

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process Naming
proc_name = "AMC_Chatbot_API"

# SSL (if needed)
# keyfile = "/path/to/keyfile"
# certfile = "/path/to/certfile"

# Server Mechanics
preload_app = True
reload = False  # Set to True for development

# Debugging
capture_output = True
enable_stdio_inheritance = True
