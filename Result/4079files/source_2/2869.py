import json

from django.core.management.base import BaseCommand

from game.interactive_static.models import InteractiveStatic, InteractiveStaticRound, Survey

from game.contrib.decimal_encoder import DecimalEncoder


class Command(BaseCommand):

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--ids', nargs='+', type=int)
        group.add_argument('--greater', nargs=1, type=int)
        parser.add_argument('--limit', nargs=1, type=int)

    def handle(self, *args, **options):
        game_class = InteractiveStatic
        rounds_class = InteractiveStaticRound
        if options['greater']:
            qs = game_class.objects.filter(pk__gte=options['greater'][0]).order_by('pk')
            if options['limit']:
                qs = qs[:options['limit'][0]]
        else:
            qs = game_class.objects.filter(pk__in=set(options['ids'])).order_by('pk')

        users = []
        for game in qs:
            for user in game.users.all():
                game_id = game.id
                rounds = rounds_class.objects.filter(user=user)
                d = {'user': user.username,
                     'final_score': user.get_score,
                     'condition': user.game_type,
                     'time_created': user.date_joined,
                     'game_id': game_id,
                     'unanswered': rounds.filter(guess__lt=0).count(),
                     }
                try:
                    s = Survey.objects.get(username=user.username)
                    survey = s.dump()
                except Survey.DoesNotExist:
                    survey = None
                d['survey'] = survey
                d['rounds'] = [r.round_data() for r in rounds]
                if game_id > -1 and game.constraints.max_rounds == len(d['rounds']):
                    d['hit_status'] = 'completed'
                elif user.prompted > 0 and survey is None:
                    d['hit_status'] = 'kicked'
                elif len(d['rounds']) > 0 and game_id != -1:
                    d['hit_status'] = 'disconnected'
                elif game_id == -1:
                    d['hit_status'] = 'game_not_started'
                users.append(d)
        print(json.dumps(users, cls=DecimalEncoder))
