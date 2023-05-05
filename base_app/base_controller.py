from rest_framework.serializers import ModelSerializer
from base_app.utils import CleanDict
from base_app.http import Request, Response
from base_app.base_repo import BaseRepo


class BaseController:
    def __init__(self) -> None:
        self.request = Request
        self.responses = Response()
        self.repo = BaseRepo()
        self.serializer = ModelSerializer
        self.identifier = 'id'
        self.query_dict = {}

    def get(self, request):
        id, keyword, *query_values = self.request(
            request
        ).opts(self.identifier, "keyword", *self.query_dict.values())
        
        filter_dict = dict(zip(self.query_dict.keys(), query_values))

        casted_dict = CleanDict(filter_dict)

        query_set = self.repo.filter_by_dict_or_keyword(
            casted_dict,
            keyword
        )
        many = True

        if id:
            query_set = self.repo.get_by_keyword({self.identifier: id})
            many = False 

        serialized_data = self.serializer(query_set, many=many)
         
        return self.responses.data_response(
            data = serialized_data.data
        )
    
    def activate_or_deactivate(self, request):
        id, = self.request(
            request=request,
            method="PUT"
        ).required(self.identifier)

        instance = self.repo.get_by_keyword({self.identifier: id})
        instance.is_active =  not instance.is_active
        instance.save()

        return self.responses.message_response(
            message="status changed successfully"
        )
