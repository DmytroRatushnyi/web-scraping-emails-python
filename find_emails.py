import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time

# Load the data
input_file = "executives.csv"
output_file = "emails_found.csv"
df = pd.read_csv(input_file)

# Debug: Print column names
print("Columns in CSV:", df.columns)

# Function to find emails on a webpage
def find_emails(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        return list(set(emails))  # Remove duplicates
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

# Function to generate possible email formats
def generate_email_formats(name, domain):
    name_parts = name.lower().split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]  # Use the last part as the last name
    else:
        first_name = name_parts[0]
        last_name = ""  # Handle single-part names

    formats = []
    if first_name and last_name:
        formats.extend([
            f"{first_name}.{last_name}@{domain}",  # john.doe@acme.com
            f"{first_name[0]}{last_name}@{domain}", # jdoe@acme.com
            f"{first_name}@{domain}",               # john@acme.com
            f"{last_name}@{domain}",                # doe@acme.com
        ])
    elif first_name:
        formats.append(f"{first_name}@{domain}")    # Handle single-part names
    return formats

# Main logic
results = []
for index, row in df.iterrows():
    name = row['Name']  # Update this if your column name is different
    domain = row['Domain']  # Update this if your column name is different
    print(f"Processing {name} from {domain}...")

    # Option 1: Scrape the company website for emails
    company_url = f"https://{domain}"
    found_emails = find_emails(company_url)

    # Option 2: Generate possible email formats
    possible_emails = generate_email_formats(name, domain)

    # Combine results
    emails = list(set(found_emails + possible_emails))
    results.append({"Name": name, "Company": row['Company'], "Domain": domain, "Emails": ", ".join(emails)})

    # Add a delay to avoid being blocked
    time.sleep(2)

# Save results to a new CSV
results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False, encoding='utf-8')
print(f"Results saved to {output_file}")