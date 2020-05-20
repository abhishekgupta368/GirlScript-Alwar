from django.test import TestCase
from .models import TelegramGroup
from .models import WhattsappGroup
from .models import UserFeedback
from .models import UserEvent
from .models import UserEventImage
from .models import Schedule
from .models import Speaker
from .models import Team
from .models import TeamPosition

# Create your tests here.

# testing database.
class TelegramGroupTest(TestCase):
    def test_insert_data(self):
        TelegramGroup.objects.create(
                                group_name = "Alwar",
                                contact = "9087000556",
                                telegram_url="www.t.me"
                            )
        self.assertEqual(TelegramGroup.objects.count(), 1)

class WhattsappGroupTest(TestCase):
    def test_insert_data(self):
        WhattsappGroup.objects.create(
                                group_name = "Alwar",
                                contact = "9087000556",
                                whattsapp_url="www.t.me"
                            )
        self.assertEqual(WhattsappGroup.objects.count(), 1)


