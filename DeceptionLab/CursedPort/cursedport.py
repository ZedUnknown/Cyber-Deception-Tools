import os
import sys
import time
import string
import random
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = ""  # The host address where the server will run
PORT = 8000  # The port number on which the server will listen

URLs_PER_GENERATE = (7, 12)  # The range of how many URLs to generate per page [Default=(7, 12)]
LENGTH_OF_URL = (20, 32)  # The range of the length of each generated URL [Default=(20, 32)]
TIMEOUT = 350  # The delay (in milliseconds) between receiving a request and serving a response [Default=350]

ENABLE_UPPER_CASE = True  # Enable or disable uppercase letters in generated URLs
ENABLE_LOWER_CASE = True  # Enable or disable lowercase letters in generated URLs
ENABLE_DIGITS = True  # Enable or disable digits (numbers) in generated URLs
ENABLE_PUNCTUATIONS = True  # Enable or disable punctuation characters in generated URLs

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CursedPort</title>
    <style>
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #ff2c2c;
            padding: 20px;
            bottom: 50;
            text-align: center;
        }
        h1 {
            font-size: 36px;
            margin: 0;
        }
        main {
            padding: 20px;
            text-align: center;
        }
        a {
            color: #0051ff;
            text-decoration: none;
            font-size: 20;
            transition: color 0.3s ease;
        }
        a:hover {
            color: #0038b0;
        }
    </style>
</head>
<body>
    <header>
        <h1>CursedPort</h1>
    </header>
    <main>
        URL_PLACEHOLDER
    </main>
</body>
</html>
"""  # Define the HTML content with a placeholder for the URLs

class RequestHandlerAPI(BaseHTTPRequestHandler):
    websites = None
    
    def generate(self, seed):
        random.seed(seed)
        html = HTML
        num_links = random.randint(URLs_PER_GENERATE[0], URLs_PER_GENERATE[1])
        
        urls = []
        choices = []
        if self.websites is None:
            if ENABLE_UPPER_CASE:
                choices.extend(string.ascii_uppercase)
            if ENABLE_LOWER_CASE:
                choices.extend(string.ascii_lowercase)
            if ENABLE_DIGITS:
                choices.extend(string.digits)
            if ENABLE_PUNCTUATIONS:
                choices.extend("_-")
                
            for i in range(num_links):
                url = ''.join(random.choice(choices) for i in range(random.randint(LENGTH_OF_URL[0], LENGTH_OF_URL[1])))
                urls.append(url)
            
        else:
            for i in range(num_links):
                url = ''.join(random.choice(self.websites))
                urls.append(url)
            
        page = html.replace("URL_PLACEHOLDER", ''.join(f"\n<a href={url}>https://{url}</a><br>" for url in urls))
        return page
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        
    def do_GET(self):
        time.sleep(TIMEOUT//1000)
        # 200: OK - The request was successful, and the server is returning the requested data.
        # 404: Not Found - The requested resource could not be found on the server.
        # 500: Internal Server Error - An unexpected error occurred on the server while processing the request.
        # 302: Found/Redirect - The requested resource has been temporarily moved to a different location. The client should redirect to the new location.
        # 403: Forbidden - The client does not have permission to access the requested resource.
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        data = self.generate(self.path) # Use the current URL to generate a new seed for randomization
        self.wfile.write(data.encode())
        
        
def RunServer():
    # Using system.argv (Input: python my_script.py arg1 arg2 ==> Output:['my_script.py', 'arg1', 'arg2'])
    # sys.argv[0] == script name (ex: script.py)
    # sys.argv[1] == script.py argv1
    name = os.path.basename(sys.argv[0])
    if '-h' in sys.argv or '--help' in sys.argv:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[==[Usage]==]\n\n> Without File: {name}\n> With File: {name} -f FILE_NAME")
        exit()
        
    # Using len it helps to solve problem whether user run the script with word python or not
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[2] == '-f'):
        try:
            filename = sys.argv[2] if sys.argv[1] == '-f' else sys.argv[1]
            with open(filename, 'r') as file:
                RequestHandlerAPI.websites = [line.strip() for line in file]
                print(RequestHandlerAPI.websites)
                
            if not RequestHandlerAPI.websites:
                print('Provided FILE was empty, Using generated links.')
                RequestHandlerAPI.websites = None
                
        except Exception as error:
            print(f'Error: {error}.')
            
    try:
        print(f"Starting the SERVER on port {PORT}...")
        server = HTTPServer((HOST, PORT), RequestHandlerAPI)
        print("Server has started! Use Ctrl+C to stop")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping the server...")
        server.shutdown()
        print("Server has stopped!")
    except Exception as error:
        print(f"Error: {error}")
        
if __name__ == '__main__':
    RunServer()
