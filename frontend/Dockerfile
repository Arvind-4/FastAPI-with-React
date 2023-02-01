FROM node:alpine as build

WORKDIR /app/frontend

COPY ./frontend /app/frontend

RUN yarn

RUN yarn build

FROM nginx:latest

COPY --from=build /app/frontend/build /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]