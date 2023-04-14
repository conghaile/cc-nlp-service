## CoinCrowd NLP Service*
An application that receives scraped threads via REST API calls from the CoinCrowd scraper, performs NLP on each sentence in each post, and puts the results into a Postgres database. It's not very useful if you don't have your own model trained on shitposts.

**(Not actually a microservice)*