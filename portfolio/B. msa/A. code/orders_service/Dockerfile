FROM node:18

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

RUN npm install mysql cookie-parser body-parser express-session session-file-s
tore method-override jsonwebtoken express ejs

COPY devops_msa_orders/. .

EXPOSE 3003

CMD [ "node", "index.js" ]
