# Fanstasy-Football
# Fantasy Sports

## Introduction
For this project, you can choose your own sport and create a fantasy league for it.

## Objectives
The functionality required from this project is:

- Draft a team - ensure that players are available
- Score player stats over a period of time
- Determine team total after interpreting stats

You may find that some of the work overlaps with another feature and that a common helper function would be useful.

### Extra challenges
If you would like to take your project a step further, consider these:

- Draft multiple teams
    - Determine league winner
    - Only allow a player on 1 team
- Limit a team to a certain set of positions
- Input multiple weeks of data
    - Output the team's score after each week
- Rank multiple teams
- Create a nice way to print out your data (i.e. "pretty print")

## Notes
You will need to create your own test data for this. There are several examples from different sports inside the `TestData` folder to the left. The first row contains labels for the columns for your benefit (you don't need to include this). To create your own, make a spreadsheet with the player's stats for a certain time period and download it as either a tab-separated values file or a comma-separated values file.

There is also a `read_data()` function that opens the file with a given name and returns the contents as a `string`. This is already called in your `main()` function to give you an example. You may change the code in `main()` but do not change the `read_data()` function.

## Example
**NOTE** This is just a sample. You may choose a different format.

```
Welcome to the Fantasy Quidditch League!

How many teams do you have this season? 2

Enter the next team name: Team1
Enter the next team name: Team2

Enter the name of player #1 for team Team1: H. Potter
Enter the name of player #1 for team Team2: C. Chang
Enter the name of player #2 for team Team1: K. Bell
Enter the name of player #2 for team Team2: O. Wood

How many weeks are in this season? 4

Rankings after week 1
{'Team2': 322, 'Team1': 115}


Rankings after week 2
{'Team2': 687, 'Team1': 278}


Rankings after week 3
{'Team2': 981, 'Team1': 430}


Rankings after week 4
{'Team2': 1207, 'Team1': 457}


Team2 is the winner!
```
