import sqlite3
import pandas as pd
conn = sqlite3.connect("./snippets/snippets.db")

languages = ['Python', 'Java', 'C', 'C++', 'Go', 'JavaScript', 'HTML']


def get_snippets(lang):
    c = conn.cursor()
    c.execute("SELECT snippet, language FROM snippets WHERE language =:lang ORDER BY RANDOM()", {
              'lang': lang})
    tuple = c.fetchmany(10000)
    df = pd.DataFrame(tuple)
    print(df.shape)
    # print(df)
    df.to_csv(f"data_{lang.lower()}.csv")
    conn.commit()

for language in languages:
    get_snippets(language)

conn.close()
