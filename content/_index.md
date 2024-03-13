---
# Leave the homepage title empty to use the site title
title: 
date: 2022-10-24
type: landing

sections:

  - block: slider
    content:
      slides:
        - title: 
          content: 
          align: left
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: team.jpg
              filters:
                brightness: 1
              fit: cover
            position: left
            color: '#666'
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      # Make the slides full screen within the browser window?
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 5000

  - block: collection
    content:
      title: Latest Publications
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
      page_type: publication
    design:
      view: citation
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Team members->" %}}
    design:
      columns: '1'
    
  - block: contact
    content:
      title: Contact
      text: |-
        Contact us:
      email: test@example.org
      phone: 888 888 88 88
      address:
        street: 5 Yiheyuan Road
        city: Beijing
        region: Haidian
        postcode: '100871'
        country: China
        country_code: CN
      coordinates:
        latitude: '39.9964'
        longitude: '116.3250'
      directions: Xin'ao Engineering Building Room 253
      autolink: true
    design:
      columns: '1'
---