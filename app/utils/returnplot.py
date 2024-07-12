import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.colors import LinearSegmentedColormap

# below two functions return color code for histogram based on the intensity of Polarity Score
def color_map_USA(v):
    """
    Returns list of RGB color combinations for histogram (For organizations from USA).

    Args:
        v (list): List of values of polarity score ranging from -1 to 1

    Returns:
        list: List of RGB values for plot according to the intensity of Polarity Score
    """
    cm = []
    for i in v:
        if(i>0):
            cm.append((0, 0.3922, 0, i))
        else:
            cm.append((0.7098, 0.2824, 0.5019, abs(i)))

    return cm
def color_map_IN(v):
    """
    Returns list of RGB color combinations for histogram (For organizations from India).

    Args:
        v (list): List of values of polarity score ranging from -1 to 1

    Returns:
        list: List of RGB values for plot according to the intensity of Polarity Score
    """
    cm = []
    for i in v:
        if(i>0): 
            cm.append((0, 0, 1, i))
        else:
            cm.append((1, 0, 0, abs(i)))

    return cm


def map_en_name(s):
    """
    Returns the entity strings into proper format eg.: narendra modi: Narendra Modi and aap: AAP

    Args:
        s (str): Political entity

    Returns:
        str: Political entity in proper form
    """
    if(s in ['bjp', 'aap', 'tmc', 'goi', 'rss']):
        return s.upper()
    
    return s.title()

def entity_sent(df):
    """
    Returns the dic of entities as key and list of sentiments associated with it. Eg. {Donald Trump: [positive, negative, negative, ....], ...}

    Args:
        df (dataframe): Pandas dataframe with sentiments named column which contains the entities in an articles and associated sentiment in dic form

    Returns:
        dic: {Donald Trump: [positive, negative, negative, ....], ...} like dic
    """
    en_dic = {}
    for dic in df.sentiments:
        for k in dic:
            try:
                en_dic[k] += [dic[k]]
            except:
                en_dic[k] = [dic[k]]

    return en_dic

def sent_count(l):
    """
    Returns numbers of each kind of sentiments

    Args:
        l (list): List of sentiments associated with an entity over a range of articles

    Returns:
        dic: Dic with positive, negative and neutral as keys and their count as values
    """
    dic = {'positive': 0, 'negative': 0, 'neutral': 0}
    for i in l:
        try:
            dic[i] +=1
        except:
            continue

    return dic

def polarity_score(d):
    """
    Returns the polarity score for a given entity

    Args:
        d (dic): A dic with number of positive, negative and neutral sentiments
    
    Returns:
        float: Polarity score ranging from -1 to 1
    """
    P = d['positive']
    N = d['negative']
    T = sum(d.values())

    try:
        return (P-N)/T
    except:
        return 0
    
def top_entities_sorted(f, s_date, e_date):
    """
    Given media house name and date filer returns the unique entities' dic with sentiment associated in desc order of their frequency

    Args:
        f (str): Media house name
        s_date (datetime): From date
        e_date (datetime): To date

    Returns:
        dic: 
    """
    df = pd.read_json('data/Topic Sentiment Data/'+f+'.json')

    date_objs = []
    # Loop through the lists and convert to datetime objects
    for day, month, year in zip(df.date_day, df.date_month, df.date_year):
        date_str = f"{day} {month} {year}"
        date_obj = datetime.strptime(date_str, '%d %B %Y')
        date_objs.append(date_obj)

    df['date'] = date_objs

    df = df[(df.date>=s_date) & (df.date<=e_date)]

    top_senti_list = entity_sent(df)

    for k in top_senti_list:
        top_senti_list[k] = sent_count(top_senti_list[k])

    top_senti_list = dict(sorted(top_senti_list.items(), key=lambda x: x[1]['positive'] + x[1]['negative'] + x[1]['neutral'], reverse=True))

    return top_senti_list

#########################################################################

def gen_plot(order, top_en_no, start_date, end_date):
    map_org_name = {'checkyourfact': 'Check Your Fact', 'politifact': 'PolitiFact', 'snopes': 'Snopes', 'altnews': 'Alt News', 'boomlive': 'Boom', 'opindia': 'OpIndia'}

    fig, ((ax1), (ax2), (ax3), (ax4), (ax5), (ax6)) = plt.subplots(6, 1, sharex=True, figsize=(7, 1.5*top_en_no))

    plt.rcParams['font.size'] = 13

    error_bar_settings = {
        'ecolor': 'black',  
        'elinewidth': 0.4,    
        'capsize': 2,
        'capthick': 0.4
    }

    for f,ax in zip(['checkyourfact', 'politifact', 'snopes', 'altnews', 'boomlive', 'opindia'], [ax1, ax2, ax3, ax4, ax5, ax6]):
        top_senti_list = top_entities_sorted(f, start_date, end_date)

        top_en = list(top_senti_list)[:top_en_no]
        PS = {}
        for k in top_en:
            try:
                #PS[k] = top_senti_list[k]#polarity_score(top_senti_list[k])
                PS[k] = polarity_score(top_senti_list[k])
            except:
                PS[k] = 0

        #print(order)
        if(order=='Alphabatic'):
            PS = dict(sorted(PS.items()))

        #print(PS)

        labels = list(PS)
        labels.reverse()
        labels = [map_en_name(i) for i in labels]
        values = list(list(PS.values()))
        values.reverse()

        if(f in ['checkyourfact', 'politifact', 'snopes']):
            ax.barh(np.arange(len(labels)), values, color=color_map_USA(values))
        else:
            ax.barh(np.arange(len(labels)), values, color=color_map_IN(values))

        ax.text(0.95, 0.95, map_org_name[f], transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='right')

        midpoint = 0#(np.min(values) + np.max(values)) / 2
        ax.axvline(x=midpoint, color='k', linestyle='-', linewidth=0.85) 
        
        ax.set_yticks(np.arange(len(labels)))
        ax.set_yticklabels(labels)

        if(f=='opindia'):
            ax.set_xticks([-1,-0.5,0,0.5,1]) 
            ax.set_xticklabels([-1,-0.5,0,0.5,1], fontsize=10)  
            ax.set_xlabel("Polarity Score", fontsize=13.5)

    fig.text(-0.0, 0.5, 'Top '+str(top_en_no)+' most frequent political entities', va='center', rotation='vertical', fontsize=13.5)
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.1, hspace=0.15)

    return plt