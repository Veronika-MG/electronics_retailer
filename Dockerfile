FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]

CMD ["sh", "-c", "python electronics_retailer/manage.py runserver 0.0.0.0:8000"]