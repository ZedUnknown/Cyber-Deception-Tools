# CursedPort
## Instructions
Please provide the URLs in a list format. Each URL should be listed on a separate line without any additional formatting or prefixes, such as 'http://' or 'https://'. Simply list the domain name itself. 

_For example:_  
www.wikipedia.org  
www.youtube.com  
www.github.com  
www.google.com  
.  
.  
.


Make sure to remove any extra characters, spaces, or line breaks. This format will help prevent hackers from accessing the original websites.

## Customizing Generated URLs

The script provides options to customize the generated URLs. Here are the configurable parameters and their descriptions:

- `HOST`: The host address where the server will run. By default, it is set to an empty string.
- `PORT`: The port number on which the server will listen. By default, it is set to `8000`.

- `URLs_PER_GENERATE`: The range of how many URLs to generate per page. By default, it is set to generate between 7 and 12 URLs.
- `LENGTH_OF_URL`: The range of the length of each generated URL. By default, it is set to generate URLs with lengths between 20 and 32 characters.

- `TIMEOUT`: The delay (in milliseconds) between receiving a request and serving a response. By default, it is set to `350`.

- `ENABLE_UPPER_CASE`: Enable or disable uppercase letters in generated URLs. By default, it is set to `True`.
- `ENABLE_LOWER_CASE`: Enable or disable lowercase letters in generated URLs. By default, it is set to `True`.
- `ENABLE_DIGITS`: Enable or disable digits (numbers) in generated URLs. By default, it is set to `True`.
- `ENABLE_PUNCTUATIONS`: Enable or disable punctuation characters in generated URLs. By default, it is set to `True`.

Feel free to modify these parameters in the script to customize the behavior of the generated URLs according to your preferences.

## Running the Code

To run the code, execute the following command in your terminal:

```bash
python cursedport.py
```
This will run the code with the default settings. If you prefer to use custom website names, you can provide a text file with the -f flag:

```bash
python cursedport.py -f FILENAME.txt
```
The file should contain a list of website names, with each name on a separate line.

## Feedback and Suggestions

Your feedback and suggestions are valuable to us! If you encounter any problems, have ideas for improvement, or would like to suggest additional options, please feel free to:

- Open an issue in this repository to report a problem or bug.
- Submit a pull request if you have a solution or enhancement to contribute.
- Reach out to us through the contact information provided in the repository.

We appreciate your input and look forward to hearing from you! Together, we can make this project even better.
