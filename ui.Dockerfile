FROM node:latest AS build
WORKDIR /app
COPY package.json yarn.lock /app/
RUN yarn install
COPY public /app/public
COPY src /app/src
RUN npm run build

FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/build/ /usr/share/nginx/html/
