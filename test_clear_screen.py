import casioplot

casioplot.set_pixel(20, 20, (255, 0, 0)) #sets the pixel at (20, 20) to red
casioplot.show_screen() #displays VRAM
casioplot.clear_screen() #clears VRAM
casioplot.set_pixel(20, 30, (0, 255, 0)) #sets the pixel at (20,30) to green

#If it works a tiny green pixel should be displayed in the middle left of your screen