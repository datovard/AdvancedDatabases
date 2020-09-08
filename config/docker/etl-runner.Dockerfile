FROM python:3

WORKDIR /usr/src

COPY /usr/src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /usr/src/ .

RUN ls

# CMD [ "python", "./your-daemon-or-script.py" ]