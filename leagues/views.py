from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {

		################## SPORTS ORM 1 - Simple Finds ##############################
        # qry_1 = League.objects.filter(sport="Baseball")
        # qry_2 = League.objects.filter(name__contains="Women")
        # qry_3 = League.objects.filter(name__contains="hockey")
        # qry_4 = League.objects.exclude(name__contains="football")
        # qry_5 = League.objects.filter(name__contains="conference")
        # qry_6 = League.objects.filter(name__contains="atlantic")
        # qry_7 = Team.objects.filter(location="Dallas")
        # qry_8 = Team.objects.filter(team_name="Raptors")
        # qry_9 = Team.objects.filter(location__contains="city")
        # qry_10 = Team.objects.filter(team_name__startswith="T")
        # qry_11 = Team.objects.all().order_by("-team_name")
        # qry_12 = Team.objects.all().order_by("team_name")
        # qry_13 = Player.objects.filter(last_name="Cooper")
        # qry_14 = Player.objects.filter(first_name="Joshua")
        # qry_15 = Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
        ### from django.db.models import Q 
        # qry_16 = Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))

		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),

		################## SPORTS ORM 2 - ForeignKey, ManyToMany Relationships ##############################
		"qry_2_1": League.objects.get(name="Atlantic Soccer Conference").teams.all(), 
		"qry_2_2": Team.objects.get(team_name="Penguins").curr_players.all(),
		"qry_2_3": Player.objects.filter(curr_team__league_id=2),
		"qry_2_4": Player.objects.filter(curr_team__league_id=7, last_name="Lopez"),
		"qry_2_5": Player.objects.filter(curr_team__league__sport="Football"),
		"qry_2_6": Team.objects.filter(curr_players__first_name="Sophia"),
		"qry_2_7": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"qry_2_8": Player.objects.filter(last_name="Flores").exclude(curr_team_id=10), #Team.objects.filter(curr_players__last_name="Flores").exclude(league_id=8)
		"qry_2_9": Team.objects.filter(all_players__first_name="Samuel").filter(all_players__last_name="Evans"),
		"qry_2_10": Player.objects.filter(all_teams=37),
		"qry_2_11": Player.objects.filter(all_teams=40).exclude(curr_team=40),
		"qry_2_12": Team.objects.filter(all_players__first_name="Jacob").filter(all_players__last_name="Gray").filter(league_id=9),
		"qry_2_13": Player.objects.filter(all_teams__league_id=3, first_name="Joshua"), #Team.objects.filter(all_players__first_name="Joshua").filter(league_id=3)
		"qry_2_14": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gt=11), # Team.objects.annotate(num=Count('all_players')).order_by('-num')[:24]]
		"qry_2_15": Player.objects.annotate(num_teams=Count('all_teams')).order_by('-num_teams')

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")