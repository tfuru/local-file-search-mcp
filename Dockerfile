FROM python:3.12.11

WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# EXPOSE 8000
WORKDIR /app

# fastmcp run server.py --transport sse
CMD ["fastmcp", "run", "server.py", "--transport", "sse"]
