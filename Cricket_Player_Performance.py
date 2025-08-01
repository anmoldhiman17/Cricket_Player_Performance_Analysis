import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style='whitegrid')

# Cricket Player Performance Dataset (sample)
data = {
    'Player': ['Virat Kohli', 'MS Dhoni', 'Rohit Sharma', 'Jasprit Bumrah', 'Hardik Pandya', 'KL Rahul'],
    'Role': ['Batsman', 'Batsman', 'Batsman', 'Bowler', 'All-Rounder', 'Batsman'],
    'Matches': [250, 347, 243, 130, 125, 100],
    'Runs': [12000, 10500, 9800, 120, 3500, 4200],
    'Wickets': [4, 1, 8, 230, 70, 0],
    'Strike Rate': [93.2, 87.6, 90.5, None, 113.7, 89.4],
    'Average': [58.2, 50.6, 48.7, None, 34.5, 44.2]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# ---------------------- Top 5 Run Scorers ----------------------
top_runs = df.sort_values(by='Runs', ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x='Runs', y='Player', data=top_runs, palette='crest')
plt.title('Top 5 Run Scorers - Cricket Player Performance', fontsize=16)
plt.xlabel('Total Runs')
plt.ylabel('Player')
plt.tight_layout()
plt.show()

# ---------------------- Top 5 Wicket Takers ----------------------
top_wickets = df.sort_values(by='Wickets', ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x='Wickets', y='Player', data=top_wickets, palette='flare')
plt.title('Top 5 Wicket Takers - Cricket Player Performance', fontsize=16)
plt.xlabel('Total Wickets')
plt.ylabel('Player')
plt.tight_layout()
plt.show()

# ---------------------- Strike Rate vs Average ----------------------
plt.figure(figsize=(10, 6))
filtered = df.dropna(subset=['Strike Rate', 'Average'])
sns.scatterplot(data=filtered, x='Strike Rate', y='Average', hue='Player', s=100, palette='tab10')
plt.title('Strike Rate vs Batting Average', fontsize=16)
plt.xlabel('Strike Rate')
plt.ylabel('Batting Average')
plt.tight_layout()
plt.show()

# ---------------------- Role-wise Count ----------------------
plt.figure(figsize=(6, 6))
sns.countplot(data=df, x='Role', palette='Set2')
plt.title('Number of Players by Role')
plt.xlabel('Player Role')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
