FROM python:3.7

WORKDIR /pricehunt/

COPY ./ ./ 

RUN  pip install -r requirements.txt

CMD python -u multi.py
