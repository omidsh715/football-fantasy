
from players.models import Player
from django.conf import settings


class Team(object):

    def __init__(self, request):
        self.session = request.session
        team = self.session.get(settings.TEAM_SESSION_ID)
        if not team:
            team = self.session[settings.TEAM_SESSION_ID] = {}
        self.team = team

    def add(self, player):
        player_id = str(player.id)
        player_pos = str(player.position)
        player_price = str(player.price)
        self.team[player_id] = {'player_pos': player_pos, 'player_price': player_price}
        """example : {'12': {'player_pos': GK, 'player_price': 7}}"""
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, player):
        player_id = str(player.id)
        if player_id in self.team:
            del self.team[player_id]
            self.save()

    def __iter__(self):
        player_ids = self.team.keys()
        players = Player.objects.filter(id__in=player_ids)

        team = self.team.copy()
        for player in players:
            team[str(player.id)]['player'] = player
            yield player

    def get_total_price(self):
        price_list = [int(item['player_price']) for item in self.team.values()]
        return sum(price for price in price_list)

    def clear(self):
        del self.session[settings.TEAM_SESSION_ID]
        self.save()

    def confirm_team(self):
        values = self.team.values()
        (gk_count, def_count, mid_count, mid_count, fw_count) = (0, 0, 0, 0, 0)

        for value in values:
            if value['player_pos'] == 'GK':
                gk_count += 1
            elif value['player_pos'] == 'DEF':
                def_count += 1
            elif value['player_pos'] == 'MID':
                mid_count += 1
            elif value['player_pos'] == 'FW':
                fw_count += 1

        if gk_count > 1 or def_count > 4 or mid_count > 4 or fw_count > 2:
            return False
