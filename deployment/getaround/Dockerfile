FROM node:22.14.0

WORKDIR /simulation.bonnardconsulting

COPY . .

RUN npm ci --omit dev

RUN apt-get update && apt-get install -y python3 python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install python3-pandas -y
RUN apt-get install python3-openpyxl -y

EXPOSE 8001

CMD ["node", "build"]


