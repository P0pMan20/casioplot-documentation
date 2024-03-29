# casioplot-documentation
casioplot is a preinstalled micropython module on casio graphing calculators that support MicroPython.
Such as the Casio fx-CG50

# Functions
* [get_pixel()](https://github.com/P0pMan20/casioplot-documentation/blob/main/README.md#get_pixelx-y)
* [set_pixel()](https://github.com/P0pMan20/casioplot-documentation/blob/main/README.md#set_pixelx-y-rgb0-0-0)
* [draw_string()](https://github.com/P0pMan20/casioplot-documentation/blob/main/README.md#draw_stringx-y-string-rgb0-0-0-text_sizemedium)
* [show_screen()](https://github.com/P0pMan20/casioplot-documentation/blob/main/README.md#show_screen)
* [clear_screen()](https://github.com/P0pMan20/casioplot-documentation/blob/main/README.md#clear_screen)
 

 

## get_pixel(x, y)
#### Parameters
* x : integer, x coordinate on screen
* y : integer, y coordinate on screen

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

## set_pixel(x, y, rgb=(0, 0, 0))
#### Parameters
* x : integer, x coordinate on screen
* y : integer, y coordinate on screen
* rgb : tuple, colour of pixel in RGB format



#### Returns
* None
 
Set a pixel in VRAM using (x, y) coordinates and RGB
 
#### Usage
```python
import casioplot

casioplot.set_pixel(20, 20, (255, 0, 0)) #sets the pixel at (20, 20) to red
casioplot.show_screen() #displays VRAM

```
![Set_Pixel_Example](/caps/Capt01.bmp)

## draw_string(x, y, string, rgb=(0, 0, 0), text_size='medium')
#### Parameters
* x : integer, x coordinate on screen (starting from upper left corner)
* y : integer, y coordinate on screen (starting from upper left corner)
* string : string, string to be displayed on the scrren
* rgb : tuple, colour of pixel in RGB format
* text_size : string, size of text, can be small, medium or large


#### Returns
* None
 
Draws a string into VRAM

#### Usage
```python
import casioplot

casioplot.draw_string(20, 20, "test_string", (255, 0, 0), "large") #draws a large red string starting at (20,20)
casioplot.show_screen() #displays VRAM

```
![Draw_String_Example](/caps/Capt02.bmp)

## show_screen()
#### Parameters
* None


#### Returns
* None
 
Displays the VRAM

#### Usage
```python
import casioplot

casioplot.set_pixel(20, 20, (255, 0, 0)) #sets the pixel at (20, 20) to red
casioplot.show_screen() #displays VRAM

```

## clear_screen()
#### Parameters
* None


#### Returns
* None
 
Clears the VRAM

#### Usage
```python
import casioplot

casioplot.set_pixel(20, 20, (255, 0, 0)) #sets the pixel at (20, 20) to red
casioplot.show_screen() #displays VRAM
casioplot.clear_screen() #clears VRAM
casioplot.set_pixel(20, 30, (0, 255, 0)) #sets the pixel at (20,30) to green
```
![Clear_Screen](/caps/Capt03.bmp)
