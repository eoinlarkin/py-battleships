# Stage 1: Build the Mamba environment
FROM mambaorg/micromamba:2.0.5

# Set the working directory
WORKDIR /app

# Copy the environment.yml file
COPY environment.yml .

# Create the Mamba environment
RUN micromamba create -n myenv -f environment.yml --yes && \
    micromamba clean --all --yes

# Ensure the environment is activated when using RUN
ENV MAMBA_DOCKERFILE_ACTIVATE=1

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Ensure correct permissions for package-lock.json
USER root

# Install npm dependencies inside the activated environment
RUN micromamba run -n myenv npm install

# Copy the rest of your application code
COPY assets/ ./assets/
COPY battleships/ ./battleships/
COPY controllers/ ./controllers/
COPY views/ ./views/
COPY index.js ./
COPY run.py ./

# Expose the port your game runs on (if applicable)
EXPOSE 8000

# Command to run your game
CMD ["micromamba", "run", "-n", "myenv", "node", "index.js"]