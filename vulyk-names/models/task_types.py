# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from vulyk.models.task_types import AbstractTaskType

from vulyk_names.models.tasks import (
    NamesAnswer, NamesTask)


class NamesTaskType(AbstractTaskType):
    """
    Names Task to work with Vulyk.
    """

    answer_model = NamesAnswer
    task_model = NamesTask

    name = "Аналіз імен та зв'язків між ними"
    description = ''

    template = 'base.html'
    helptext_template = 'help.html'
    type_name = 'names_task'

    redundancy = 2

    JS_ASSETS = ['static/scripts/handlebars.js',
                 'static/scripts/jquery.serializejson.js',
                 'static/scripts/base.js', ]

    CSS_ASSETS = ['static/styles/bootstrap-social.css',
                  'static/styles/base.css', ]
