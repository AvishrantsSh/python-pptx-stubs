from pptx.oxml.shapes.autoshape import CT_Shape
from pptx.oxml.shapes.connector import CT_Connector
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectFrame
from pptx.oxml.shapes.groupshape import CT_GroupShape
from pptx.oxml.shapes.picture import CT_Picture

type ShapeElement = CT_Connector | CT_GraphicalObjectFrame | CT_GroupShape | CT_Picture | CT_Shape
