from django.shortcuts import render
from django.views import View

"""Use: ["get", "post", "put", "patch", "delete", "head", "options", "trace"]"""

try:
    from search.node import StackFrontier, Node, QueuedStackFrontier
except ImportError:
    pass


class NodeView(View):
    def get(self, request, *args, **kwargs):
        node = Node(
            parent=None,
            state={
                "explored": False,
            },
            action=None,
        )
        return render(request, "node_view.html", {"node": node})
