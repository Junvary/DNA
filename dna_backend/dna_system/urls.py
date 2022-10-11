from django.urls import path, include
from dna_system.views.user import LoginView, GetUserListView, GetUserMenuView
from dna_system.views.role import GetRoleListView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('get-user-list/', GetUserListView.as_view()),
    path('get-role-list/', GetRoleListView.as_view()),
    path('get-user-menu/', GetUserMenuView.as_view())
]
