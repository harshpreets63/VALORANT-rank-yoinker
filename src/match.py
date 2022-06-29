from colr import color


class Match:
    def __init__(self, Requests, log):
        self.Requests = Requests
        self.log = log

    def get_recent_five_matches(self, puuid: str):
        response = self.Requests.fetch('pd',
                                       f"/mmr/v1/players/{puuid}/competitiveupdates?queue=competitive&startIndex=0&endIndex=5",
                                       "get")
        point_earned = []
        try:
            if response.ok:
                self.log("retrieved rank successfully")
                r = response.json()
                for match in r["Matches"]:
                    if match["RankedRatingEarned"] > 0:
                        rank_color = (50, 226, 178)
                    elif match["RankedRatingEarned"] < 0:
                        rank_color = (255, 70, 84)
                    else:
                        rank_color = (127, 127, 127)
                    point_earned.append(color(str(match["RankedRatingEarned"]), fore=rank_color))
        except Exception:
            pass
        while len(point_earned) < 5:
            point_earned.append(color("×", fore=(127, 127, 127)))
        return point_earned
