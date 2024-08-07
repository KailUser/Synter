# Synter | Lyntr Bot  

## Introduction to Synter

Synter is a Python-based automation tool designed to assist with creating and posting content on Lyntr, a popular social media platform. By leveraging the power of Selenium, Synter allows you to automate the process of posting on Lyntr, freeing up your time and ensuring that your posts are made accurately and consistently.

## Installation Guide

To get started with Synter, you'll first need to install the necessary dependencies. The primary requirement for running Synter is Selenium, a powerful web automation tool.

### Step 1: Installing Selenium

Selenium can be easily installed using pip, the Python package installer. Open your terminal or command prompt and execute the following command:

```pypi
pip install selenium
```

This command will download and install the Selenium library, along with its dependencies. Once the installation is complete, you're ready to move on to the next step.

### Step 2: Running the Synter Script

After you've installed Selenium, the next step is to run the main Python file that contains the Synter script. Before you do this, make sure you've configured the script with your personal Lyntr token. This token is necessary for authenticating the bot and allowing it to post on your behalf.

Open the `main.py` file in your preferred text editor, and locate the following lines:

```python
if __name__ == "__main__":
    bot = LyntrBot(token="INSERT YOUR TOKEN HERE") # Replace "INSERT YOUR TOKEN HERE" with your actual token
    bot.send_post("Hello, Lynter!") # Customize this line with your desired post content
```

To run the script, use the following command:

```python
python3 main.py
```

When you execute this command, a new Chrome window will open, controlled by the bot script. The bot will log in to your Lyntr account and post the content you've specified.

## Obtaining Your Lyntr Token

To use Synter effectively, you need to obtain your Lyntr token. This token is used to authenticate your account and grant the bot access to post on your behalf.

### Step 1: Open Lyntr in Chrome

First, navigate to [Lyntr](https://lyntr.com/) using Google Chrome.

### Step 2: Access the Developer Tools

Once you're on the Lyntr homepage, open Chrome's Developer Tools. You can do this by pressing `Ctrl + Shift + I` (on Windows/Linux) or `Cmd + Option + I` (on macOS). Alternatively, you can right-click on the page and select "Inspect."

### Step 3: Find Your Token

With the Developer Tools open, switch to the "Network" tab. From here, you'll need to filter the requests by searching for the URL `https://lyntr.com/api/me`. Once you find the request, click on it, and look for your token in the response. It will usually be labeled as `_TOKEN__DO_NOT_SHARE` or something similar.

### Step 4: Copy and Paste Your Token

Copy the token value and paste it into line 80 of the `main.py` file, as mentioned earlier. Make sure to save your changes before running the script.

## Usage Instructions

After setting up the token and customizing your post content, you're ready to use Synter. Simply run the script, and the bot will automatically handle the rest. This includes logging in to your Lyntr account, navigating to the appropriate section, and posting your content.

The bot operates entirely within a Chrome window, so you'll be able to see it in action. This transparency allows you to monitor the bot's activities and ensure everything is running smoothly.

## Additional Customization

Synter is a flexible tool, and with some Python knowledge, you can further customize the script to suit your needs. Whether you want to schedule posts, add more complex interactions, or expand its functionality, the script is open for modification.

## Acknowledgments

- **[FaceDev](https://github.com/face-hh)** for creating Lyntr, the platform that inspired the creation of Synter.
- **[Syirezz](https://github.com/KaliUser)** for developing the Synter bot and making it available to the community.

Happy posting!