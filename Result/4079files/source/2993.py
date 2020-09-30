# -*- coding: utf-8 -*-
# Copyright (c) 2016-present, CloudZero, Inc. All rights reserved.
# Licensed under the BSD-style license. See LICENSE file in the project root for full license information.

import requests_mock
from reactor.utils.slack import SlackWeb


def test_slack_message_no_webhook():
    slack = SlackWeb()
    result = slack.notify(msg="nothing")
    assert result is False


def test_slack_notify():
    """
    Send a slack message using a mocked Requests object
    """
    with requests_mock.Mocker() as m:
        url = "http://dummy.webhook.value.com"
        m.post(url, text='foobar')
        slack = SlackWeb(webhook_url=url)
        result = slack.notify(text="nothing to see here")
        assert result is True
        assert slack.response.text == 'foobar'


def test_slack_message():
    """
    Send a slack message using a mocked Requests object
    """
    expected_output1 = r'{"text": "*Test Message*", "mrkdwn": true, "attachments": [{"pretext": null, ' \
                       r'"color": "#36A646", "text": "Test content", "mrkdwn_in": ["text"]}]}'

    expected_output2 = r'{"text": "*Test Message*", "mrkdwn": true, "attachments": [{"pretext": "First:", ' \
                       r'"color": "#36A646", "text": "*foo*: bar\n*baz*: boom", "mrkdwn_in": ["text"]}, ' \
                       r'{"pretext": "Second:", "color": "#36A646", "text": "very interesting data", ' \
                       r'"mrkdwn_in": ["text"]}]}'

    with requests_mock.Mocker() as m:
        url = "http://dummy.webhook.value.com"
        m.post(url, text='foobar')
        slack = SlackWeb(webhook_url=url)
        result = slack.message(title='Test Message',
                               details='Test content')
        assert result is True
        assert slack.payload == expected_output1

        result = slack.message(title='Test Message',
                               details=[{"title": 'First:',
                                         "text": {'foo': "bar",
                                                  'baz': "boom"}},
                                        {"title": 'Second:',
                                         "text": "very interesting data"}])
        assert result is True
        assert slack.payload == expected_output2
