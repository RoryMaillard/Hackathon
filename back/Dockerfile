FROM python:3.11
WORKDIR /app
COPY back/. back/.
ENV API_KEY=${API_KEY}
RUN pip install --no-cache-dir -r back/requirements.txt
CMD ["gunicorn", "-b" ,"0.0.0.0:5000" ,"back.src.main:app"]
EXPOSE 5000
