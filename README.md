# gis-tools 
![python](https://img.shields.io/badge/python-3.7.1-green) 
![license](https://img.shields.io/github/license/alexeygribko/gis-tools)

This package contains some functions and presets for better GIS data processing with Python.
# Install
	pip install git+git://github.com/alexeygribko/gis-tools.git
# Use
```python
from gistools.geometry import *

# returns 45.0
angle(Point(0, 0), Point(1, 1), Point(1, 0))

# returns 'right'
which_side_line(LineString([(0, 0), (1, 1)]), Point(1, 0))

```
## License
	Copyright (c) 2018 The Python Packaging Authority
	
	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:
	
	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.
	
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.