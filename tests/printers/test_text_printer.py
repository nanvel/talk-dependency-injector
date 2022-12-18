from datetime import datetime

import pytz
from pydantic.color import Color

from todopy.models import Priority, Task
from todopy.printers import TextPrinter


def test_text_printer():
    printer = TextPrinter(color=Color("black"))

    content = printer.call(
        task=Task(
            id=0,
            text="Lorem ipsum",
            time=datetime(2022, 1, 1, 1, 1).replace(tzinfo=pytz.utc),
            priority=Priority.LOW,
        )
    )

    assert content == "0: Lorem ipsum [0 2022-01-01 01:01:00+00:00]"
