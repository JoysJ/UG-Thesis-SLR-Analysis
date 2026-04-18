import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- 1. Publication Volume per Year ---
def plot_publication_volume():
    data = {2008: 1, 2009: 1, 2013: 1, 2014: 1, 2015: 1, 2017: 2, 2018: 2, 
            2019: 3, 2020: 15, 2021: 11, 2022: 10, 2023: 17, 2024: 21, 2025: 44, 2026: 2}
    years, counts = list(data.keys()), list(data.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(years, counts, color='skyblue', edgecolor='navy')
    plt.title('Annual Publication Volume (2008-2026)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Papers', fontsize=12)
    plt.xticks(years, rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, v in enumerate(counts):
        plt.text(years[i], v + 0.5, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('fig_1_publication_volume.png')
    plt.close()

# --- 2. Language Distribution ---
def plot_languages():
    languages = {"English": 28, "Chinese": 12, "Spanish": 9, "French": 8, "Korean": 6, 
                "Japanese": 5, "Hindi": 5, "Arabic": 5, "Italian": 2, "German": 2} # Top 10 for clean visual
    sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    names, values = [x[0] for x in sorted_langs], [x[1] for x in sorted_langs]
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(names[::-1], values[::-1], color='teal', alpha=0.8)
    plt.title('Top 10 Explicitly Named Languages in Corpus', fontsize=14)
    plt.xlabel('Number of Papers', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    
    for bar in bars:
        plt.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
                f'{int(bar.get_width())}', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('fig_2_language_distribution.png')
    plt.close()

# --- 3. Application Domains ---
def plot_domains():
    data = {'Open-Domain / General': 11, 'Healthcare & Mental Health': 8, 
            'Task-Oriented & Customer Service': 7, 'NLP Tasks & Evaluation': 5, 
            'Embodied Agents & Robotics': 4, 'Other': 4, 'Education': 3}
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
    labels, values = list(sorted_data.keys()), list(sorted_data.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(labels, values, color='lightgreen', edgecolor='darkgreen')
    plt.title('Distribution of Application Domains', fontsize=14)
    plt.xlabel('Number of Papers', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    for i, v in enumerate(values):
        plt.text(v + 0.2, i, str(v), va='center', fontweight='bold')
        
    plt.tight_layout()
    plt.savefig('fig_3_application_domains.png')
    plt.close()

# Run all functions
if __name__ == "__main__":
    print("Generating Thesis Visualizations...")
    plot_publication_volume()
    plot_languages()
    plot_domains()
    print("Complete! Charts saved as PNG files in your current directory.")
