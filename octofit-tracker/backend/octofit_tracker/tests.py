from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(email='tony@stark.com', username='IronMan', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30, calories_burned=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'IronMan')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')

    def test_activity_str(self):
        self.assertIn('IronMan', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('IronMan', str(self.leaderboard))
