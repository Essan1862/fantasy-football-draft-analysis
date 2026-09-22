import pandas as pd
import requests

DRAFT_ID = 522458773321240576
LEAGUE_ID = 522458773317046272
TEAMS_PER_ROUND = 12

def get_draft_picks(draft_id = DRAFT_ID):
    url = f'https://api.sleeper.app/v1/draft/{draft_id}/picks'
    response = requests.get(url, timeout = 30)
    response.raise_for_status()
    return response.json()

def get_rosters(league_id = LEAGUE_ID):
    url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
    response = requests.get(url, timeout = 30)
    response.raise_for_status()
    return response.json()

def build_draft_dataframe(picks, rosters, teams_per_round = TEAMS_PER_ROUND):
    roster_results = {}

    for roster in rosters:
        roster_id = roster['roster_id']
        settings = roster.get('settings', {})

        roster_results[roster_id] = {"team_points": settings.get("fpts"),
            "potential_points": settings.get("ppts"),
            "team_wins": settings.get("wins"),
            "team_losses": settings.get("losses")}

    rows = []

    for pick in picks:
        roster_id = pick['roster_id']
        metadata = pick.get('metadata', {})
        results = roster_results.get(roster_id, {})

        first_name = metadata.get("first_name", "")
        last_name = metadata.get("last_name", "")
        player_name = f"{first_name} {last_name}".strip()

        rows.append(
            {
                "pick_no": pick["pick_no"],
                "pick_in_round": ((pick["pick_no"] - 1) % teams_per_round) + 1,
                "round": pick["round"],
                "player_id": pick.get("player_id"),
                "player": player_name,
                "position": metadata.get("position"),
                "roster_id": roster_id,
                "team_points": results.get("team_points"),
                "potential_points": results.get("potential_points"),
                "team_wins": results.get("team_wins"),
                "team_losses": results.get("team_losses"),
            }
        )

    df = pd.DataFrame(rows)

    df["pick_group"] = pd.cut(
        df["pick_in_round"],
        bins=[0, 4, 8, teams_per_round],
        labels=["Early", "Middle", "Late"],
        include_lowest=True,
    )

    return df

def load_draft_dataframe(draft_id = DRAFT_ID, league_id = LEAGUE_ID,
                         teams_per_round = TEAMS_PER_ROUND):
    
    picks = get_draft_picks(draft_id)
    rosters = get_rosters(league_id)
    return build_draft_dataframe(picks, rosters, teams_per_round)

if __name__ == "__main__":
    draft_df = load_draft_dataframe()
    print(draft_df.head())
    print(f"\nRows: {len(draft_df)}")
