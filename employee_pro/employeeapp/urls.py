from django.urls import path
from employeeapp.views import emp, show, edit, update, destroy

urlpatterns = [
    path('add', emp, name='emp'),
    path('', show, name='show'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='delete'),
]
