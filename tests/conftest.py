import os

# pytest-localftpserver
os.environ["FTP_USER"] = "user"
os.environ["FTP_PASS"] = "pass"
os.environ["FTP_HOME"] = os.path.join(os.path.dirname(__file__), "..", "var")
os.environ["FTP_PORT"] = "31175"
