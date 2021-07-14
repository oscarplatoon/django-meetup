from django.shortcuts import render, redirect
from .models import Group, Event, User, UserGroup
from .forms import GroupForm, EventForm
# Create your views here.
def all_groups(request):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  all_groups = Group.objects.all()
  return render(request, 'groups/all_groups.html', {'all_groups': all_groups})

def _tutorial(request):
  if request.user.is_anonymous == True:
    all_groups = Group.objects.all()
    return render(request, 'groups/all_groups.html', {'all_groups': all_groups})
  else:
    request.user.viewed_tutorial = True
    request.user.save()
    return render(request, 'tutorial.html', {})

def group_detail(request, group_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  group = Group.objects.get(id=group_id,)
  if UserGroup.objects.filter(group=group, user=request.user):
    joined = True
  else:
    joined = False
  members = group.members.all()
  events = group.events.all()
  return render(request, 'groups/group_detail.html', {'group': group, 'members': members, 'events': events, 'joined': joined})

def new_group(request):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  if request.method == 'POST':
    form = GroupForm(request.POST)
    if form.is_valid():
      group = form.save(commit=False)
      group.owner = request.user
      group.save()
      return redirect('group_detail', group.id)
  else:
    form = GroupForm()
  return render(request, 'groups/group_form.html', {'form': form, 'type': 'New'})

def edit_group(request, group_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  group = Group.objects.get(id=group_id)
  if request.method == 'POST':
    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
      group = form.save(commit=False)
      group.owner = request.user
      group.save()
      return redirect('group_detail', group.id)
  else:
    form = GroupForm(instance=group)
  return render(request, 'groups/group_form.html', {'form': form, 'type': 'Edit'})

def delete_group(request, group_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  group = Group.objects.get(id=group_id)
  group.delete()
  return redirect('all_groups')

# EVENTS
def event_detail(request, group_id, event_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  event = Event.objects.get(id=event_id)
  group = Group.objects.get(id=group_id)
  return render(request, 'events/event_detail.html', {'event': event})

def new_event(request, group_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      event = form.save(commit=False)
      event.group = Group.objects.get(id=group_id)
      event.save()
      return redirect('event_detail', group_id, event.id)
  else:
    form = EventForm()
  return render(request, 'events/event_form.html', {'form': form, 'type': 'New'})

def edit_event(request, group_id, event_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  event = Event.objects.get(id=event_id)
  if request.method == 'POST':
    form = EventForm(request.POST, instance=event)
    if form.is_valid():
      event = form.save(commit=False)
      event.group = Group.objects.get(id=group_id)
      event.save()
      return redirect('event_detail', group_id, event.id)
  else:
    form = EventForm(instance=event)
  return render(request, 'events/event_form.html', {'form': form, 'type': 'Edit'})

def delete_event(request, group_id, event_id):
  if request.user.is_anonymous or request.user.viewed_tutorial == False:
    return _tutorial(request)
  event = Event.objects.get(id=event_id)
  event.delete()
  return redirect('group_detail', group_id)


def join_group(request, group_id):
  group = Group.objects.get(id=group_id)
  group.members.add(request.user)
  return redirect('group_detail', group_id)

def leave_group(request, group_id):
  group = Group.objects.get(id=group_id)
  group.members.remove(request.user)
  return redirect('group_detail', group_id)


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error_404.html', data)
