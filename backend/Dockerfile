FROM python:3.13.4-slim-bullseye

# create python virtual environment
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY backend/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY backend/src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]