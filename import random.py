import matplotlib.pyplot as plt
import random

teams = {
    'Mumbai Indians': {'batting_strength': 85, 'bowling_strength': 80, 'all_rounders': 75, 'captaincy': 90},
    'Chennai Super Kings': {'batting_strength': 88, 'bowling_strength': 78, 'all_rounders': 82, 'captaincy': 95},
    'Gujarat Titans': {'batting_strength': 82, 'bowling_strength': 78, 'all_rounders': 70, 'captaincy': 88},
    'Royal Challengers Bangalore': {'batting_strength': 83, 'bowling_strength': 70, 'all_rounders': 75, 'captaincy': 85},
    'Kolkata Knight Riders': {'batting_strength': 78, 'bowling_strength': 75, 'all_rounders': 72, 'captaincy': 84},
}

def calculate_team_strength(team):
    attributes = teams[team]
    base_strength = (attributes['batting_strength'] * 0.4 +
                     attributes['bowling_strength'] * 0.3 +
                     attributes['all_rounders'] * 0.2 +
                     attributes['captaincy'] * 0.1)
    
    if team == 'Chennai Super Kings':
        base_strength *= 1.05  
    return base_strength

def predict_winner(teams):
    team_strengths = {team: calculate_team_strength(team) for team in teams}
    total_strength = sum(team_strengths.values())
    
    normalized_probabilities = {team: (strength / total_strength) for team, strength in team_strengths.items()}
    
    winner = random.choices(list(normalized_probabilities.keys()), weights=normalized_probabilities.values())[0]
    
    return winner

def simulate_ipl_season(teams, simulations=1000):
    win_counts = {team: 0 for team in teams}
    
    for _ in range(simulations):
        winner = predict_winner(teams)
        win_counts[winner] += 1
    
    win_probabilities = {team: (win_counts[team] / simulations) * 100 for team in teams}
    
    return win_probabilities

win_probabilities = simulate_ipl_season(teams)

for team, probability in win_probabilities.items():
    print(f'{team}: {probability:.2f}% chance of winning')

def plot_bar_chart(win_probabilities):
    teams = list(win_probabilities.keys())
    probabilities = list(win_probabilities.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(teams, probabilities, color='blue')
    
    plt.title('IPL Winning Team Predictions - Bar Chart', fontsize=16)
    plt.xlabel('Teams', fontsize=14)
    plt.ylabel('Winning Probability (%)', fontsize=14)
    
    for bar, prob in zip(bars, probabilities):
        plt.text(bar.get_x() + bar.get_width() / 2.0, bar.get_height(),
                 f'{prob:.2f}%', ha='center', va='bottom', fontsize=12)
    
    plt.show()

def plot_pie_chart(win_probabilities):
    teams = list(win_probabilities.keys())
    probabilities = list(win_probabilities.values())
    
    plt.figure(figsize=(8, 8))
    plt.pie(probabilities, labels=teams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors[:len(teams)])
    
    plt.title('IPL Winning Team Predictions - Pie Chart', fontsize=16)
    plt.show()

def plot_horizontal_bar_chart(win_probabilities):
    teams = list(win_probabilities.keys())
    probabilities = list(win_probabilities.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(teams, probabilities, color='green')
    
    plt.title('IPL Winning Team Predictions - Horizontal Bar Chart', fontsize=16)
    plt.ylabel('Teams', fontsize=14)
    plt.xlabel('Winning Probability (%)', fontsize=14)
    
    for bar, prob in zip(bars, probabilities):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f'{prob:.2f}%', va='center', ha='left', fontsize=12)
    
    plt.show()

plot_bar_chart(win_probabilities)
plot_pie_chart(win_probabilities)
plot_horizontal_bar_chart(win_probabilities)
