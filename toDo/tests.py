from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task
from .serializers import TaskCreateSerializer, TaskListSerializer, TaskUpdateSerializer


class TaskViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def create_task(self, data):
        return self.client.post(reverse('create_task'), data, format='json')

    def get_tasks(self):
        return self.client.get(reverse('get_tasks'), format='json')

    def update_task(self, task_id, data):
        return self.client.patch(reverse('update_task', kwargs={'task_id': task_id}), data, format='json')

    def delete_task(self, task_id):
        return self.client.delete(reverse('delete_task', kwargs={'task_id': task_id}), format='json')

    def test_create_task(self):
        data = {'title': 'New Task',
                'description': 'Task Description', 'status': 'To Do'}
        response = self.create_task(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        response = self.get_tasks()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        task = Task.objects.create(
            title='Task 1', description='Description', status='To Do')
        data = {'status': 'Done'}
        response = self.update_task(task.id, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.create(
            title='Task 1', description='Description', status='To Do')
        response = self.delete_task(task.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
