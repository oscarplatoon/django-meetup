from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_groups, name='all_groups'),
    path('<int:group_id>', views.group_detail, name='group_detail'),
    path('new', views.new_group, name='new_group'),
    path('<int:group_id>/edit', views.edit_group, name='edit_group'),
    path('<int:group_id>/delete', views.delete_group, name='delete_group'),
    path('<int:group_id>/join', views.join_group, name='join_group'),
    path('<int:group_id>/leave', views.leave_group, name='leave_group'),
    path('<int:group_id>/event/<int:event_id>', views.event_detail, name='event_detail'),
    path('<int:group_id>/event/new', views.new_event, name='new_event'),
    path('<int:group_id>/event/<int:event_id>/edit', views.edit_event, name='edit_event'),
    path('<int:group_id>/event/<int:event_id>/delete', views.delete_event, name='delete_event'),
]
