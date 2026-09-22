import matplotlib.pyplot as plt
import pandas as pd
import requests

DRAFT_ID = 522458773321240576
LEAGUE_ID = 522458773317046272

def get_draft_picks(draft_id = DRAFT_ID):
    url = f'https://api.sleeper.app/v1/draft/{draft_id}/picks'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_rosters(league_id = LEAGUE_ID):
    url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def build_draft_dataframe(picks, rosters):
    roster_points = {}

    for roster in rosters:
        roster_id = roster['roster_id']
        points = roster['settings']['fpts']
        roster_points[roster_id] = points

    rows = []

    for pick in picks:
        roster_id = pick['roster_id']
        metadata = pick['metadata']

        rows.append({"pick_no": pick["pick_no"],
            "round": pick["round"],
            "player": metadata["first_name"] + " " + metadata["last_name"],
            "position": metadata["position"],
            "roster_id": roster_id,
            "team_points": roster_points.get(roster_id)})

    return pd.DataFrame(rows)

def load_draft_dataframe():
    picks = get_draft_picks()
    rosters = get_rosters()
    return build_draft_dataframe(picks, rosters)

# # print(picks[0]) - look for 'roster_id' in both outputs -> use that to link pick number and total points acquired
# # for pick in picks:
# #     print(pick['metadata']['first_name'], pick['metadata']['last_name'], pick['metadata']['position'])

# # print(response2.status_code) - prints 200
# # print(rosters[0]) - look for 'roster_id' in both outputs -> use that to link pick number and total points acquired

# # fpts: actual points the team got in total
# # ppts: highest total score a team could have gotten if the team had their highest scoring team in each week

# roster_points = {}
# for roster in rosters:
#     r_id = roster["roster_id"]
#     points = roster["settings"]["fpts"]
#     roster_points[r_id] = points

# rows = []
# for pick in picks:
#     r_id = pick["roster_id"]
#     player_name = pick["metadata"]["first_name"] + " " + pick["metadata"]["last_name"]
#     position = pick["metadata"]["position"]
#     pick_no = pick["pick_no"]
#     round_no = pick['round']
#     pick_number = pick['pick_no']
#     team_points = roster_points.get(r_id, None)

#     rows.append({
#         "pick_no": pick_no,
#         "round": round_no,
#         "player": player_name,
#         "position": position,
#         "roster_id": r_id,
#         "team_points": team_points
#     })

# for row in rows:
#     print(f"{row['player']}: Round {row['round']}, Pick: {row['pick_no']}")

# # Start of the analysis

# df = pd.DataFrame(rows)
# print(df)
# # print(df.head())
# # print(df.shape)

# df = df.dropna(subset = ['team_points'])

# # does higher pick number correspond to a higher amount of points
# correlation = df['pick_no'].corr(df['team_points'])
# print('Correlation between pick number and total team points:', round(correlation, 5))

# # average team points by round
# round_avg = df.groupby('round')['team_points'].mean()
# print(round_avg)

# # average team points based on position drafted
# position_avg = df.groupby('position')['team_points'].mean().sort_values(ascending=False)
# print(position_avg)


# # Beginning of Visualizations

# # round_avg.plot(kind = 'bar', title = 'Average Team Points by Draft Round')
# # plt.xlabel('Round Drafted')
# # plt.ylabel('Average Team Points')
# # plt.tight_layout()
# # plt.show()

# plt.scatter(df['pick_no'], df['team_points'])
# plt.xlabel('Pick Number')
# plt.ylabel('Team Points')
# plt.title("Draft Pick Number vs. Total Team Points")
# plt.tight_layout()
# plt.show()

