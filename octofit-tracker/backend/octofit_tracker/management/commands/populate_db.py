from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Workouts
        cardio = Workout.objects.create(name='Morning Cardio', description='Cardio session', difficulty='Easy')
        strength = Workout.objects.create(name='Strength Training', description='Strength session', difficulty='Medium')

        # Create Users
        users = [
            User.objects.create(username='Superman', email='superman@dc.com', team=dc),
            User.objects.create(username='Batman', email='batman@dc.com', team=dc),
            User.objects.create(username='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(username='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(username='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(username='Spider-Man', email='spiderman@marvel.com', team=marvel),
        ]

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, workout=cardio, duration=30, calories_burned=300)
            Activity.objects.create(user=user, workout=strength, duration=45, calories_burned=400)

        # Create Leaderboard
        for idx, user in enumerate(users, start=1):
            Leaderboard.objects.create(user=user, score=1000-idx*100, rank=idx)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
