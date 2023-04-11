def net_rr(runs_scored, overs_played, runs_conceded, overs_bowled):
    nrr = ((runs_scored / overs_played) - (runs_conceded / overs_bowled)) 
    return nrr

# To determine the team with the higher NRR
def higher_nrr(team1_nrr, team2_nrr):
    if team1_nrr > team2_nrr:
        return "Team 1 has a higher NRR"
    elif team2_nrr > team1_nrr:
        return "Team 2 has a higher NRR"
    else:
        return "The teams have the same NRR"

# Example data of two teams
team1_runs_scored = int(input('T1 runs scored-' ))
team1_overs_played = int(input('T1 overs played-'))
team1_runs_conceded =int(input('T1 runs conceded-'))
team1_overs_bowled = int(input('T1 overs bowled-'))

team2_runs_scored = int(input('T2 runs scored-' ))
team2_overs_played = int(input('T2 overs played-'))
team2_runs_conceded =int(input('T2 runs conceded-'))
team2_overs_bowled = int(input('T2 overs bowled-'))

# Calculate NRR for each team
team1_nrr = net_rr(team1_runs_scored, team1_overs_played, team1_runs_conceded, team1_overs_bowled)
team2_nrr = net_rr(team2_runs_scored, team2_overs_played, team2_runs_conceded, team2_overs_bowled)

# Determine which team has the higher NRR
result = higher_nrr(team1_nrr, team2_nrr)
print(result)

# Tie-breaker condition
if team1_nrr == team2_nrr:
    team1_total_runs = team1_runs_scored - team1_runs_conceded
    team2_total_runs = team2_runs_scored - team2_runs_conceded
    if team1_total_runs > team2_total_runs:
        print("Team 1 has a higher total runs scored")
    elif team2_total_runs > team1_total_runs:
        print("Team 2 has a higher total runs scored")
    else:
        print("The teams have the same total runs scored")
