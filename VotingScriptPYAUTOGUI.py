import pygetwindow as gw
import pyautogui
from pywinauto import Application
from pywinauto import Desktop

import win32gui
import win32con

import subprocess
import time
from flask import Flask, request
import threading


app = Flask(__name__)

# List of URLs to open
urls = [
    # Add your URLs here
]

# Dictionary to track the status of each URL
url_status = {url: 'pending' for url in urls}

# Define a timeout (in seconds)
timeout = 60

# Function to open a URL in Chrome
def open_url(url):
    chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    command = [chrome_path, '--start-maximized', url]
    subprocess.Popen(command)

# Function to check if all URLs are complete
def all_urls_complete():
    return all(status == 'complete' for status in url_status.values())

# Endpoint to receive status updates from Tampermonkey scripts
@app.route('/status', methods=['POST'])
def receive_status():
    url = request.json['url']
    status = request.json['status']
    url_status[url] = status
    return 'Status received'

def process_urls():
    for url in urls:
        open_url(url)

        # Wait for the URL to complete or timeout
        start_time = time.time()
        while url_status[url] == 'pending':
            if time.time() - start_time > timeout:
                break
            time.sleep(1)

        if url_status[url] == 'complete':
            print(f'{url} is complete.')
        else:
            print(f'{url} timed out.')

        # If all URLs are complete, exit the loop
        if all_urls_complete():
            break

if __name__ == '__main__':
    t = threading.Thread(target=app.run, kwargs={'port': 5000})
    t.start()
    process_urls()
    
# Optionally, you can handle the URLs that timed out and retry them.

'''
# Path to the Google Chrome executable
chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# URL to open
url = 'https://topminecraftservers.org/vote/11365'

# Open Google Chrome and navigate to the URL
command = [chrome_path, '--start-maximized', url]
subprocess.Popen(command)


url= 'https://minecraft-mp.com/server/252430/vote/'
command = [chrome_path, '--start-maximized', url]
subprocess.Popen(command)

'''





#https://topminecraftservers.org/vote/11365

#https://minecraft-mp.com/server/252430/vote/

#https://minecraft.buzz/vote/6219

#https://topg.org/minecraft-servers/server-601275    -12 hour

#https://minecraft-server.net/vote/minemalia/

#https://www.minecraft-serverlist.net/vote/54222

#https://minecraftbestservers.com/server-minemalia.957/vote