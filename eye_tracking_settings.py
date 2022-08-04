from talon import app
from talon.track.geom import Point2d
from talon_plugins import speech, eye_mouse, eye_zoom_mouse

if app.platform == "mac":
    eye_zoom_mouse.config.screen_area = Point2d(300, 175)
    eye_zoom_mouse.config.img_scale = 3 
# elif app.platform == "windows":
#     eye_zoom_mouse.config.screen_area = Point2d(200, 150)
#     eye_zoom_mouse.config.img_scale = 4.5

