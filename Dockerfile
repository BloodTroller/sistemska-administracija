FROM python:3.12
LABEL school_subject=["sistemska-administracija","racunalniski-vid"]
LABEL by="bloodtroller"
WORKDIR /code
COPY . .
RUN pip install -r req.txt
CMD ["python", "main.py"]