from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.listing, name="listing"),
    path("<int:id>", views.avalib_list, name="avalib_list"),
    path("my_listings", views.my_listings, name="my_listings"),
    path('sell/<int:id>/', views.sell_listing, name='sell_listing'),
    path("history", views.history, name="history"),
    path("del_listing/<int:id>", views.del_listing, name="del_listing"),
    path("watchlist", views.watchlist, name="watchlist")
    
]
