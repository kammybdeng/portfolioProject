FROM python:3.8.3-slim-buster

COPY . .

ENV API_KEY=${API_KEY}
ENV BASE_URL=${BASE_URL}

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD [ "python", "myPortfolio/stats.py"]



# TO-Do: replace with this step
# docker build -t myportfolio/test .
# docker run -e API_KEY -e BASE_URL myportfolio/test

# TO-DO: replace this step 
# file created inside container, spreadsheet and log
# to copy back to host use following command
# docker cp {container_id}:/myFiles/{filename} myFiles/