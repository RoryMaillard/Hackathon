FROM python:3.9
# Or any preferred Python version.
WORKDIR /src
COPY . /src

RUN python -m pip install -r requirements.txt

EXPOSE 5000
#RUN pip install requests beautifulsoup4 python-dotenv
CMD ["python", "./src/parkings.py"]
# Or enter the name of your unique directory and parameter set.
