"""
URL configuration for ccsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from timetrack.views import TimesheetListView, TimesheetCreateView, TimesheetUpdateView, TimesheetDeleteView, TimeEntryListView

urlpatterns = [
    path('sheet/list/', TimesheetListView.as_view(), name='sheet-list'),
    path('sheet/create/', TimesheetCreateView.as_view(), name='sheet-create'),
    path('sheet/update/<pk>', TimesheetUpdateView.as_view(), name='sheet-update'),
    path('sheet/delete/<pk>', TimesheetDeleteView.as_view(), name='sheet-delete'),
    path('entries/list/<int:timesheet_id>', TimeEntryListView.as_view(), name='entry-list')
]
