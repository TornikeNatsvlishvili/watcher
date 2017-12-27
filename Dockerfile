FROM python:3.6

COPY requirements/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /watcher
COPY run.py run.py
WORKDIR /watcher


ENTRYPOINT ["python"]
CMD ["run.py"]