"""
The actual SVG object
"""
from collections import Sequence
from typing import Any, Dict, Iterable, Optional, Union
from xml.etree import ElementTree

from vectorvondoom import elements  # PathDescription needed for type
from vectorvondoom.elements import (
    Element, Elements, Circle, Line, Polygon, Polyline, Rect, Path
)
from vectorvondoom.geometry import HALF_PI, Point


__all__ = ['SVG', 'Circle', 'Line', 'Polyline', 'Polygon', 'Rect']


class SVG:
    """
    The actual SVG object
    """
    def __init__(
        self,
        width: Optional[int]=None,
        height: Optional[int]=None,
        background: Optional[str]=None,
        attributes: Optional[Dict[str, Any]]=None,
        root: Optional[ElementTree.Element]=None,
        offset: Optional[Point]=None,
        invert_y: Optional[bool]=False
    ) -> None:
        """
        size: The size of the viewbox.
        background: The background colour.
        attributes: Any other attributes to add to the root element.
        """
        if attributes is None:
            attributes = {}

        if width is not None and height is not None:
            attributes['viewBox'] = f'0 0 {width} {height}'

        if invert_y and height is None:
            raise ValueError("height must be given in order to invert y.")

        if background:
            attributes['style'] = f'background: {background}'

        if root is None:
            root = ElementTree.Element(
                'svg',
                xmlns="http://www.w3.org/2000/svg",
                version="1.1",
                attrib=self.format_attributes(attributes)
            )

        self._root = root
        self._offset = offset
        self._height = height
        self._invert_y = invert_y

    def circle(
        self, center: Point, radius: float, **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a circle
        """
        self.add(Circle.new(center, radius, **attributes))

    def rect(
        self, top_left: Point, width: float, height=float,
        **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a rectangle
        """
        self.add(Rect.new(top_left, width, height, **attributes))

    def rectangle(
        self, top_left: Point, bottom_right: Point,
        **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a rectangle
        """
        self.add(Rect.from_box(top_left, bottom_right, **attributes))

    def line(
        self, start: Point, end: Point,  **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a polylin
        """
        self.add(Line.new(start, end, **attributes))

    def polyline(
        self, points: Iterable[Point],  **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a polylin
        """
        self.add(Polyline.new(points, **attributes))

    def polygon(
        self, points: Iterable[Point],  **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a polygon
        """
        self.add(Polygon.new(points, **attributes))

    def path(
        self,
        *descriptions: elements.PathDescription,
        **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a path
        """
        self.add(Path(descriptions, attributes))

    def star(
        self, center: Point, length: int, num_points: int,
        rotation: float=-HALF_PI, ngram: bool=False,
        inner_length: Optional[int]=None,
        **attributes: Dict[str, Any]
    ) -> None:
        """
        Add a star.

        center: The center of the star.
        length: The length of each point.
        num_points: The number of points on the star.
        rotation: (optional, -π/2) The rotation of the star.
        ngram: (optional, False) Draw the star using n straight lines
            (e.g., make a pentagram)
        inner_length: (optional, None) How far from the center to
            connect each point. If ngram is True, this value is ignored.
            If not given, the ngram length will be used.
        """
        self.add(
            Elements.star(
                center, length, num_points, rotation, ngram, inner_length,
                **attributes
            )
        )

    def add_raw(
        self,
        tag: str,
        attributes: Dict[str, Any],
        text: Optional[str]=None
    ) -> None:
        """
        Write a raw element.
        """
        element = ElementTree.SubElement(
            self._root, tag, attrib=self.format_attributes(attributes)
        )

        if text is not None:
            element.text = text

    def add(self, element: Union[Element, Elements]) -> None:
        """
        Add an element to the SVG.
        """
        if self._offset:
            element = element.translate(self._offset)

        if self._invert_y:
            element = element.reflect(
                vertical=True, origin=Point(0, 0)
            ).translate(Point(0, self._height))

        if isinstance(element, Elements):
            tags = element.tags()
        else:
            tags = (element.tag(),)

        for tag in tags:
            self.add_raw(tag.name, tag.attributes)

    def offset(self, point: Point) -> 'SVG':
        """
        Create an SVG that draws to the same SVG, at an offset.
        """
        return SVG(
            root=self._root,
            offset=point,
            height=self._height,
            invert_y=self._invert_y,
        )

    def export(self) -> bytes:
        """
        Export the svg object to bytes.
        """
        return ElementTree.tostring(self._root)

    @classmethod
    def format(cls, value: Any) -> str:
        """
        Format an attribute value.
        """
        if hasattr(value, '__svg__'):
            return value.__svg__()
        elif isinstance(value, Sequence) and not isinstance(value, str):
            return ' '.join(cls.format(item) for item in value)
        elif isinstance(value, float):
            return '{:0.02f}'.format(value)

        return str(value)

    @classmethod
    def format_attributes(cls, attributes: Dict[str, Any]) -> Dict[str, str]:
        """
        Format an attribute dict.
        """
        return {
            key.replace('_', '-'): cls.format(value)
            for key, value in attributes.items()
        }
