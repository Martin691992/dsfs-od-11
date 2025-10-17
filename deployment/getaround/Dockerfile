FROM node:22.14.0

WORKDIR /getaround

COPY . .

RUN npm ci --omit dev

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv
RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN apt-get install python3-pandas -y
# RUN apt-get install python3-openpyxl -y
# RUN apt-get install python3-joblib -y
# RUN apt-get install python3-sklearn -y
# RUN apt-get install python3-numpy -y

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" PIP_NO_CACHE_DIR=1
RUN pip install -r requirements.txt

EXPOSE 8050

CMD ["node", "build"]


