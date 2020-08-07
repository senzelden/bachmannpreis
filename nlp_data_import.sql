CREATE TABLE summary_sentiments (
    text_id INTEGER,
    total_tokens INTEGER,
    sentiment_score REAL,
    tokens_wo_sentiment INTEGER,
    positive_tokens INTEGER,
    positive_sentiment REAL,
    negative_tokens INTEGER,
    negative_sentiment REAL,
    sentiment_distance REAL,
    discussion_summary TEXT,

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE
);

\COPY summary_sentiments FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/summary_sentiments.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE detailed_summary_sentiments (
    text_id INTEGER,
    element_position INTEGER,
    critic_ids_talking VARCHAR(50),
    critics_talking VARCHAR(200),
    total_tokens INTEGER,
    sentiment_score REAL,
    tokens_wo_sentiment INTEGER,
    positive_tokens INTEGER,
    positive_sentiment REAL,
    negative_tokens INTEGER,
    negative_sentiment REAL,
    sentiment_distance REAL,
    summary_element TEXT,

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE
);

\COPY detailed_summary_sentiments FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/detailed_sentiment.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE most_common_words (
    text_id INTEGER,
    word VARCHAR(100),
    total_count INTEGER
);

\COPY most_common_words FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/most_common_words.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE text_topics (
    text_id INTEGER,
    top_10_words TEXT,
    topic_count INTEGER,

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE
);

\COPY text_topics FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/texts_topics.csv' DELIMITER ',' CSV HEADER;


CREATE TABLE text_basics (
    text_id INTEGER,
    text_length INTEGER,
    total_sentences INTEGER,
    topic_id INTEGER,

    FOREIGN KEY (text_id)
        REFERENCES texts ON DELETE CASCADE
);

\COPY text_basics FROM '/home/denniss/Desktop/Coding/spiced/bachmannpreis/text_infos_updated.csv' DELIMITER ',' CSV HEADER;