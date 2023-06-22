FROM node:alpine
WORKDIR /app

COPY ./src/react/frontend/package.json /app/
COPY ./src/react/frontend/package-lock.json /app/

RUN npm i

COPY ./src/react/frontend/public /app/public
COPY ./src/react/frontend/src /app/src

CMD ["npm", "run", "start"]