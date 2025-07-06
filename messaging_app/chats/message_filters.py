import django_filters
from .models import Message


class MessageFilter(django_filters.FilterSet):
    # Filter messages by sender's username, case-insensitive partial match
    sender_username = django_filters.CharFilter(field_name="sender__username", lookup_expr='icontains')

    # Custom filter to find messages where conversation includes a participant with a username matching the input
    conversation_participant = django_filters.CharFilter(method='filter_by_participant')

    # Filters to get messages sent on or after a specific datetime
    timestamp_after = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    # Filters to get messages sent on or before a specific datetime
    timestamp_before = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    # Alternative date filters (start and end of range) for the message timestamp
    start_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    # Another filter for sender username (similar to sender_username)
    sender = django_filters.CharFilter(field_name="sender__username", lookup_expr='icontains')
    # Filter messages by conversation ID (exact match)
    conversation = django_filters.NumberFilter(field_name="conversation__id")
    
    def filter_by_participant(self, queryset, name, value):
        # Filters messages where the conversation's participants' usernames contain the search term
        return queryset.filter(conversation__participants__username__icontains=value)

    class Meta:
        model = Message
        # Define which filter fields are exposed for filtering
        fields = ['sender_username', 'conversation_participant', 'timestamp_after', 'timestamp_before']



class MessageFilter(django_filters.FilterSet):
    # Filter messages sent from this date/time onwards
    start_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    # Filter messages sent up to this date/time
    end_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')
    # Filter messages by sender username, case-insensitive partial match
    sender = django_filters.CharFilter(field_name="sender__username", lookup_expr='icontains')
    # Filter messages by exact conversation ID
    conversation = django_filters.NumberFilter(field_name="conversation__id")

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'start_date', 'end_date']