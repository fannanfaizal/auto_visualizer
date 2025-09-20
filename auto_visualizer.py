import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from column_detector import detect_column_types 


def visualize(df: pd.DataFrame):

    col_types = detect_column_types(df)
    
    for col, ctype in col_types.items():
        print(f"Visualizing {col} ({ctype})...")

        if ctype == "numerical":
            plt.figure(figsize=(15, 4))

            plt.subplot(1, 3, 1)
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f"Histogram of {col}")

            plt.subplot(1, 3, 2)
            sns.boxplot(x=df[col])
            plt.title(f"Boxplot of {col}")

            plt.subplot(1, 3, 3)
            plt.scatter(df.index, df[col])
            plt.title(f"Scatter Plot of {col}")
            plt.xlabel("Index")
            plt.ylabel(col)

            plt.tight_layout()
            plt.show()

        elif ctype == "categorical":
            plt.figure(figsize=(12, 5))

            plt.subplot(1, 2, 1)
            sns.countplot(x=df[col])
            plt.title(f"Count Plot of {col}")
            plt.xticks(rotation=45)

            plt.subplot(1, 2, 2)
            freq = df[col].value_counts()
            sns.barplot(x=freq.index, y=freq.values)
            plt.title(f"Bar Chart of {col}")
            plt.xticks(rotation=45)

            plt.tight_layout()
            plt.show()

        elif ctype == "text":
            text_data = " ".join(df[col].dropna().astype(str))
            if text_data.strip():  

                wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)
                
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                plt.title(f"Word Cloud for {col}")
                plt.show()

                words = pd.Series(" ".join(df[col].dropna().astype(str)).lower().split())
                freq = words.value_counts().head(10)

                plt.figure(figsize=(6, 4))
                sns.barplot(x=freq.values, y=freq.index)
                plt.title(f"Top 10 Words in {col}")
                plt.show()


if _name_ == "_main_":
    df = pd.DataFrame({
        "Age": [23, 25, 30, 40, 29, 35],
        "Salary": [3000, 3500, 4000, 4200, 5000, 5500],
        "Gender": ["M", "F", "M", "M", "F", "F"],
        "Review": [
            "Good product",
            "Excellent service and fast delivery",
            "Bad experience",
            "Nice",
            "Very useful and handy",
            "Average quality"
        ]
    })
    visualize(df)
