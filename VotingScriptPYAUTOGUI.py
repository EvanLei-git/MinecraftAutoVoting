from flask import Flask, request
import threading
import subprocess
import time
import webbrowser
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# Dictionary to track the status of each URL
url_status = {}

# List of URLs to open
urls = [
  # Type your targeted sites
]

# Define a timeout (in seconds)
timeout = 60

# Function to open a URL in Chrome
def open_url(url):
    time.sleep(2)

    chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    command = [chrome_path, '--start-maximized', url]
    subprocess.Popen(command)

# Function to close the Chrome browser window
def close_chrome():
    time.sleep(2)
    subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# Function to check if all URLs are complete
def all_urls_complete():
    return all(status == 'completed' for status in url_status.values())


# Endpoint to receive status updates from Tampermonkey scripts
@app.route('/status', methods=['POST', 'OPTIONS'])
def receive_status():
    if request.method == 'OPTIONS':
        # Respond to preflight request
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return ('', 200, response_headers)
    elif request.method == 'POST':
        received_url = request.json.get('url')
        status = request.json.get('status')

        if received_url and status:
            # Extract the parent URL (domain) from the received URL
            received_parent_url = urlparse(received_url).scheme + "://" + urlparse(received_url).hostname

            # Iterate through the URLs in your list to find a match
            for url in urls:
                # Extract the parent URL (domain) from the URL in the list
                url_parent_url = urlparse(url).scheme + "://" + urlparse(url).hostname

                # Compare the parent URLs
                if received_parent_url == url_parent_url:
                    url_status[url] = status
                    print (url_status)
                    print(f'Received status update for URL: {received_url}, Status: {status}')
                    print(f'Matched with URL in the list: {url}')
                    break  # Break out of the loop once a match is found

            # Respond to the actual POST request
            response_headers = {
                'Access-Control-Allow-Origin': '*',
            }
            return ('Status received', 200, response_headers)
        else:
            return 'Invalid data received', 400

# Function to process URLs
def process_urls():
    global url_status
    # Define the url_status dictionary
    url_status = {url: 'pending' for url in urls}

    # Keep track of URLs that need to be retried
    retry_urls = []

    for url in urls:
        close_chrome()
        # Open the URL in a browser using the subprocess module
        open_url(url)

        # Wait for the URL to complete or timeout
        start_time = time.time()
        while url_status.get(url) == 'pending':

            if time.time() - start_time > timeout:
                break
            time.sleep(1)

        if url_status.get(url) == 'completed':
            print(f'{url} is complete.')
        else:
            print(f'{url} timed out.')
            # Add the URL to the retry list
            retry_urls.append(url)

    # Close the Chrome browser window after processing all URLs


    # Retry the URLs that didn't complete at the end of the queue
    for retry_url in retry_urls:
        open_url(retry_url)
        # Wait for the URL to complete or timeout
        start_time = time.time()
        while url_status.get(retry_url) == 'pending':
            if time.time() - start_time > timeout:
                break
            time.sleep(1)

        if url_status.get(retry_url) == 'completed':
            print(f'{retry_url} is complete after retry.')
        else:
            print(f'{retry_url} timed out after retry. Moving to the next URL.')


if __name__ == '__main__':
    # Run the Flask server in a separate thread
    t = threading.Thread(target=app.run, kwargs={'port': 5000})
    t.start()

    # Process URLs
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
