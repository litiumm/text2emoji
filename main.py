import pandas as pd

df = pd.read_json("emojis.json")
df = df.drop(["category", "definition", "shortcode", "name", "senses"], axis=1)
df["unicode"] = df["unicode"].str.split(" ").str.get(0)

text = input("Input: ")
textSplit = text.split(" ")


def tte(word):
    for j in df["keywords"]:  # j is list
        row = df[df['keywords'].apply(lambda x: x == [word])].index.tolist()
    if row:
        emote = df.iloc[row[0], 1]  # Get the value in the "unicode" column
        emote = "\\U000" + emote[2:]
        return (emote.encode().decode("unicode_escape"))
    else:
        return word


for i in range(len(textSplit)):
    textSplit[i] = tte(textSplit[i])
for i in textSplit:
    print(i, end=" ")
