# Use official Node LTS
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies
RUN npm install --production=false

# Copy rest of the source
COPY . .

# Build the Vite app
RUN npm run build

# Cloud Run listens on 8080
EXPOSE 8080

# Start the server
CMD ["npm", "start"]
