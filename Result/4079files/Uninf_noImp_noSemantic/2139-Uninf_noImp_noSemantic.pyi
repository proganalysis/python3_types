from typing import Any, Optional

class Database:
    bot: Any = ...
    conn: Any = ...
    DB_NAME: str = ...
    def __init__(self, bot: Optional[Any] = ...) -> None: ...
    def flag_gaming_channel(self, channel_id: Any, game_title: Any, allowed: Any) -> None: ...
    def get_flagged_games(self, channel_id: Any): ...
    def remove_flagged_games(self, channel_id: Any) -> None: ...
    def get_game_channel(self, title: Any): ...
    def insert_coins(self, userid: Any, coins: Any, mention: Optional[Any] = ...) -> None: ...
    def remove_coins(self, userid: Any, coins: Any, mention: Optional[Any] = ...) -> None: ...
    def get_coins(self, userid: Any): ...
    def get_top_coin_holders(self): ...
    def get_rich_users(self, botid: Any, wealthy_amount: Any): ...
    def add_music_to_db(self, link: Any) -> None: ...
    def get_random_music(self): ...