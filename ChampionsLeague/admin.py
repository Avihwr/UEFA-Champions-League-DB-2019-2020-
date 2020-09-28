from django.contrib import admin
from .models import *


# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['Groups']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['TeamGroup', 'Team1', 'Team2', 'Team3', 'Team4']

    def get_ordering(self, request):
        return ['TeamGroup']


class ClubAdmin(admin.ModelAdmin):
    list_display = ['Club_Name', 'Club_Manager','Club_Captain', 'Stadium', 'Relation', 'Goals', 'Market_Value', 'img']

    def get_ordering(self, request):
        return ['-Goals']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['Name',
                    'Club',
                    'Age',
                    'Goals',
                    'Overall',
                    'Market_Value',
                    'is_Captain',
                    'imgsrc']

    def get_ordering(self, request):
        return ['-Overall']


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['Manager_name', 'Manager_team',
                    'Manager_age', 'img']

    def get_ordering(self, request):
        return ['-Manager_age']


admin.site.register(TeamGroups, TeamAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Stadium)
admin.site.register(Captain)
