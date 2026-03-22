#use official python image
FROM python:3.9-slim
#CREATE NON ROOT USER
RUN useradd -M appuser

# set work directory
WORKDIR /app

#COPY Files
COPY ./app

#INSTALL DEPENDENCIES
RUN pip install -no-cache-dir flask

swithc user
USER appuser

#expose port
EXPOSE 5000

#RUN THE APPLICATION
CMD ["python","app.py"]