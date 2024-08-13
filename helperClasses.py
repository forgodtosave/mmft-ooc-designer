class Node():
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z
        self.channels = set()   # Channels, die diesen Node verwenden
        self.arcs = set()       # Arcs, die diesen Node verwenden
        self.quads = set()      # Quads um diesen Node herum

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
    @property
    def z(self) -> float:
        return self._z
        


class Channel():
    def __init__(self, node1: int, node2: int, width: float):
        self._node1 = node1
        self._node2 = node2
        self._width = width
        # hier dann z.b:
        # node1.channels.add(self)
        # node2.channels.add(self)

    @property
    def node1(self) -> int:
        return self._node1
    
    @property
    def node2(self) -> int:
        return self._node2
    
    @property
    def width(self) -> float:
        return self._width
       
        

class Arc():
    def __init__(self, node1: int, center: list, node2: int, width: float, direction: int):
        self._node1 = node1
        self._center = center
        self._node2 = node2
        self._width = width
        self._direction = direction
        # hier dann z.b:
        # start_node.arcs.add(self)
        # end_node.arcs.add(self)

    @property
    def node1(self) -> int:
        return self._node1
    
    @property
    def center(self) -> list:
        return self._center
    
    @property
    def node2(self) -> int:
        return self._node2
    
    @property
    def width(self) -> float:
        return self._width
    
    @property
    def direction(self) -> int:
        return self._direction
    
