# News Headline & Article Link Scraper

This Python application automatically extracts current news headlines, publication times, and direct article links from a specified news website. The collected data is then saved into a .csv (Comma Separated Values) file, making it easily viewable and analyzable.

# What It Does
News Information Extraction: Gathers article titles, their publication dates/times, and the direct links to the detailed news pages from the target news site.

Data Recording (CSV): Saves all extracted news data into a structured .csv file. This format can be easily opened and processed with spreadsheet programs like Excel.

Up-to-Date Information Access: Provides fast and efficient data extraction from static or semi-dynamic content on news websites.

# Why Is This Important?
Current news data is vital for fields like media monitoring, market analysis, trend identification, or tracking developments on specific topics. This application helps by:

Media Monitoring: Offers the potential to automatically track news related to specific keywords or subjects.

Market Trends: Helps you catch market trends and announcements by monitoring news relevant to your industry.

Time & Effort Savings: Eliminates the need for manual news site Browse and data collection, saving valuable time and resources.

# Technologies Used
Python: The primary programming language used for developing the application.

requests Library: Used for sending HTTP requests and retrieving HTML content from websites.

BeautifulSoup Library: Utilized for easily parsing the retrieved HTML content and extracting specific data.

csv Module (Python Built-in): Used for writing the collected data into a standard CSV file format.

# How It Works
The application sends an HTTP request to the specified news website and retrieves the page's HTML content.

It then uses BeautifulSoup to parse and analyze this HTML content.

For each news item, it identifies and extracts information such as the headline, publication time, and article link.

All collected data is gathered into lists.

Finally, the collected data is written row by row into a CSV file named news_data.csv using Python's built-in csv module.

