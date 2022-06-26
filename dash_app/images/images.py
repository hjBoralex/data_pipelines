# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:22:42 2022

@author: hermann.ngayap
"""
import dash
import dash_html_components as html
import base64

image_filename = 'C:/hjBoralex/etl/gitcwd/dash/assets/images/Boralex_2.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

boralex_logo = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image))
])