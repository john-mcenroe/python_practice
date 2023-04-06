import pandas as pd                        
from pytrends.request import TrendReq
from datetime import datetime, timedelta

# Create a pandas dataframe with keywords
pytrend = TrendReq()
df = pytrend.trending_searches(pn='united_states')
df.head()

now = datetime.now()
last_hour = now - timedelta(hours=1)
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
last_hour_str = last_hour.strftime("%Y-%m-%d %H:%M:%S")

related_queries = pytrend.related_queries()
related_queries.values()

# Define a function to get the trend score for a keyword
def get_trend_score(keyword):
    pytrend.build_payload(kw_list=[keyword], timeframe='2022-01-15 2022-01-15', geo='US')
    df_trend = pytrend.interest_by_region()
    trend_score = df_trend[keyword].mean()
    related_queries = pytrend.related_queries()
    related_topics = pytrend.related_topics()
    return trend_score

# Apply the function to every row in the dataframe
df['trend_score'] = df[0].apply(get_trend_score)
df = df.sort_values('trend_score', ascending = False)
print(df.head(100))


# Get relevant trends from Google Trends and related queries
def get_relevant_trends():
    pytrend = TrendReq()
    df = pytrend.trending_searches(pn='united_states')
    df['trend_score'] = df[0].apply(get_trend_score)
    df = df.sort_values('trend_score', ascending = False)
    return df


# Get related queries for the top trends
def get_related_queries():
    df = get_relevant_trends()
    related_queries = {}
    for keyword in df[0].head(10):
        pytrend.build_payload(kw_list=[keyword], timeframe='2022-01-15 2022-01-15', geo='US')
        related_queries[keyword] = pytrend.related_queries()
    return related_queries

# Get related topics for the top trends
def get_related_topics():
    df = get_relevant_trends()
    related_topics = {}
    for keyword in df[0].head(10):
        pytrend.build_payload(kw_list=[keyword], timeframe='2022-01-15 2022-01-15', geo='US')
        related_topics[keyword] = pytrend.related_topics()
    return related_topics

# Combine topics, queries and trends together into a data frame keyed on trends
def combine_all():
    df = get_relevant_trends()
    related_queries = get_related_queries()
    related_topics = get_related_topics()
    df_combined = pd.DataFrame()
    for keyword in df[0].head(1):
        df_combined[keyword] = related_queries[keyword][keyword]['query']
        df_combined[keyword + ' topics'] = related_topics[keyword][keyword]['title']
    return df_combined

# Get the top 10 trends and related queries and topics
df_combined = combine_all()
df_combined.head(10)
