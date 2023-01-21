from typing import Dict, List

from raw_decorator import for_all_methods, return_raw_value
from requestor import Requestor


@for_all_methods(return_raw_value)
class HejtoApi(object):

    def __init__(self) -> None:
        super().__init__()
        self.__requestor = Requestor()

    def get_posts(self, query_params: Dict[str, str] = None, **kwargs):
        response = self.__requestor.make_request(path_parts=["posts"], query_params=query_params)
        return response

    def get_post_details(self, slug: str, query_params: Dict[str, str] = None, **kwargs):
        return self.__requestor.make_request(path_parts=["posts", slug], query_params=query_params)

    def get_post_likes(self, slug: str, query_params: Dict[str, str] = None, **kwargs):
        return self.__requestor.make_request(path_parts=["posts", slug, 'likes'], query_params=query_params)

    def get_post_comments(self, slug: str, query_params: Dict[str, str] = None, **kwargs):
        return self.__requestor.make_request(path_parts=["posts", slug, 'comments'], query_params=query_params)

    def get_comment_details(self, slug: str, comment_id: str, query_params: Dict[str, str] = None, **kwargs):
        return self.__requestor.make_request(path_parts=["posts", slug, 'comments', comment_id], query_params=query_params)
