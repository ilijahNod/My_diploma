FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /MyCourseProject
COPY requirements.txt /MyCourseProject/
RUN pip install -r requirements.txt
COPY . /MyCourseProject/
