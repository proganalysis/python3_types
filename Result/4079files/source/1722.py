from django.test import TestCase
from channels.tests import ChannelTestCase


# class MyTests(ChannelTestCase):
#     def test_a_thing(self):
#         # Add a test channel to a test group
#         Group("test-group").add("test-channel")
#         # Send to the group
#         Group("test-group").send({"value": 42})
#         # Verify the message got into the destination channel
#         result = self.get_next_message("test-channel", require=True)
#         self.assertEqual(result['value'], 42)
