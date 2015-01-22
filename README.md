# Responsive content types for FeinCMS
This [Django](http://www.djangoproject.com) package allows you to create responsive content types with [FeinCMS](http://feincms.org/). 
It allows users to select the number of columns they want for small, medium of large screens, per content type.
These contenttypes are wrapped in divs, containing the corresponding [Foundation](http://foundation.zurb.com/) classes.

## Installation
Use pip to install the package
```
$ pip install responsive_content_type
```    
In your Django settings, add responsive_content_type to the INSTALLED_APPS
```
INSTALLED_APPS = (
    ...
    'responsive_content_type',
    ...
)
```
## Usage
To create a responsive content type, simpy import the ResponsiveContentType class and extend it.
Next, in your templates folder, create a folder called content, containing the template for this content type.
This package will handle the rest.

Example:
``` python
# models.py
from django.db import models
from responsive_content_type.models import ResponsiveContentType


class Paragraph(ResponsiveContentType):
    text = models.CharField(_('Text'), max_length=200)
    
    class Meta:
        abstract = True
```

``` html
<!-- templates/content/paragraph.html -->
<p>
    {{ content.text }}
</p>
```


## To do
* Make Python 3 compatible
* Add Bootstrap support
