#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sentry-wechat-webhook",
    version='0.0.6',
    author='linguofeng',
    author_email='linguofeng@msn.com',
    url='https://github.com/linguofeng/sentry-wechat-webhook',
    description=u'Sentry 企业微信 Webhook 插件',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry wechat webhook',
    include_package_data=True,
    zip_safe=False,
    packages=['wechat_webhook'],
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_wechat_webhook = wechat_webhook.plugin:WechatWebhookPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)
