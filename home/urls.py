from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "ICEcream Admin"
admin.site.site_title = "Herokhor Admin Portal"
admin.site.index_title = "Welcome to herokhor Researcher Portal"

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("services",views.services, name="services"),
    path("contact",views.contact, name="contact"),
    path("action",views.action, name="action"),
    path("bhubon",views.bhubon, name="bhubon"),
    path("game",views.game, name="game"),
    path("card",views.card, name="card"),
    path("doodle",views.doodle, name="doodle"),
    path("breakout",views.breakout, name="breakout"),
    path("snake",views.snake, name="snake"),
    path("pong",views.pong, name="pong"),
]
