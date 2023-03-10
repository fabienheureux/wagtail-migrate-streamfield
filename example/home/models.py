from django.db import models

from wagtail.models import Page
from wagtail.blocks import StreamBlock, StructBlock
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock


class ExtendedImageBlock(StructBlock):
    image = ImageChooserBlock()


class StoryBlock(StreamBlock):
    extended_image = ExtendedImageBlock()


class HomePage(Page):
    body = StreamField(StoryBlock(), use_json_field=True)

    content_panels = [FieldPanel("body")]
