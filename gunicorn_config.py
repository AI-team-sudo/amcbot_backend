"""Gunicorn config file"""

# Core Settings
bind = "0.0.0.0:10000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
keepalive = 120

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process Naming
proc_name = "AMC_Chatbot_API"

# SSL (if needed)
# keyfile = "/etc/ssl/private/key.pem"
# certfile = "/etc/ssl/certs/cert.pem"
