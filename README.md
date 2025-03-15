# web-scraping-emails-python

## Description
This Python script scrapes company websites to find publicly available email addresses and generates potential email formats based on a given list of executives. It takes input from a CSV file containing names, company names, and domains, then saves the discovered and generated emails to a new CSV file.

## Features
- Scrapes email addresses from company websites.
- Generates possible email formats based on names and domains.
- Removes duplicate emails for better accuracy.
- Saves the results to a CSV file.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/DmytroRatushnyi/web-scraping-emails-python.git
   cd web-scraping-emails-python

2. Install dependencies:
   pip install -r requirements.txt

## Usage
1️. Prepare the input CSV file (executives.csv)
Create a CSV file with the following structure:
- Name,Company,Domain
- John Doe,Acme Inc,acme.com
- Jane Smith,TechCorp,techcorp.com

2. Run the script:
   python find_emails.py

3. The script will:
Scrape email addresses from the provided domains.
Generate possible email formats based on names.
Save results to emails_found.csv.

## Output Format
The script saves results in emails_found.csv with the structure:
- Name,Company,Domain,Emails
- John Doe,Acme Inc,acme.com,john.doe@acme.com, jdoe@acme.com
- Jane Smith,TechCorp,techcorp.com,jane@techcorp.com, jane.smith@techcorp.com

## Notes
This script does not guarantee email accuracy.
Scraping too many sites quickly may result in being blocked; a delay is added to avoid this.
Ensure compliance with website terms of service before scraping.

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome! If you find issues, feel free to open an issue.

🚀 Happy Scraping! 🚀
