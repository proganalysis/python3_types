from typing import Any

RECIPIENTS: Any
pytestmark: Any

async def test_sendmail_multiple_times_in_sequence(smtp_client: Any, smtpd_server: Any, message: Any) -> None: ...
async def test_sendmail_multiple_times_with_gather(smtp_client: Any, smtpd_server: Any, message: Any) -> None: ...
async def test_connect_and_sendmail_multiple_times_with_gather(smtpd_server: Any, hostname: Any, port: Any, message: Any): ...
async def test_multiple_clients_with_gather(smtpd_server: Any, hostname: Any, port: Any, message: Any): ...
async def test_multiple_actions_in_context_manager_with_gather(smtpd_server: Any, hostname: Any, port: Any, message: Any): ...
async def test_many_commands_with_gather(monkeypatch: Any, smtp_client: Any, smtpd_server: Any, smtpd_class: Any, smtpd_response_handler_factory: Any) -> None: ...
async def test_close_works_on_stopped_loop(smtpd_server: Any, event_loop: Any, hostname: Any, port: Any) -> None: ...
async def test_context_manager_entry_multiple_times_with_gather(smtpd_server: Any, smtp_client: Any, message: Any): ...
