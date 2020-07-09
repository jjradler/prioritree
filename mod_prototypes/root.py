from .node import Node


class Root(Node):
    """
    .. class::Root
    .. desc::Singleton. If there is another Root in this Tree
    """
    def __init__(self):
        super().__init__()

    @property
    def _user_node(self):
        yield None

