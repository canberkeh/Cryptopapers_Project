FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# entry.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh