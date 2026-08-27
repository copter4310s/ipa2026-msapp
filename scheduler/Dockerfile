FROM python
WORKDIR /home/myapp
COPY ./database.py /home/myapp/
COPY ./scheduler.py /home/myapp/
COPY ./producer.py /home/myapp/
COPY ./requirement.txt /home/myapp/
RUN pip install -r /home/myapp/requirement.txt
CMD ["python", "/home/myapp/scheduler.py"]
