from . import AsyncTestCase, read_fixture, AsyncContext

from notifier import zendesk
from notifier.model import *


class TestZendesk(AsyncTestCase):
    def setUp(self):
        super().setUp()
        self.client = zendesk.ZendeskDynamicContent({
            'zendesk.user': 'dummy_user',
            'zendesk.token': 'dummy_token',
            'zendesk.default_locale': 'fr'
        })
        self.coro(self.client.bootstrap())
        self.locales = {'fr': 16}

    def test_items(self):
        expected = [
            'dc.auto_reply_welcome_take_survey', 'dc.makro_password-change_password', 'dc.auto_reply_subject_line',
            'dc.notify_requester_of_comment_update', 'dc.makro_bug-force_close', 'dc.url_tutorial',
            'dc.auto_reply_check_tutorial', 'dc.makro_bug-sorry_about_the_migration_we_will_send_a_tool',
            'dc.url_survey'
        ]
        context = AsyncContext(context=self.make_response(read_fixture('zendesk_items.json')))
        self.mock_session_new.request.side_effect = iter([context])
        items = self.coro(self.client.items(self.locales))
        self.assertCountEqual(expected, items.keys())

    def test_items_pagination(self):
        expected = ['dc.auto_reply_update_to_latest_verson', 'dc.auto_reply_check_tutorial']
        zendesk_item_page_context = AsyncContext(context=self.make_response(read_fixture('zendesk_item_page.json')))
        zendesk_item_context = AsyncContext(context=self.make_response(read_fixture('zendesk_item.json')))
        self.mock_session_new.request.side_effect = iter([zendesk_item_page_context, zendesk_item_context])
        items = self.coro(self.client.items(self.locales))
        self.assertCountEqual(expected, items.keys())

    def test_item_variants(self):
        expected = {
            19: 70145,
            88: 109984,
            2: 33901,
            67: 59218,
            69: 59238,
            22: 532486,
            1: 33668,
            8: 34007,
            10: 75874,
            27: 85790,
            66: 54276
        }
        context = AsyncContext(context=self.make_response(read_fixture('zendesk_item.json')))
        self.mock_session_new.request.side_effect = iter([context])
        items = self.coro(self.client.items(self.locales))
        self.assertEqual(1, len(items))
        item = items['dc.auto_reply_update_to_latest_verson']
        self.assertEqual(expected, item.variants)

    def test_update(self):
        dc_item = DynamicContentItem('dummy_key', 'wti_id', ZendeskItem('zendesk_id', 'name', 'text', {16: 'item_id'}))
        translations = [WtiString('id', 'fr', 'text', 'STATUS', '2011-10-09 08:33:18 UTC', False)]
        self.coro(self.client.update(dc_item, translations, self.locales))
        self.mock_session_new.request.assert_called_with(
            'PUT',
            'https://keepsafe.zendesk.com/api/v2/dynamic_content/items/zendesk_id/variants/update_many.json',
            data='{"variants": [{"active": true, "content": "text",'
            ' "default": false, "id": "item_id", "locale_id": 16}]}',
            timeout=0)
