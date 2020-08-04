

# positive characteristics:
# 15 protagonist watches TV
def protagonist_is_watching_TV():
    words = ["fernsehen",
             "Fernseher"]

# 21 genre: science fiction

# 30 rodents

# 34 dinosaurs

# 35 space

# 44 octopus

# 45 internet exists

# 46 protagonists are cooking

# 48 author has to read as first person

# negative characteristics:
# 34: title in plural (Vulkantänze, Sondagen) - check for noun in plural (as POS problem)
def plural_in_title():
    ...


# 35: title with punctuation (comma is ok) - POS problem
def punctuation_in_title():
    ...


# 36: title has no relation to text, but is supposed to give an extra dimension - (title in text?)
def relation_title_text():
    ...


# 37: subtitle (allowed: Erzählung, Novelle)
def has_subtitle():
    ...


# 39: first word: adjective - (POS problem)
def is_first_word_adjective():
    ...


def occurence_of_words():
    bad_words = ["ungläubig",
                 "gewiss",
                 "sogleich",
                 "somit",
                 "urplötzlich",
                 "nur allzu",
                 "im Begriff sein, etwas zu tun",
                 "scheint zu",
                 "etwas vermögen",
                 "in diesem Moment",
                 "Stillstand", # except for cars, devices
                 "unmerklich",
                 "nicht enden wollend",
                 "unbeschreiblich", # except in direct speech
                 "alles durchdringend",
                 "windschief",
                 "fassungslos",
                 "gen",
                 "indes",
                 "mit fester / gebieterischer / irgendeiner Stimme",
                 "mit festem / gebieterischem / irgendeinem Blick",
                 "gespielt", # as in gespielt ungezwungene Gesten
                 "betont",
                 "bis zum Zerreißen",
                 "nicht lange fackeln",
                 "panisch",
                 "stürzen", # except hinfallen
                 "scheu",
                 "zerbricht", # an etwas -2 points
                 "Schaudern",
                 "nächstgelegen",
                 "instinktiv",
                 "gleichwohl",
                 "grinsen",
                 "gemahnt an etwas",
                 "gibt kein Halten mehr",
                 "schmerzhaftes Wiedersehen",
                 "soeben",
                 "vernehmen",
                 "zudem",
                 "hektisch",
                 "befindlich",
                 "etwas fristen",
                 "hörbar",
                 "sichtlich",
                 "keines Blickes gewürdigt",
                 "da war es wieder, das",
                 "keine Ahnung, auf was man sich einlässt",
                 "heillos",
                 "schnappt", # except Krokodile as subject
                 "störrische / widerspenstige Haarsträhne"]
    for word in text:
        if word in bad_words:
            return True
    return False


# 49 Protagonists are named Leander, ... except, if they are children
def bad_protagonists_names():
    bad_names=["Leander",
               "Muriel",
               "Luna",
               "Laura",
               "Lena",
               "Lea"]
    for word in text:
        if word in bad_names:
            return True
    return False


# 53 programming_elements (file names as headlines, chat protocols, code in text)
def has_programming_elements():
    ...


# 63 synonyms for "sagen", -2 points "gähnte Leander"
def synonym_of_sagen():
    synonyms = ["gähnen",
                "..."]
    for word in text:
        if word in synonyms:
            return True
    return False


# 69 most common word represents more than 5 percent of all words
def most_common_word_too_often():
    ...


# 75 bad comparison
def bad_comparison():
    bad_comparison = ["wie in Zeitlupe",
                      "wie im Film",
                      "wie in einem schlechten Film",
                      "wie im Traum"]
    for comparison in bad_comparison:
        if comparison in text:
            return True
    return False


# 81 explicit naming of watches, clocks
def occurence_of_watches():
    watch_words=["Uhr",
                 "flic-flac",
                 "Casio-Uhr",
                 "Armbanduhr",
                 "Fitbit"]
    for word in watch_words:
        if word in text:
            return True
    return False


# 100 circus and clowns
def occurence_of_circus():
    bad_words = ["Karussell",
                 "Jahrmarkt",
                 "Zirkus",
                 "Feuerwerk",
                 "Clowns"]
    for word in bad_words:
        if word in text:
            return True
    return False


# 114 exclamation mark outside of direct speech

# 131 talking about Marseille

# 134 talking about "Nacken", except "Nackenkotelett"

# 135 "das kalte Nass", "das warme Nass", "das rote Nass"