#use official python image
FROM python:3.9-slim
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
#CREATE NON ROOT USER
RUN useradd -M appuser

# set work directory
WORKDIR /app

#COPY Files
COPY . .

#INSTALL DEPENDENCIES
RUN pip install --no-cache-dir flask

#swithc user
USER appuser

#expose port
EXPOSE 5000

#RUN THE APPLICATION
CMD ["python","app.py"]
