# Fantasy Football Draft Analysis

## Overview

This project analyzes fantasy football draft data to explore how draft position relates to player production and overall team performance. Using data retrieved from the Sleeper API, I built a Python-based data pipeline to collect, clean, and organize draft and league data before analyzing patterns across draft rounds and pick positions.

The goal of the project is to determine whether drafting earlier provides a measurable advantage and how the importance of draft position changes throughout the draft.

## Research Questions

This project focuses on several questions:

- Does an earlier draft position lead to better overall team performance?

- How does the relationship between draft position and team performance change across draft rounds?

- Do early, middle, and late draft positions produce noticeably different outcomes?

## Key Findings

The analysis suggests that the value of draft position varies across rounds rather than providing a consistent advantage throughout the draft.

- Earlier selections showed a stronger relationship with team outcomes in the first round.

- The relationship between pick position and performance became less consistent in later rounds.

- These results suggest that having an early pick may provide an initial advantage, but later-round drafting and overall roster construction remain important to team success.

## Data & Methodology

Draft and league data are collected directly from the Sleeper API using Python's `requests` library.

The data pipeline retrieves draft selections and roster results before combining them into a **pandas DataFrame**. Each draft selection includes information such as:

- Overall pick number

- Pick position within the round

- Draft round

- Player name and position

- Associated fantasy roster

- Team fantasy points

- Potential fantasy points

- Team wins and losses

Draft positions are also classified into three groups:

| Draft Group | Pick Positions |
| ----------- | -------------- |
| Early       | Picks 1–4      |
| Middle      | Picks 5–8      |
| Late        | Picks 9–12     |

The resulting dataset is then analyzed by draft round and pick group to examine relationships between draft position and team performance.

## Technologies

- **Python**

- **pandas** — data cleaning, transformation, and analysis

- **requests** — Sleeper API requests

- **Plotly** — interactive data visualizations

- **Jupyter Notebook** — exploratory analysis and documentation

## Project Structure

`pull_data.py`

Handles data collection and preparation. The script retrieves draft picks and roster information from Sleeper, combines the datasets, calculates each player's position within a draft round, and classifies selections as Early, Middle, or Late.

`data_visualization.ipynb`

Contains the exploratory analysis and visualizations used to investigate relationships between draft position and team performance across different rounds of the draft.

## Limitations

The current analysis focuses on a single fantasy football league and draft, so the results should not be interpreted as universal relationships between draft position and fantasy football performance.

Team performance is also influenced by factors beyond initial draft position, including:

- Waiver-wire activity

- Trades

- Player injuries

- Lineup decisions

- Later-round selections

These factors are not fully captured by draft position alone.

## Future Improvements

Future versions of the project could:

- Analyze multiple leagues and seasons to increase the sample size

- Compare player-level fantasy production directly with draft position

- Measure draft value relative to expected performance at each pick

- Account for player position when evaluating draft value

- Develop predictive models for player or team performance based on draft information

## Data Source

Fantasy football draft and league data are retrieved using the Sleeper API with specific league and draft IDs. These IDs can be changed to analyze different leagues and drafts within Sleeper.
