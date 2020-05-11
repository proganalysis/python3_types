# (generated with --quick)

from typing import Any, Dict, Type, Union

CL_AUTHDB: Any
CL_MOVIEDB: Any
CL_RATINGDB: Any
CL_RECOMMENDDB: Any
CL_URL: Any
CloudantDatabase: Any
Document: Any
app: Any
cloudant_client: Any
datetime: Type[datetime.datetime]
get_next_user_id: Any
json: module
os: module
requests: module
time: module
urllib: module

class MovieDAO:
    @staticmethod
    def find_movies(search_string) -> dict: ...
    @staticmethod
    def get_movie_names(movie_ids) -> Dict[int, Any]: ...

class RatingDAO:
    @staticmethod
    def get_ratings(user_id, movie_ids = ...) -> Dict[int, float]: ...
    @staticmethod
    def save_rating(movie_id, user_id, rating) -> None: ...

class RecommendationDAO:
    @staticmethod
    def get_latest_recommendation_timestamp() -> datetime.datetime: ...
    @staticmethod
    def get_recommendations_or_product_features(user_id) -> Dict[str, Union[str, Dict[int, float]]]: ...

class RecommendationsNotGeneratedException(Exception): ...

class RecommendationsNotGeneratedForUserException(Exception): ...

class UserDAO:
    @staticmethod
    def create_user(email, password_hash) -> Any: ...
    @staticmethod
    def find_by_email(email) -> Dict[str, Any]: ...
    @staticmethod
    def load_user(user_id) -> Dict[str, Any]: ...
