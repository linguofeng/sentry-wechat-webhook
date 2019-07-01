# coding: utf-8
import json
import requests

from django import forms
from sentry.plugins.bases import notify

WECHAT_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"

class WechatWebhookOptionsForm(notify.NotificationConfigurationForm):
    key = forms.CharField(
        max_length=255,
        help_text='Wechat webhook key'
    )

class WechatWebhookPlugin(notify.NotificationPlugin):
    author = 'linguofeng'
    author_url = 'https://github.com/linguofeng/sentry-wechat-webhook'
    version = '0.0.6'
    description = u'Sentry 企业微信 Webhook 插件'
    resource_links = [
        ('Source', 'https://github.com/linguofeng/sentry-wechat-webhook'),
        ('Bug Tracker', 'https://github.com/linguofeng/sentry-wechat-webhook/issues'),
        ('README', 'https://github.com/linguofeng/sentry-wechat-webhook/blob/master/README.md'),
    ]

    slug = 'wechat_webhook'
    title = 'Wechat Webhook'
    conf_key = slug
    conf_title = title
    project_conf_form = WechatWebhookOptionsForm

    def is_configured(self, project, **kwargs):
        return bool(self.get_option('key', project))

    def notify_users(self, group, event, fail_silently=False, **kwargs):
        key = self.get_option('key', group.project)
        url = WECHAT_WEBHOOK_URL.format(key=key)
        title = u"有新的通知来自 {} 项目".format(event.project.slug)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": u"#### {title} \n > {message} [查看]({url})".format(
                    title=title,
                    message=event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.id),
                )
            }
        }
        requests.post(
            url=url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )