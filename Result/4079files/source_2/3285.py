import logging

from modules import Utils


def user_has_preferences(chatid: str) -> bool:
    """
    Checks
     if user exists in the preferences table

    :param chatid: The chatid of the user who will be tested
    :return: True if it exists, False if it doesn't exist
    """
    results = Utils.retrieve_query_results(f"SELECT * FROM PREFERENCES WHERE CHAT_ID={chatid}")
    if not results:
        return False
    else:
        return True


def add_user_to_preferences(chatid: str) -> None:
    """
    Add user to the preference table

    :param chatid: The chatid of the user who will be tested
    """
    Utils.exec_query(f"INSERT INTO PREFERENCES VALUES ('{chatid}', '1', '1')")
    logging.info(f'{chatid} has been added to preferences')


def remove_user_from_preferences(chatid: str) -> None:
    """
    Remove the chatid from the preference table

    :param chatid: The chatid of the user who will be removed
    """
    Utils.exec_query(f"DELETE FROM PREFERENCES WHERE CHAT_ID='{chatid}'")
    logging.info(f'{chatid} has been removed from preferences')


def update_link_preview_preference(chatid: str, value: bool) -> None:
    """
    Update the link_preview preference of the user

    :param chatid: The chatid of the user who will be tested
    :param value: The boolean value that will be converted to int and inserted in the table
    """
    if value:
        value = 1
    else:
        value = 0

    Utils.exec_query(f"UPDATE PREFERENCES SET LINK_PREVIEW='{value}' WHERE CHAT_ID='{chatid}'")


def get_user_link_preview_preference(chatid: str) -> bool:
    """
    Retrieve the link_preview preference of the user

    :param chatid: The chatid of the user who will be tested
    :return: The boolean value of the preference
    """
    if not user_has_preferences(chatid):
        add_user_to_preferences(chatid)

    results = Utils.retrieve_query_results(f"SELECT LINK_PREVIEW FROM PREFERENCES WHERE CHAT_ID={chatid}")
    if results[0][0] == 0:
        return False
    else:
        return True


def update_notifications_sound_preference(chatid: str, value: bool) -> None:
    """
    Update the notifications preference of the user

    :param chatid: The chatid of the user who will be tested
    :param value: The boolean value that will be converted to int and inserted in the table
    """
    if value:
        value = 1
    else:
        value = 0

    Utils.exec_query(f"UPDATE PREFERENCES SET NOTIFICATIONS_SOUND='{value}' WHERE CHAT_ID='{chatid}'")


def get_user_notifications_sound_preference(chatid: str) -> bool:
    """
    Retrieve the notifications preference of the user

    :param chatid: The chatid of the user who will be tested
    :return: The boolean value of the preference
    """
    if not user_has_preferences(chatid):
        add_user_to_preferences(chatid)

    results = Utils.retrieve_query_results(f"SELECT NOTIFICATIONS_SOUND FROM PREFERENCES WHERE CHAT_ID={chatid}")
    if results[0][0] == 0:
        return False
    else:
        return True
