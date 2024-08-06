#!/bin/bash

# Pull the latest changes from the repository
git pull origin main

# Start the application
exec python main.py