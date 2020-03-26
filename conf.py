# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "stayrea/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "StayreoのBlog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Stayreo"
email = "stayrea@gmail.com"
author_homepage = "https:/github.com/stayrea"
description = "Valar Morghulis"
key_words = ['stayrea', 'Valar Morghulis', 'stayreo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "Valar Morghulis."
    },
    {
        "name": "",
        "url": "https://stayrea.github.io/Blog-With-GitHub-Boilerplate/",
        "brief": "Stayreo の Blog"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}"豆瓣
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "豆瓣",
        "url": "https://www.douban.com/people//",
        "icon": "gi gi-douban"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
