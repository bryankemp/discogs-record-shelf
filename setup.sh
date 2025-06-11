#!/bin/bash

# Discogs Report Tool Setup Script

echo "Setting up Discogs Custom Reports Tool..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env file and add your Discogs API token"
fi

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get your Discogs API token from: https://www.discogs.com/settings/developers"
echo "2. Edit the .env file and add your token"
echo "3. Test the tool: python main.py list-shelves --username YOUR_USERNAME"
echo ""
echo "For usage examples, see README.md"

