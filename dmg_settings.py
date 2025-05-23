# DMG settings for Flanepy
volume_name = "Flanepy"
format = "UDZO"
size = "100M"
files = ["dist/Flanepy.app"]
symlinks = {"Applications": "/Applications"}
icon_locations = {
    "Flanepy.app": (140, 120),
    "Applications": (500, 120)
}
background = None  # You can add a background image path here if you have one
window_rect = ((100, 100), (640, 280)) 