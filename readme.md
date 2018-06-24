* document:https://docs.djangoproject.com/en/2.0/topics/templates/
* 常用语法 ：变量相关的用{{}}，逻辑相关的用{%%}
* Filters ：语法： {{ value|filter_name:参数 }}
** default: {{ test_default|default:"nothing"}}
** length: {{name_list|length}}
** filesizeformat: {{file_size|filesizeformat}}
** slice:  {{name_list|slice:"2:-1"}}
** date:   {{date|date:"Y-m-d H:i:s"}}
** safe:   {{script|safe}}
** truncatechars:  {{script|truncatechars:10}}
