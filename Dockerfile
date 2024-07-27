FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y dos2unix
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh
RUN dos2unix entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["sh", "-c", "python electronics_retailer/manage.py runserver 0.0.0.0:8000"]