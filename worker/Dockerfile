FROM python
WORKDIR /home/myapp
COPY ./database.py /home/myapp/
COPY ./worker.py /home/myapp/
COPY ./get_interfaces.py /home/myapp/
COPY ./requirement.txt /home/myapp/
RUN pip install -r /home/myapp/requirement.txt
CMD ["python", "/home/myapp/worker.py"]
