FROM node:22.14.0

WORKDIR /getaround

COPY . .

RUN npm ci --omit dev

RUN apt-get update && apt-get install -y python3 python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install python3-pandas -y
RUN apt-get install python3-openpyxl -y
RUN apt-get install python3-joblib -y

EXPOSE 8000

CMD ["node", "build"]


