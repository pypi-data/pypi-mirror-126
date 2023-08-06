# Blur Image
A library to blurring images.
# Install
```
pip3 install blur-image
```
# Using
```python
from blur_image import blur
# blur(source, output, mode = "simple")
# Modes: simple, box, gaussian
# Value is available for this modes: box, gaussian
blur("source.png", "blurred_source.png")
```