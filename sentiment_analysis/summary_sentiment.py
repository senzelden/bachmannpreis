import pandas as pd
import spacy
from spacy_sentiws import spaCySentiWS


class SentimentAnalyzer:
    """Performs sentiment analysis"""

    def __init__(self, source='../data/database_csvs/discussion_summary.csv', sentiws_path='../data/sentiws', output_path='summary_sentiment.csv'):
        self.source = source
        self.sentiws_path = sentiws_path
        self.output_path = output_path


    def full_summary(self):
        """performs sentiment analysis on full summary"""

        def _preprocess_text_with_spacy(summary, model):
            """returns text with lemmatized tokens"""
            one_summary = []
            doc = model(summary)
            for word in doc:
                if not word.is_stop and word.is_alpha:
                    if str(word) in ["Winkels", "Spinnen"]:
                        word = str(word)
                    else:
                        word = word.lemma_
                    one_summary.append(word)
            return ' '.join(one_summary)

        def _sentiment_analysis(summaries, model):
            """performs sentiment analysis with sentiWS, returns new DataFrame"""
            sentiment_scores = []
            summary_sentiment = pd.DataFrame()
            for i, summary in enumerate(summaries):
                doc = model(summary)
                sentiment_score = 0
                total_tokens = 0
                pos_tokens = 0
                neg_tokens = 0
                not_covered_tokens = 0
                positive_rating = 0
                negative_rating = 0
                pos_tokens_dict = {}
                neg_tokens_dict = {}
                for token in doc:
                    if not token.is_stop and token.is_alpha:
                        #                 token = token.lemma_
                        total_tokens += 1
                        if type(token._.sentiws) is float:
                            sentiment_score += token._.sentiws
                            if token._.sentiws > 0:
                                if str(token) not in pos_tokens_dict.keys():
                                    pos_tokens_dict[str(token)] = 1
                                else:
                                    pos_tokens_dict[str(token)] += 1
                                pos_tokens += 1
                                positive_rating += token._.sentiws
                            elif token._.sentiws < 0:
                                if str(token) not in neg_tokens_dict.keys():
                                    neg_tokens_dict[str(token)] = 1
                                else:
                                    neg_tokens_dict[str(token)] += 1
                                neg_tokens += 1
                                negative_rating += token._.sentiws
                        else:
                            not_covered_tokens += 1
                sentiment_score = sentiment_score / (pos_tokens + neg_tokens)
                positive_rating = positive_rating / pos_tokens
                negative_rating = negative_rating / neg_tokens

                print(i + 524, "SENTIMENT ANALYSIS: ")
                print("TOTAL SENTIMENT SCORE: ", sentiment_score)
                print("TOTAL TOKENS: ", total_tokens)
                print("TOKENS WITHOUT SENTIMENT: ", not_covered_tokens)
                print("POSITIVE TOKENS: ", pos_tokens)
                print("POSITIVE RATING: ", positive_rating)
                print("NEGATIVE TOKENS: ", neg_tokens)
                print("NEGATIVE RATING: ", negative_rating)
                sentiment_scores.append(sentiment_score)
                sentiment_distance = positive_rating - negative_rating
                print("SENTIMENT DISTANCE: ", sentiment_distance)
                {k: v for k, v in sorted(pos_tokens_dict.items(), key=lambda item: item[1])}
                print("POSITIVE TOKENS DICTIONARY: ", pos_tokens_dict)
                {k: v for k, v in sorted(neg_tokens_dict.items(), key=lambda item: item[1])}
                print("NEGATIVE TOKENS DICTIONARY: ", neg_tokens_dict, "\n")
                summary_sentiment = pd.concat([summary_sentiment, pd.DataFrame(
                    [[i + 524], [total_tokens], [sentiment_score], [not_covered_tokens], [pos_tokens],
                     [positive_rating], [neg_tokens], [negative_rating], [sentiment_distance], [str(summary)],
                     [pos_tokens_dict], [neg_tokens_dict]]).transpose()])
            return summary_sentiment


        df = pd.read_csv(self.source, index_col='text_id')
        print("Source loaded ..")
        nlp = spacy.load('de_core_news_md')
        print("Spacy model loaded ..")
        print("Starting preprocessing ..")
        df['processed_summary'] = df['discussion_summary'].apply(lambda row: _preprocess_text_with_spacy(row, nlp))
        print("Summaries preprocessed ..")
        summaries = df[~df['discussion_summary'].isna()]['processed_summary'].values
        sentiws = spaCySentiWS(sentiws_path=self.sentiws_path)
        nlp.add_pipe(sentiws)
        summary_sentiment = _sentiment_analysis(summaries, nlp)
        print("Sentiment analysis completed ..")
        summary_sentiment = summary_sentiment.rename(
            columns={0: "text_id", 1: "total_tokens", 2: "sentiment_score", 3: "tokens_without_sentiment",
                     4: "positive_tokens", 5: "positive_sentiment", 6: "negative_tokens", 7: "negative_sentiment",
                     8: "sentiment_distance", 9: "element_text", 10: "pos_tokens",
                     11: "neg_tokens"}).reset_index().drop(columns='index').set_index('text_id').copy()
        summary_sentiment.to_csv(self.output_path)
        print("DataFrame saved ..")


    def detailed_summary(self):
        """performs sentiment analysis on summary details"""

        def _preprocess_text_with_spacy(summary, model):
            """returns text with lemmatized tokens"""
            one_summary = []
            doc = model(summary)
            for word in doc:
                if not word.is_stop and word.is_alpha:
                    if str(word) in ["Winkels", "Spinnen"]:
                        word = str(word)
                    else:
                        word = word.lemma_
                    one_summary.append(word)
            return ' '.join(one_summary)

        def _detailed_sentiment_analysis(df2, model):
            """performs detailed sentiment analysis with sentiWS, returns new DataFrame"""
            detailed_scores = pd.DataFrame()
            for author_id in range(524, (len(df2) + 524)):
                print(author_id)
                critics = critics_all[
                    critics_all.year == int(df2.iloc[author_id - 524].date_participation[:4])].full_name.values
                critics_last_names = [critic.split()[-1] for critic in critics]
                if author_id >= 717 and author_id <= 827:
                    split_summary = df2.iloc[author_id - 524]['discussion_summary'].split("\n")
                else:
                    split_summary = df2.iloc[author_id - 524]['discussion_summary'].split("\n\n")
                cleaned_split_summary = []
                for split in split_summary:
                    if split == "":
                        pass
                    else:
                        split = _preprocess_text_with_spacy(split, model)
                        cleaned_split_summary.append(split)
                for i, summary in enumerate(cleaned_split_summary):
                    talking_ids = []
                    talking = []
                    doc = nlp(summary)
                    sentiment_score = 0
                    total_tokens = 0
                    pos_tokens = 0
                    neg_tokens = 0
                    not_covered_tokens = 0
                    positive_rating = 0
                    negative_rating = 0
                    pos_tokens_dict = {}
                    neg_tokens_dict = {}
                    for token in doc:
                        if not token.is_stop and token.is_alpha:
                            #                 token = token.lemma_
                            total_tokens += 1
                            if type(token._.sentiws) is float:
                                sentiment_score += token._.sentiws
                                if token._.sentiws > 0:
                                    if str(token) not in pos_tokens_dict.keys():
                                        pos_tokens_dict[str(token)] = 1
                                    else:
                                        pos_tokens_dict[str(token)] += 1
                                    pos_tokens += 1
                                    positive_rating += token._.sentiws
                                elif token._.sentiws < 0:
                                    if str(token) not in neg_tokens_dict.keys():
                                        neg_tokens_dict[str(token)] = 1
                                    else:
                                        neg_tokens_dict[str(token)] += 1
                                    neg_tokens += 1
                                    negative_rating += token._.sentiws
                            else:
                                not_covered_tokens += 1
                    if pos_tokens > 0 or neg_tokens > 0:
                        sentiment_score = sentiment_score / (pos_tokens + neg_tokens)
                        if pos_tokens > 0:
                            positive_rating = positive_rating / pos_tokens
                        if neg_tokens > 0:
                            negative_rating = negative_rating / neg_tokens
                    sentiment_distance = positive_rating - negative_rating
                    for j, critic in enumerate(critics):
                        if (critic in split_summary[i]) or (critics_last_names[j] in split_summary[i]):
                            talking.append(critic)
                            talking_ids.append(str(critics_all[critics_all.full_name == critic]['critic_id'].values[0]))
                    print(author_id, i, ", ".join(talking), sentiment_score)
                    {k: v for k, v in sorted(pos_tokens_dict.items(), key=lambda item: item[1])}
                    {k: v for k, v in sorted(neg_tokens_dict.items(), key=lambda item: item[1])}
                    detailed_scores = pd.concat([detailed_scores, pd.DataFrame(
                        [[author_id], [i], ["|".join(talking_ids)], ["|".join(talking)], [total_tokens], [sentiment_score],
                         [not_covered_tokens], [pos_tokens], [positive_rating], [neg_tokens], [negative_rating],
                         [sentiment_distance], [split_summary[i]], [pos_tokens_dict], [neg_tokens_dict]]).transpose()])
            return detailed_scores

        df = pd.read_csv(self.source, index_col='text_id')
        nlp = spacy.load('de_core_news_md')
        sentiws = spaCySentiWS(sentiws_path=self.sentiws_path)
        nlp.add_pipe(sentiws)
        critics_participations = pd.read_csv('../data/database_csvs/critics_participations_all.csv')
        critics = pd.read_csv('../data/database_csvs/critics_updated.csv')
        critics_all = pd.merge(critics_participations, critics, left_on='critic_id', right_on='critic_id')
        critics_all["full_name"] = critics_all["first_name"].str.cat(
            critics_all[["middle_name", "last_name"]].fillna("").astype(str), sep=" ").str.replace("  ", " ")
        texts = pd.read_csv('../data/database_csvs/texts_updated.csv', index_col='text_id')
        df2 = pd.merge(df, texts[['date_participation']], left_on='text_id', right_on='text_id')
        detailed_summary_sentiments = _detailed_sentiment_analysis(df2, nlp)
        detailed_summary_sentiments = detailed_summary_sentiments.rename(
            columns={0: "text_id", 1: "element_position", 2: "critic_ids_talking", 3: "critics_talking",
                     4: "total_tokens", 5: "sentiment_score", 6: "tokens_without_sentiment", 7: "positive_tokens",
                     8: "positive_sentiment", 9: "negative_tokens", 10: "negative_sentiment", 11: "sentiment_distance",
                     12: "element_text", 13: "pos_tokens_dict", 14: "neg_tokens_dict"}).reset_index().drop(
            columns='index').copy()
        detailed_summary_sentiments.to_csv('detailed_sentiment_updated.csv')

if __name__ == "__main__":
    sentiment_analysis = SentimentAnalyzer(source='../data/database_csvs/discussion_summary.csv', sentiws_path='../data/sentiws')
    sentiment_analysis.detailed_summary()