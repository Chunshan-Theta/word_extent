#FROM python:3.7.3-alpine
FROM  python:3.7
EXPOSE 8000


WORKDIR /app
ADD ./manage.py /app

#Using pip:
#RUN python -m pip install -r requirements.txt
#RUN apt-get update

#CMD /bin/bash
CMD python manage.py runserver 0.0.0.0:8000 --noreload
