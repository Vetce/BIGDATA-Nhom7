FROM node:18-alpine

# Install dependencies
WORKDIR /app

# Copy package files
COPY package*.json ./
COPY server/package*.json ./server/

# Install dependencies
RUN npm install
RUN cd server && npm install && cd ..

# Copy application code
COPY . .

# Expose ports
EXPOSE 3000 5000

# Start both server and client
CMD ["npm", "run", "dev"]
