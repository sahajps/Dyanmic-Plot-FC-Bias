import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def color_map_USA(v):
    cm = []
    for i in v:
        if(i>0):
            cm.append((0, 0.3922, 0, i))
        else:
            cm.append((0.7098, 0.2824, 0.5019, abs(i)))

    return cm

def color_map_IN(v):
    cm = []
    for i in v:
        if(i>0): 
            cm.append((0, 0, 1, i))
        else:
            cm.append((1, 0, 0, abs(i)))

    return cm


def map_en_name(s):
    if(s=='aap' or s=='bjp' or s=='tmc'):
        return s.upper()
    
    return s.title()

########################################################

def map_to_root(df):
    top_dic = {}
    for dic in df.sentiments:
        for k in dic:
            try:
                top_dic[k] += [dic[k]]
            except:
                top_dic[k] = [dic[k]]

    return top_dic

def sent_count(l):
    dic = {'positive': 0, 'negative': 0, 'neutral': 0}
    for i in l:
        try:
            dic[i] +=1
        except:
            continue

    return dic

def polarity_score(d):
    P = d['positive']
    N = d['negative']
    T = sum(d.values())

    try:
        return (P-N)/T #, (P*0.0 + N*0.29412)/T #(P, N, T-P-N)
    except:
        return 0 #, 0
    
def Main(f, y, m):
    df = pd.read_json('data/Topic Sentiment Data/'+f+'.json')

    if(y!='all'):
        df = df[df.date_year==y]
        #df = df[df.date_month.isin(m)]

    top_senti_list = map_to_root(df)

    for k in top_senti_list:
        top_senti_list[k] = sent_count(top_senti_list[k])

    top_senti_list = dict(sorted(top_senti_list.items(), key=lambda x: x[1]['positive'] + x[1]['negative'] + x[1]['neutral'], reverse=True))

    return top_senti_list


    
#########################################################################

def gen_plot(top_en_no, start_date, end_date):
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
        top_senti_list = Main(f, 'all', 'all')

        df = pd.DataFrame(columns=['year']+list(top_senti_list)[:top_en_no])

        PS = {'year': 'all'}
        for k in top_senti_list:
            try:
                #PS[k] = top_senti_list[k]#polarity_score(top_senti_list[k])
                PS[k] = polarity_score(top_senti_list[k])
            except:
                PS[k] = 0

        df.loc[len(df)] = PS

        labels = list(df.iloc[0].index)[1:]
        labels = [map_en_name(i) for i in labels]
        values = list(df.iloc[0])[1:]

        ax.barh(np.arange(len(labels)), values, color=color_map_USA(values))
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