Python 3.8.5

Script Library Requirements
1. requests-html
2. bs4
3. csv

To install above requirements
1. open cmd or system console
2. "pip install requests-html"
*Note, the first time you ever run the render() method which is used in the script, it will download Chromium into your home directory (e.g. ~/.pyppeteer/). This only happens once.
3. "pip install bs4"
4. "pip install csv"

Script usage guide
1. This code scrapes operationally avaiable capacity of SG Resources Mississippi from gasnom.com.
2. Script scrapes data from May 30th, 2024 only.
3. A csv file with the name "SGResourcesMississippi-OperationallyAvailableCapacity-May-30-2024" is generated on the local directory containing the scraped data.
4. Data is already generated and saved in the csv file on this repo but if you would like to test the functionality of the script, feel free to pull the repo on your local machine and delete the csv file before running the script, or just download the script itself instead.
