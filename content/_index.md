---
# Leave the homepage title empty to use the site title
title: 开放热学实验室-中文简介
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        开放热学实验室
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        描述
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="团队成员" %}}
    design:
      columns: '1'
---