FROM python:3.12

WORKDIR /app

COPY . .

CMD ["python", "inventorypart2.py"]

