FROM node:20.9.0
WORKDIR /app
COPY front/. .
RUN npm install
RUN npm run build
ENV PORT=3000
EXPOSE $PORT
CMD ["npm", "run", "serve", "--", "--host", "0.0.0.0","--port","3000"]
