FROM python:3

RUN mkdir /code
WORKDIR /code

ADD requirements.txt ./
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

ADD . ./

ENTRYPOINT ["python", "create-blueprint.py"]