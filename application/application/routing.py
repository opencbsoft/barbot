from channels.routing import route

channel_routing = [
    route("http.request", "application.core.consumer"),
]