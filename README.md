# Project: Bachmannpreis

![ER model bachmann database](images/bachmann_postgres_er.jpeg)

### Background

The 'Tage der deutschsprachigen Literatur' in Klagenfurt, Austria, is a major literary festival and basically the only one that is being televised in German television. This event consists of readings of 30 minutes by a number of invited writers who are being evaluated by a circle of critics. The culmination of the event is a live voting by the critics to determine which writers receive an award, most notably the Ingeborg-Bachmann-Preis. For several germanspeaking writers this event has been a starting or ending point for their literary career. 

### Structure

This project consists of five parts that have been realised:

##### 1. Getting the data / Wrangling the data / Storing the data
* Scrape data about the event (Wikipedia, official website of Bachmannpreis) using BeautifulSoup
* Use Goodreads API and geopy to acquire additional data
* Data Wrangling with pandas
* Set up database with PostgreSQL

##### 2. NLP
* Sentiment analysis for jury discussion (with spacy and SentiWS)
* NER and POS-tagging for texts using flair
* Topic modeling with NMF and TFIDF

##### 3. Feature Engineering / Prediction
* Engineer features for prediction within Pandas
* Predict winning authors with Random Forest model using AutoSKLearn

##### 4. Web application
* Deploy website using Flask and chart.js
* Live website: http://countbachmann.herokuapp.com

##### 5. Chatbot
* Program chatbot for user interaction (Rasa)
