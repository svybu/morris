FROM  python:3.10.7-slim-bullseye
EXPOSE 3000
COPY requirements.txt .
RUN pip install -r /requirements.txt 
RUN pip install gunicorn
WORKDIR /api
COPY Data ./Data
COPY API_start.py .
COPY wsgi.py .
COPY determinate_gender.py .
COPY Cache ./Cache
#ENTRYPOINT ["python", "API_start.py"] 
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "API_start:app"]