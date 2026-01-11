# Use official Node LTS
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install only production dependencies (express)
RUN npm install --production

# Copy the static HTML dashboard files
COPY index.html ./
COPY Overview ./Overview/
COPY Connectors ./Connectors/
COPY DashboardAttribution ./DashboardAttribution/
COPY DashboardPaid ./DashboardPaid/
COPY DashboardPaidCampaigns ./DashboardPaidCampaigns/
COPY AnaluseCampaign ./AnaluseCampaign/

# Copy server file
COPY server.js ./

# Create dist directory and copy files (server expects them in dist/)
RUN mkdir -p dist && \
    cp index.html dist/ && \
    cp -r Overview dist/ && \
    cp -r Connectors dist/ && \
    cp -r DashboardAttribution dist/ && \
    cp -r DashboardPaid dist/ && \
    cp -r DashboardPaidCampaigns dist/ && \
    cp -r AnaluseCampaign dist/

# Cloud Run listens on 8080
EXPOSE 8080

# Start the server
CMD ["npm", "start"]
