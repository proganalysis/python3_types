from cloudant.database import CloudantDatabase as CloudantDatabase
from datetime import datetime
from typing import Any, Dict, List, Optional

CL_URL: Any
CL_MOVIEDB: Any
CL_AUTHDB: Any
CL_RATINGDB: Any
CL_RECOMMENDDB: Any

class RecommendationsNotGeneratedException(Exception): ...
class RecommendationsNotGeneratedForUserException(Exception): ...

class MovieDAO:
    @staticmethod
    def get_movie_names(movie_ids: List[int]) -> Dict[int, str]: ...
    @staticmethod
    def find_movies(search_string: str) -> Dict[int, str]: ...

class RatingDAO:
    @staticmethod
    def get_ratings(user_id: str, movie_ids: List[int]=...) -> Dict[int, float]: ...
    @staticmethod
    def save_rating(movie_id: int, user_id: str, rating: Optional[float]) -> Any: ...

class RecommendationDAO:
    @staticmethod
    def get_latest_recommendation_timestamp() -> datetime: ...
    @staticmethod
    def get_recommendations_or_product_features(user_id: str) -> Dict: ...

class UserDAO:
    @staticmethod
    def load_user(user_id: str) -> Dict[str, str]: ...
    @staticmethod
    def find_by_email(email: str) -> Dict[str, str]: ...
    @staticmethod
    def create_user(email: str, password_hash: str) -> str: ...
