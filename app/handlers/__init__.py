from .route import route_api
from .video_handler import video_api
from .interval_handler import interval_api

blueprints = [
    route_api,
    video_api,
    interval_api,
]

