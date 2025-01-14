# -*- coding: utf-8 -*-

import cairo
import math
import random

def draw_background(ctx, r, g, b, width, height):
    ctx.set_source_rgb(r, g, b)
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

canvas = (600,600)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas[0], canvas[1])
ctx = cairo.Context(surface)
draw_background(ctx, 1, 1, 1, canvas[0], canvas[1])


w, h = 600, 600

subdivisions = 5000

# Not too small
min_diff = 80

# Space between quads
sep = 1

# Piet Mondrian Color Palette
colors = [(38, 71, 124), (240, 217, 92), (162, 45, 40), (223, 224, 236), (223, 224, 236), (223, 224, 236), (223, 224, 236), (223, 224, 236)]

# Subdivision adjustment
splits = [.5, 1, 1.5]

# Canvas Border
edge = 8

def setup():
    #size(w, h)
    #pixelDensity(2)
    
    #background(255)

    quads = []
    # Add the initial rectangle
    quads.append([(edge, edge), (w - edge, edge), (w - edge, h - edge), (edge, h - edge)])
    
    # Start splitting things up
    for i in range(subdivisions):
        q_index = random.choices(range(len(quads)))
        q = quads[int(q_index[0])]
        q_lx = q[0][0]
        q_rx = q[1][0]
        q_ty = q[0][1]
        q_by = q[2][1]
   
        s = splits[int(random.choice(range(len(splits))))]
        if (random.random() < .5):
            if ((q_rx - q_lx) > min_diff):
                # Get new shapes x value (y is same)
                x_split = (q_rx - q_lx)/2 * s + q_lx
                
                quads.pop(q_index[0])
                quads.append([(q_lx, q_ty), (x_split - sep, q_ty), (x_split - sep, q_by), (q_lx, q_by)])
                quads.append([(x_split + sep, q_ty), (q_rx, q_ty), (q_rx, q_by), (x_split + sep, q_by)])
            
        else:
            if ((q_by - q_ty) > min_diff):
                y_split = (q_by - q_ty)/2 * s + q_ty
                
                quads.pop(q_index[0])
                quads.append([(q_lx, q_ty), (q_rx, q_ty), (q_rx, y_split - sep), (q_lx, y_split - sep)])
                quads.append([(q_lx, y_split + sep), (q_rx, y_split + sep), (q_rx, q_by), (q_lx, q_by)])
    return quads

def draw_retangles(ctx, quads, line_width):
    for quad in quads:
        ctx.move_to(quad[0][0], quad[0][1])
        ctx.line_to(quad[1][0], quad[1][1])
        ctx.line_to(quad[2][0], quad[2][1])
        ctx.line_to(quad[3][0], quad[3][1])
        ctx.close_path()

        color = random.choice(colors)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255)
        ctx.fill_preserve()

        ctx.set_source_rgba(0, 0, 0)
        ctx.set_line_width(line_width)
        ctx.stroke()
        
        
if __name__ == "__main__":
    quads = setup()
    draw_retangles(ctx, quads, 2)
    surface.write_to_png("test.png")
