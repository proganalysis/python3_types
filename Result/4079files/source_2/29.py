"""
Tests for the SVG class.
"""
from xml.etree import ElementTree

from nose.tools import assert_equals, assert_raises


def test_svg():
    """
    The SVG class
    """
    from vectorvondoom.elements import Circle, Elements, Polygon
    from vectorvondoom.geometry import Point
    from vectorvondoom.svg import SVG

    svg = SVG(100, 50, background='#696969')

    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    assert_equals(root.getchildren(), [])

    svg.add(Circle.new(Point(50, 25), 25))
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(children[0].attrib, {'cx': '50', 'cy': '25', 'r': '25'})

    svg.add(
        Circle.new(
            Point(15, 10), 5, stroke='black', fill='white', stroke_width=2
        )
    )
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 2)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(children[0].attrib, {'cx': '50', 'cy': '25', 'r': '25'})
    assert_equals(children[1].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(
        children[1].attrib,
        {
            'cx': '15', 'cy': '10', 'r': '5',
            'stroke': 'black', 'fill': 'white', 'stroke-width': '2'
        }
    )

    svg.add(Polygon.new(
        (Point(0, 0), Point(2, 0), Point(1, 2)), stroke_width=1)
    )
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 3)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(children[0].attrib, {'cx': '50', 'cy': '25', 'r': '25'})
    assert_equals(children[1].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(
        children[1].attrib,
        {
            'cx': '15', 'cy': '10', 'r': '5',
            'stroke': 'black', 'fill': 'white', 'stroke-width': '2'
        }
    )
    assert_equals(children[2].tag, '{http://www.w3.org/2000/svg}polygon')
    assert_equals(
        children[2].attrib,
        {
            'points': '0.00 0.00 2.00 0.00 1.00 2.00',
            'stroke-width': '1'
        }
    )

    svg.add_raw(
        'text',
        {
            'x': 0, 'y': 100,
            'font-size': 12, 'font-family': "Verdana",
        },
        text="Hello World"
    )
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 4)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(children[0].attrib, {'cx': '50', 'cy': '25', 'r': '25'})
    assert_equals(children[1].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(
        children[1].attrib,
        {
            'cx': '15', 'cy': '10', 'r': '5',
            'stroke': 'black', 'fill': 'white', 'stroke-width': '2'
        }
    )
    assert_equals(children[2].tag, '{http://www.w3.org/2000/svg}polygon')
    assert_equals(
        children[2].attrib,
        {
            'points': '0.00 0.00 2.00 0.00 1.00 2.00',
            'stroke-width': '1'
        }
    )
    assert_equals(children[3].tag, '{http://www.w3.org/2000/svg}text')
    assert_equals(
        children[3].attrib,
        {
            'x': '0', 'y': '100',
            'font-size': '12', 'font-family': "Verdana",
        }
    )
    assert_equals(children[3].text, 'Hello World')

    sub_svg = svg.offset(Point(-1, 1))
    sub_svg.add(Polygon.new(
        (Point(0, 0), Point(2, 0), Point(1, 2)), stroke_width=1)
    )
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 5)
    assert_equals(children[4].tag, '{http://www.w3.org/2000/svg}polygon')
    assert_equals(
        children[4].attrib,
        {
            'points': '-1.00 1.00 1.00 1.00 0.00 3.00',
            'stroke-width': '1'
        }
    )

    svg = SVG(100, 50, background='#696969')
    svg.add(
        Elements.new(
            Circle.new(Point(50, 25), 25),
            Circle.new(
                Point(15, 10), 5, stroke='black', fill='white', stroke_width=2
            )
        ),
    )
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 2)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(children[0].attrib, {'cx': '50', 'cy': '25', 'r': '25'})
    assert_equals(children[1].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(
        children[1].attrib,
        {
            'cx': '15', 'cy': '10', 'r': '5',
            'stroke': 'black', 'fill': 'white', 'stroke-width': '2'
        }
    )

    svg = SVG(50, 50, background='#696969')
    svg.star(Point(25, 25), 25, 5, ngram=True)
    svg.add(Elements.star(Point(25, 25), 25, 5, ngram=True))
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 50 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 2)
    assert_equals(children[0].tag, children[1].tag)
    assert_equals(children[0].attrib, children[1].attrib)


def test_invert():
    """
    Inverted SVG elements
    """
    from vectorvondoom.svg import Point, SVG

    svg = SVG(100, 50, background='#696969', invert_y=True)
    svg.line(Point(0, 0), Point(1, 2), stroke_width=1)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}line')
    assert_equals(
        children[0].attrib,
        {
            'x1': '0', 'y1': '50',
            'x2': '1', 'y2': '48',
            'stroke-width': '1'
        }
    )

    svg = SVG(100, 50, background='#696969', invert_y=True).offset(Point(5, 3))
    svg.line(Point(0, 0), Point(1, 2), stroke_width=1)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}line')
    assert_equals(
        children[0].attrib,
        {
            'x1': '5', 'y1': '47',
            'x2': '6', 'y2': '45',
            'stroke-width': '1'
        }
    )

    with assert_raises(ValueError):
        svg = SVG(background='#696969', invert_y=True)


def test_shortcuts():
    """
    SVG shortcut elements
    """
    from vectorvondoom.elements import MoveTo, LineTo, ClosePath
    from vectorvondoom.geometry import Point
    from vectorvondoom.svg import SVG

    svg = SVG(100, 50, background='#696969')
    svg.circle(Point(50, 25), 25)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}circle')
    assert_equals(children[0].attrib, {'cx': '50', 'cy': '25', 'r': '25'})

    svg = SVG(100, 50, background='#696969')
    svg.rect(Point(50, 25), 5, 10)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}rect')
    assert_equals(
        children[0].attrib,
        {'x': '50.00', 'y': '25.00', 'width': '5.00', 'height': '10.00'}
    )

    svg = SVG(100, 50, background='#696969')
    svg.rectangle(Point(50, 25), Point(55, 35))
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}rect')
    assert_equals(
        children[0].attrib,
        {'x': '50.00', 'y': '25.00', 'width': '5.00', 'height': '10.00'}
    )

    svg = SVG(100, 50, background='#696969')
    svg.line(Point(0, 0), Point(1, 2), stroke_width=1)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}line')
    assert_equals(
        children[0].attrib,
        {
            'x1': '0', 'y1': '0',
            'x2': '1', 'y2': '2',
            'stroke-width': '1'
        }
    )

    svg = SVG(100, 50, background='#696969')
    svg.polyline((Point(0, 0), Point(2, 0), Point(1, 2)), stroke_width=1)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}polyline')
    assert_equals(
        children[0].attrib,
        {
            'points': '0.00 0.00 2.00 0.00 1.00 2.00',
            'stroke-width': '1'
        }
    )

    svg = SVG(100, 50, background='#696969')
    svg.polygon((Point(0, 0), Point(2, 0), Point(1, 2)), stroke_width=1)
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}polygon')
    assert_equals(
        children[0].attrib,
        {
            'points': '0.00 0.00 2.00 0.00 1.00 2.00',
            'stroke-width': '1'
        }
    )

    svg = SVG(100, 50, background='#696969')
    svg.path(
        MoveTo(Point(3, 3), True),
        LineTo(Point(0, -3), True),
        LineTo(Point(-3, 0), True),
        LineTo(Point(0, 3)),
        ClosePath(),
        stroke_width=1
    )
    root = ElementTree.fromstring(svg.export())
    assert_equals(root.tag, '{http://www.w3.org/2000/svg}svg')
    assert_equals(
        root.attrib, {
            'version': '1.1',
            'viewBox': '0 0 100 50',
            'style': 'background: #696969'
        }
    )
    children = root.getchildren()
    assert_equals(len(children), 1)
    assert_equals(children[0].tag, '{http://www.w3.org/2000/svg}path')
    assert_equals(
        children[0].attrib,
        {
            'd': 'm 3.00 3.00 v -3.00 h -3.00 L 0.00 3.00 z',
            'stroke-width': '1'
        }
    )
