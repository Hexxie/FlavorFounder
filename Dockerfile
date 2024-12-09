# Use an official Node.js image as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the working directory
COPY js/flavor-founder/package.json js/flavor-founder/package-lock.json ./

# Install dependencies using npm
RUN npm install

# Copy the rest of the application files into the working directory
COPY js/flavor-founder/ ./

# Expose the port the app runs on
EXPOSE 3000

# Start the app
CMD ["npm", "run", "dev"]
