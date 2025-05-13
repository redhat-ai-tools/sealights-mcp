FROM registry.redhat.io/ubi9/python-311

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY sealights_mcp_server.py ./

CMD ["python", "sealights_mcp_server.py"] 