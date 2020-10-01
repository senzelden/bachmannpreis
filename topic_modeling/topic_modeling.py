import os
import requests

from bs4 import BeautifulSoup as soup
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import spacy

from topic_modeling_helpers import german, names


class NMFTopicModeler:
    """
    Returns topics for collection of documents.
    Expects path to directory with documents(named with increasing integers: 0.txt, 1. txt, ...) or pickled list with texts
    and number of topics to be used for NMF model.

    Params:
    ------------------------------------------
    source: "pickle" or "folder" (default="pickle")
    path_to_documents: relative path (default="../Texte/cleaned")
    pickled_doc_list: relative path (default="cleaned_texts.p")
    n_topics: number of topics for NMF model (default=10)
    """

    def __init__(self, source="pickle", dir="../Texte/cleaned", pickled="cleaned_texts.p", n_topics=10):
        self.source = source
        self.path_to_documents = dir
        self.n_topics = n_topics
        self.pickled_doc_list = pickled

    def run(self):
        """runs topic modeling"""

        def _read_in_texts_indices(self):
            """reads in texts and indices"""
            texts = []
            indices = []
            files = os.listdir(self.path_to_documents)
            for i in range(len(files)):
                with open(
                    f"{self.path_to_documents}/{files[i]}",
                    "r",
                    encoding="utf8",
                    errors="ignore",
                ) as f:
                    text = f.read()
                    texts.append(text)
                    indices.append(i)
            return texts, indices

        def _preprocess_text_with_spacy(short_story, model):
            """return texts with lemmatized words"""
            cleaned_story = ""
            doc = model(short_story)
            for word in doc:
                if not word.is_stop and word.is_alpha:
                    cleaned_story += word.lemma_ + " "
            return cleaned_story.strip()

        def _create_texts_corpus(texts):
            """loads texts from files and stores text and author index in separate lists"""
            lang_model = spacy.load("de_core_news_md")
            cleaned_texts = []
            for i, text in enumerate(texts):
                cleaned_texts.append(_preprocess_text_with_spacy(text, lang_model))
                print(i + 508)
            return cleaned_texts

        def _common_names_from_internet():
            """get common german first names from vorname.com"""
            response = requests.get("https://www.vorname.com/beliebte_vornamen,0.html")
            page = soup(response.text, "html.parser")
            common_names = []
            for name_box in page.find_all(attrs={"class": "name_box"}):
                common_names.append(name_box.find("a").text.lower())
            return common_names

        def _get_tfidf_matrix(names, german, df):
            """returns vectors and matrix for topic modeling based on TF-IDF"""
            common_names = _common_names_from_internet()
            stop_names = set(names + common_names)
            new_stop_words = german + list(stop_names)
            new_stop_words.sort()
            tfidf_vect = TfidfVectorizer(
                max_df=0.8, min_df=2, stop_words=new_stop_words
            )
            doc_term_matrix = tfidf_vect.fit_transform(
                df["cleaned_text"].values.astype("U")
            )
            return tfidf_vect, doc_term_matrix

        def _get_top_10_words_per_topic():
            """prints out top 10 words for each topic"""
            top_10_words_list = []
            for i, topic in enumerate(nmf.components_):
                # print(f'Top 10 words for topic #{i}:')
                top_10_words = [
                    tfidf_vect.get_feature_names()[i] for i in topic.argsort()[-10:]
                ]
                # print(top_10_words)
                top_10_words_list.append("|".join(top_10_words))
            return top_10_words_list

        def _get_topic_and_top_10_words(doc_term_matrix, top_10_words_list):
            """returns lists of topics as integer and top 10 words"""
            topic_values = nmf.transform(doc_term_matrix)
            top_topic_words = []
            for num in topic_values.argmax(axis=1):
                top_topic_words.append(top_10_words_list[num])
            return topic_values, top_topic_words

        def _print_sorted_topics(df, topic_values, top_topic_words):
            """prints topics, top 10 words and occurrences"""
            df["topic"] = topic_values.argmax(axis=1)
            df["topic_top_10_words"] = top_topic_words
            topics = (
                df.groupby(["topic", "topic_top_10_words"])[["index"]]
                .count()
                .reset_index()
                .rename(columns={"topic": "topic_id", "index": "total_count"})
                .set_index("topic_id")
            )
            topics.sort_values("total_count", ascending=False).to_csv("topic_top_words.csv")
            pd.set_option("max_colwidth", 2000)
            print(topics.sort_values("total_count", ascending=False))

        ### Load data into dataframe
        texts, indices = _read_in_texts_indices(self)
        if self.source == "folder":
            cleaned_texts = _create_texts_corpus(texts)
        else:
            cleaned_texts = pickle.load(open(self.pickled_doc_list, "rb"))
        df = pd.DataFrame({"index": indices, "cleaned_text": cleaned_texts})
        ### Prepare matrix and run model
        tfidf_vect, doc_term_matrix = _get_tfidf_matrix(names, german, df)
        nmf = NMF(n_components=self.n_topics, max_iter=1000, random_state=42)
        nmf.fit(doc_term_matrix)
        ### Print results
        top_10_words_list = _get_top_10_words_per_topic()
        topic_values, top_topic_words = _get_topic_and_top_10_words(
            doc_term_matrix, top_10_words_list
        )
        _print_sorted_topics(df, topic_values, top_topic_words)


if __name__ == "__main__":
    topic_model = NMFTopicModeler("pickle", "../Texte/cleaned", "cleaned_texts.p", 10)
    topic_model.run()
