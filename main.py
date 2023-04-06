import json


class Player:

    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def goals(self):
        return self.goals, self.games

    def score(self):
        return self.goals + self.assists, self.goals

    def __str__(self):
        return f"{self.name:22}{self.team:5}{self.goals:2} + {self.assists:2} = {self.goals + self.assists:2} "


class FileHandler:

    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        with open(self.filename) as my_file:
            read = my_file.read()
        return json.loads(read)


class Application:

    def __init__(self):
        self.players = []

    def search_for_player(self):
        who = input("player name:")
        for player in self.players:
            if who == player.name:
                print(player)

    def teams(self):
        # teams = sorted(set(map(lambda player: player.team, self.players)))
        teams = sorted(set([player.team for player in self.players]))
        for team in teams:
            print(team)

    def countries(self):
        # countries = sorted(set(map(lambda player: player.nationality, self.players)))
        countries = sorted(set([player.nationality for player in self.players]))
        for country in countries:
            print(country)

    def players_in_team(self):
        team = input("which team? ")
        # filtered = sorted(filter(lambda player: player.team == team, self.players), key=self.score, reverse=True)
        filtered = sorted([player for player in self.players if player.team == team], key=Player.score, reverse=True)
        for player in filtered:
            print(player)

    def players_from_country(self):
        nationality = input("which nationality? ")
        # filtered = sorted(filter(lambda player: player.nationality == nationality, self.players), key=self.score, reverse=True)
        filtered = sorted([player for player in self.players if player.nationality == nationality], key=Player.score,
                          reverse=True)
        for player in filtered:
            print(player)

    def most_points(self):
        how_many = int(input("how many to show? "))
        players = sorted([player for player in self.players], key=Player.score, reverse=True)
        count = 0
        for player in players:
            if count < how_many:
                print(player)
                count += 1

    def most_goals(self):
        how_many = int(input("how many to show? "))
        players = sorted([player for player in self.players], key=Player.goals, reverse=True)
        count = 0
        for player in players:
            if count < how_many:
                print(player)
                count += 1

    def help(self):
        print("0 to exit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        chosen_file = input("choose filename:")
        filename = FileHandler(chosen_file)

        for player in FileHandler.load_file(filename):
            p = Player(player["name"], player['nationality'], player['assists'], player['goals'], player['penalties'],
                       player['team'], player['games'])
            self.players.append(p)

        print(f"read data of {len(self.players)} players")
        self.help()
        while True:
            command = input("what do you want to see? ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()


app = Application()
app.execute()

