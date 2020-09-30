# (generated with --quick)

from typing import Any, Dict, List, Optional, Type

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
    def find_movies(search_string: str) -> Dict[int, str]: ...
    @staticmethod
    def get_movie_names(movie_ids: List[int]) -> Dict[int, str]: ...

class RatingDAO:
    @staticmethod
    def get_ratings(user_id: str, movie_ids: Optional[List[int]] = ...) -> Dict[int, float]: ...
    @staticmethod
    def save_rating(movie_id: int, user_id: str, rating: Optional[float]) -> None: ...

class RecommendationDAO:
    @staticmethod
    def get_latest_recommendation_timestamp() -> datetime.datetime: ...
    @staticmethod
    def get_recommendations_or_product_features(user_id: str) -> dict: ...

class RecommendationsNotGeneratedException(Exception): ...

class RecommendationsNotGeneratedForUserException(Exception): ...

class UserDAO:
    @staticmethod
    def create_user(email: str, password_hash: str) -> str: ...
    @staticmethod
    def find_by_email(email: str) -> Dict[str, str]: ...
    @staticmethod
    def load_user(user_id: str) -> Dict[str, str]: ...
