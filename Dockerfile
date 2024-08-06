# Use a base image compatible with Raspberry Pi (ARM architecture)
FROM python:3.9-slim-buster

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# Set the working directory in the container
WORKDIR /usr/src/ArchPokemon

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the entry point script into the container
COPY entrypoint.sh /usr/src/ArchPokemon/entrypoint.sh

# Make the entry point script executable
RUN chmod +x /usr/src/ArchPokemon/entrypoint.sh

# Set the entry point to run the entry point script
ENTRYPOINT ["/usr/src/ArchPokemon/entrypoint.sh"]