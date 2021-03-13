FROM jordanirabor/python3.7-pip-pipenv

COPY . /activityApi

WORKDIR /activityApi
RUN pipenv install
RUN chmod +x entrypoint.sh
