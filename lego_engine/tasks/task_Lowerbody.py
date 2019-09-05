#!/usr/bin/env python
import numpy as np

# Labels: nothing:0, white:1, green:2, yellow:3, red:4, blue:5, black:6, unsure:7
bitmaps = [np.array([[5, 5, 5, 5]]),
           np.array([[4, 4, 4, 4],
                     [5, 5, 5, 5]]),
           np.array([[4, 4, 4, 4],
                     [5, 5, 5, 5],
                     [5, 0, 0, 0]]),
           np.array([[4, 4, 4, 4],
                     [5, 5, 5, 5],
                     [5, 0, 0, 5]]),
           np.array([[4, 0, 0, 0],
                     [4, 4, 4, 4],
                     [5, 5, 5, 5],
                     [5, 0, 0, 5]]),
           np.array([[4, 6, 0, 0],
                     [4, 4, 4, 4],
                     [5, 5, 5, 5],
                     [5, 0, 0, 5]]),
           np.array([[4, 6, 4, 4],
                     [4, 4, 4, 4],
                     [5, 5, 5, 5],
                     [5, 0, 0, 5]]),
           np.array([[0, 4, 6, 4, 4],
                     [0, 4, 4, 4, 4],
                     [0, 5, 5, 5, 5],
                     [0, 5, 0, 0, 5],
                     [5, 5, 0, 0, 0]]),
           np.array([[0, 4, 6, 4, 4],
                     [0, 4, 4, 4, 4],
                     [0, 5, 5, 5, 5],
                     [0, 5, 0, 0, 5],
                     [5, 5, 0, 5, 5]]),
          ]


