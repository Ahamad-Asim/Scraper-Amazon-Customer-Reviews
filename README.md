# Scraper-Customer-Reviews

This Scrapy script is used for crawling products and scraping customer reviews. 

It uses the CrawlSpider and Rule classes from Scrapy to navigate through the website and extract relevant information. 
The script is set up to only crawl pages from the domain given in 'allowed_domains' and starts from a specific product link given in 'start_urls'. 

CSS selectors are used to extract the star rating, customer name, and customer review from the page, and the information is combined into a dictionary. 

The script can be easily modified to extract customer reviews from any product page by changing the 'start_urls' and 'allowed_domains' and the respective css or xpath selectors. 

The script is a great tool for collecting data on customer reviews for any product's.


Usage
After giving start_urls', 'allowed_domains' and the respective css or xpath selectors. run the file using scrapy
in terminal it can be run by

```scrapy runspider scraper.py```

Application

Sentiment Analysis: The customer reviews and star ratings can be used to analyze the overall sentiment of customers towards a specific product.

Market Research: The script can be used to collect customer reviews and ratings for a specific product or category of products, which can be used to understand customer preferences and make informed business decisions.

Product Comparison: The script can be used to collect customer reviews and ratings for multiple products in the same category, which can be used to compare and contrast the performance of different products.

Data Analysis: The script can be used to collect a large amount of customer reviews and ratings, which can be analyzed to identify patterns and trends in customer behavior.

NLP: The script can be used to collect customer reviews and ratings for a specific product or category of products, which can be used for natural language processing tasks such as text classification, sentiment analysis and so on.

