#!/bin/bash

error_exit() {
    echo "$1" 1>&2
    exit 1
}

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    error_exit "pip could not be found. Please install pip first."
fi

# Check if Selenium is already installed
if pip show selenium &> /dev/null
then
    echo "Selenium is already installed."
fi

echo "Installing Selenium..."
if pip install selenium
then
    echo "Selenium installed successfully."
else
    error_exit "There was an issue installing Selenium. Check the traceback above for details."
fi

CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.72/linux64/chromedriver-linux64.zip"
DESTINATION_DIR="$HOME/Desktop"

TEMP_DIR=$(mktemp -d)

if ! command -v curl &> /dev/null
then
    error_exit "curl could not be found. Please install curl first."
fi

if ! command -v unzip &> /dev/null
then
    error_exit "unzip could not be found. Please install unzip first."
fi

echo "Downloading ChromeDriver..."
if curl -L "$CHROMEDRIVER_URL" -o "$TEMP_DIR/chromedriver.zip"
then
    echo "Download complete."
else
    error_exit "Failed to download ChromeDriver."
fi

echo "Unzipping ChromeDriver..."
if unzip "$TEMP_DIR/chromedriver.zip" -d "$TEMP_DIR"
then
    echo "Unzipping complete."
else
    error_exit "Failed to unzip ChromeDriver."
fi

if mv "$TEMP_DIR/chromedriver-linux64/chromedriver" "$DESTINATION_DIR"
then
    echo "ChromeDriver moved to $DESTINATION_DIR."
else
    error_exit "Failed to move ChromeDriver to $DESTINATION_DIR."
fi

rm -rf "$TEMP_DIR"

echo "ChromeDriver installation completed successfully."

# URL of the latest Google Chrome for Linux

DESTINATION_DIR="/opt/google/chrome"

TEMP_DIR=$(mktemp -d)

# Ask the user if they have Google Chrome installed
read -p "Do you already have Google Chrome installed? (Y/N): " has_chrome

if [[ "$has_chrome" =~ ^[Yy]$ ]]
then
    echo "You already have Google Chrome installed. Exiting the script."
    exit 0
fi

echo "Downloading Google Chrome..."
if wget -q -O google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
then
    echo "Download complete."
else
    error_exit "Failed to download Google Chrome."
fi
echo "Following requires your sudo password"
sudo dpkg -i google-chrome-stable_current_amd64.deb

echo "Google Chrome installation completed successfully."
