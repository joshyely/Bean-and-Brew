FROM node:latest as build

RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install
ENV VITE_API_URL=$VITE_API_URL
COPY . .
RUN npm run build

FROM nginx as production
RUN mkdir /app
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]