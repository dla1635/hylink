from rest_framework import viewsets
from .serializers import LinkSerializer, TagSerializer, LabelSerializer
from .serializers import LinkTagSerializer, LinkTagDetailSerializer, LinkLabelSerializer, LinkLabelDetailSerializer
from .models import Link, Tag, Label, LinkTag, LinkLabel
from rest_framework import permissions

# from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework import status, viewsets
# from rest_framework.filters import OrderingFilter
# from rest_framework.response import Response


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)       

class LinkLabelViewSet(viewsets.ModelViewSet):
    queryset = LinkLabel.objects.all()
    serializer_class = LinkLabelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        
class LinkTagViewSet(viewsets.ModelViewSet):
    queryset = LinkTag.objects.all()
    serializer_class = LinkTagSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# class LinkTagViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     Return the given match.
#     list:
#     Return a list of all the existing matches.
#     create:
#     Create a new match instance.
#     """
#     queryset = LinkTag.objects.all()
#     serializer_class = LinkTagSerializer # for list view
#     detail_serializer_class = LinkTagDetailSerializer # for detail view
#     filter_backends = (DjangoFilterBackend, OrderingFilter,)
#     ordering_fields = '__all__'
#     def get_serializer_class(self):
#         """
#         Determins which serializer to user `list` or `detail`
#         """
#         if self.action == 'retrieve':
#             if hasattr(self, 'detail_serializer_class'):
#                 return self.detail_serializer_class
#         return super().get_serializer_class()
#     def get_queryset(self):
#         """
#         Optionally restricts the returned queries by filtering against
#         a `sport` and `name` query parameter in the URL.
#         """
#         queryset = LinkTag.objects.all()
#         link = self.request.query_params.get('link', None)
#         tag = self.request.query_params.get('tag', None)
#         if link is not None:
#             link = link.title()
#             queryset = queryset.filter(link__name=link)
#         if tag is not None:
#             queryset = queryset.filter(tag=tag)
#         return queryset
#     def create(self, request):
#         """
#         to parse the incoming request and create a new match or update
#         existing odds.
#         """
#         message = request.data.pop('message_type')
#         # check if incoming api request is for new event creation
#         if message == "NewEvent":
#             event = request.data.pop('event')
#             sport = event.pop('sport')
#             markets = event.pop('markets')[0] # for now we have only one market
#             selections = markets.pop('selections')
#             sport = Sport.objects.create(**sport)
#             markets = Market.objects.create(**markets, sport=sport)
#             for selection in selections:
#                 markets.selections.create(**selection)
#             match = Match.objects.create(**event, sport=sport, market=markets)
#             return Response(status=status.HTTP_201_CREATED)
#         # check if incoming api request is for updation of odds
#         elif message == "UpdateOdds":
#             event = request.data.pop('event')
#             markets = event.pop('markets')[0]
#             selections = markets.pop('selections')
#             for selection in selections:
#                 s = Selection.objects.get(id=selection['id'])
#                 s.odds = selection['odds']
#                 s.save()
#             match = Match.objects.get(id=event['id'])
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)