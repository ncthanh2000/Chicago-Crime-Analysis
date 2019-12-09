import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
def crime_proximity(_dataframe, _feature, _threshhold):
    names = _dataframe[_feature].value_counts().keys().tolist()
    counts = _dataframe[_feature].value_counts().tolist()
    df_count = pd.DataFrame()
    df_count[_feature] = names
    df_count['Count'] = counts
    total_count = df_count['Count'].sum()
    df_count['Percentage'] = df_count.apply(lambda row: int(round(100*row['Count']/total_count, 0)), 
                                            axis=1)
    df_count = df_count[df_count['Percentage'] >= _threshhold]
    return df_count

def crime_proximity_bar(_df, _feature):
    fig, axes = plt.subplots(ncols = 1, figsize = (20,7))
    sns.barplot(y = _df[_feature], x = _df['Primary Type'], ax = axes)
    axes.set_ylabel("Crime Proportion")
    axes.set_xlabel("Primary Type")
    if(len(_df['Primary Type']) > 8):
        axes.set_xticklabels(axes.xaxis.get_majorticklabels(), rotation=90)
    fig.suptitle('Proportion of Crimes per Type', fontsize=20)
    plt.show()

def community_proximity_bar(_df, _feature):
    fig, axes = plt.subplots(ncols = 1, figsize = (20,7))
    sns.barplot(y = _df[_feature].astype(int), x = _df['Community Area'], ax = axes)
    axes.set_ylabel("Crime Proportion")
    axes.set_xlabel("Community Area")
    fig.suptitle('Proportion of Crimes per Community Area', fontsize=20)
    plt.show()

def arrest_proximity_bar(_df, _feature):
    fig, axes = plt.subplots(ncols = 1, figsize = (20,7))
    sns.barplot(y = _df[_feature], x = _df['Arrest'], ax = axes)
    axes.set_ylabel("Arrest Proportion")
    axes.set_xlabel("Arrest")
    fig.suptitle('Proportion of Arrest '+ '\n'+ str(_df), fontsize=20)
    plt.show()

def pie(_df, _feature):
    fig, axes = plt.subplots(ncols = 1, figsize = (15,7))
    axes.pie(_df[_feature], labels=_df['Arrest'], autopct='%1.1f%%',
        shadow=True, startangle=90)
    axes.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig.suptitle('Proportion of Arrest', fontsize=20)
    plt.show()