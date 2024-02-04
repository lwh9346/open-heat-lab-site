---
# Leave the homepage title empty to use the site title
title: Education
date: 2024-1-30
type: landing

sections:
  - block: slider
    content:
      slides:
        - title: Image1
          content: This is image1
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: coders.jpg
              filters:
                brightness: 1
            position: left
            color: '#666'
        - title: Image2
          content: This is image2
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: contact.jpg
              filters:
                brightness: 1
            position: center
            color: '#555'
        - title: Image3
          content: This is image3
          align: right
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: welcome.jpg
              filters:
                brightness: 1
            position: center
            color: '#333'
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      # Make the slides full screen within the browser window?
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000
---