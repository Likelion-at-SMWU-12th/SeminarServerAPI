from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Entries
from .serializers import EntriesSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404

class EntriesViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = EntriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        try:
            entries = Entries.objects.all()
            serializer = EntriesSerializer(entries, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            entry = get_object_or_404(Entries, pk=pk)
            serializer = EntriesSerializer(entry)
            return Response(serializer.data)
        except Exception as e:
            if isinstance(e, Http404):
                return Response({"error": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            entry = get_object_or_404(Entries, pk=pk)
            serializer = EntriesSerializer(entry, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"error": "Invalid request body"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if isinstance(e, Http404):
                return Response({"error": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            entry = get_object_or_404(Entries, pk=pk)
            entry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            if isinstance(e, Http404):
                return Response({"error": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)