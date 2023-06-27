FROM node:alpine
WORKDIR /app

COPY ./src/react/frontend/package-lock.json .
COPY ./src/react/frontend/package.json .

RUN npm i

COPY ./src/react/frontend/public ./public
COPY ./src/react/frontend/src ./src

CMD ["npm", "run", "start"]