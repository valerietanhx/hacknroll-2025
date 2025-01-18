FROM node:alpine AS development

ENV NODE_ENV development

WORKDIR /frontend

COPY . .
RUN npm install

EXPOSE ${FRONTEND_CONTAINER_PORT}

CMD ["npm","run","dev"]
