# casioplot-documentation
casioplot is a preinstalled micropython module on casio graphing calculators that support MicroPython.

# Functions
* [get_pixel()](https://github.com/P0pMan20/casioplot-documentation/blob/main/README.md#get_pixel)
* set_pixel()
* draw_string()
* show_screen()
* clear_screen()
 
 
 
 

## get_pixel(x,y)
#### Parameters
* x : x coordinate on screen
* y : y coordinate on screen

#### Returns
* Returns a tuple with the colour of the specified pixel, if value is off screen it returns None
 
Gets a pixel on the screen using (x, y) coordinates
 
#### Usage
```python
import casioplot

#Valid input

pixel_colour = casioplot.get_pixel(5, 10)
print(pixel_colour)

(255, 255, 255)

#Invalid input

pixel_colour = casioplot.get_pixel(2000, 2000)
print(pixel_colour)

None
```
