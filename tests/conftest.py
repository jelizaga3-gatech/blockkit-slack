from collections import namedtuple

import pytest

from blockkit import (
    Button,
    Confirm,
    Image,
    MarkdownText,
    Option,
    OptionGroup,
    PlainText,
    Filter,
)

TestValues = namedtuple(
    "TestValues",
    (
        "title text short_text image_url alt_text url deep_link "
        "action_id block_id confirm_text deny_text value date"
    ),
)


@pytest.fixture
def values():
    return TestValues(
        title="Bot thought",
        text="The way to get started is to quit _talking_ and begin *doing*",
        short_text="Do it well",
        image_url="http://placekitten.com/200/200",
        alt_text="There is a kitten",
        url="https://example.com",
        deep_link="slack://user?team=T3Y4A0MNW&id=UF7CU4UKZ",
        action_id="test_action_id",
        block_id="text_block_id",
        confirm_text="Confirm",
        deny_text="Deny",
        value="value",
        date="2019-12-08",
    )


@pytest.fixture
def markdown_text(values):
    return MarkdownText(values.text)


@pytest.fixture
def short_text(values):
    return PlainText(values.short_text)


@pytest.fixture
def plain_text(values):
    return PlainText(values.text)


@pytest.fixture
def modal_text(values):
    return PlainText("Action")


@pytest.fixture
def button(plain_text, values):
    return Button(plain_text, values.action_id)


@pytest.fixture
def image(values):
    return Image(values.image_url, alt_text=values.text)


@pytest.fixture
def confirm(values, plain_text, markdown_text):
    return Confirm(
        plain_text,
        markdown_text,
        PlainText(values.confirm_text),
        PlainText(values.deny_text),
    )


@pytest.fixture
def option(values, plain_text):
    return Option(plain_text, values.value)


@pytest.fixture
def option_group(values, plain_text, option):
    return OptionGroup(plain_text, [option for _ in range(2)])


@pytest.fixture
def required_option(request, option, option_group):
    return {"option": option, "option_group": option_group}[request.param]


@pytest.fixture
def filter_object():
    return Filter(
        include=["im", "mpim", "private", "public"],
        exclude_external_shared_channels=False,
        exclude_bot_users=True,
    )
