from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .models import Task
from .serializers import TaskCreateSerializer, TaskListSerializer, TaskUpdateSerializer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods


# Create a new task
@api_view(['POST'])
def create_task(request):
    serializer = TaskCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Read (Get a list of tasks)
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)


# Update (Change the status of a task)
@api_view(['PATCH'])
@require_http_methods(['PATCH'])
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskUpdateSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a task


@api_view(['DELETE'])
@require_http_methods(['DELETE'])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})
