import pandas as pd


def words_to_learn_csv(data):
    words_to_learn_df = pd.DataFrame(data)
    words_to_learn_df.to_csv("./data/words_to_learn.csv", index=False)
