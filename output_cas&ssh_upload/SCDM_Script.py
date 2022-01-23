#SCDM_Script 
# Python Script, API Version = V17
#ClearAll()	
#d=0.7              #change by main
a=round(0.5*(29.92-3.1415926*d),2)
# Set Sketch Plane
sectionPlane = Plane.PlaneYZ
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Sketch Rectangle #three xy point of centre rectangle of throat
point1 = Point2D.Create(MM(-d/2),MM(a/2))
point2 = Point2D.Create(MM(d/2),MM(a/2))
point3 = Point2D.Create(MM(d/2),MM(-a/2))
result = SketchRectangle.Create(point1, point2, point3)
# EndBlock

# Create Sweep Arc #left arc of throat
origin = Point2D.Create(MM(0), MM(-a/2))
start = Point2D.Create(MM(d/2), MM(-a/2))
end = Point2D.Create(MM(-d/2), MM(-a/2))
senseClockWise = True
result = SketchArc.CreateSweepArc(origin, start, end, senseClockWise)
# EndBlock

# Create Sweep Arc #right arc of throat
origin = Point2D.Create(MM(0), MM(a/2))
start = Point2D.Create(MM(-d/2), MM(a/2))
end = Point2D.Create(MM(d/2), MM(a/2))
senseClockWise = True
result = SketchArc.CreateSweepArc(origin, start, end, senseClockWise)
# EndBlock

# Trim Sketch Curve
curveSelPoint = SelectionPoint.Create(GetRootPart().Curves[2], 0.000260933859799905)
result = TrimSketchCurve.Execute(curveSelPoint)
# EndBlock

# Trim Sketch Curve
curveSelPoint = SelectionPoint.Create(GetRootPart().Curves[0], 0.000195073679892822)
result = TrimSketchCurve.Execute(curveSelPoint)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Extrude 1 Face
selection = Selection.Create(GetRootPart().Bodies[0].Faces[0])
options = ExtrudeFaceOptions()
options.ExtrudeType = ExtrudeType.Cut
result = ExtrudeFaces.Execute(selection, MM(-8), options) #left length of throat
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().Bodies[0].Faces[5])
result = DatumPlaneCreator.Create(selection, False, None)
# EndBlock

# Translate Along Z Handle
selection = Selection.Create(GetRootPart().DatumPlanes[0])
direction = Move.GetDirection(selection)
options = MoveOptions()
result = Move.Translate(selection, direction, MM(-18), options)
# EndBlock

# Set Sketch Plane
sectionPlane = Plane.Create(Frame.Create(Point.Create(MM(-18), MM(0), MM(0)),  #left plane of slope
    Direction.DirY, 
    Direction.DirZ))
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Sketch Circle
origin = Point2D.Create(MM(0), MM(0))
result = SketchCircle.Create(origin, MM(4.7625)) #Radius of inner tube
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Extrude 1 Face
selection = Selection.Create(GetRootPart().Bodies[1].Faces[0])
options = ExtrudeFaceOptions()
options.ExtrudeType = ExtrudeType.Cut
result = ExtrudeFaces.Execute(selection, MM(-95.25), options) #length of inner tube
# EndBlock

# Create Blend
selection = Selection.Create([GetRootPart().Bodies[1].Faces[2],
    GetRootPart().Bodies[0].Faces[4]])
options = LoftOptions()
options.GeometryCommandOptions = GeometryCommandOptions()
result = Loft.Create(selection, None, options)
# EndBlock

# Mirror
selection = Selection.Create(GetRootPart().Bodies[0])
mirrorPlane = Selection.Create(GetRootPart().Bodies[0].Faces[8])
options = MirrorOptions()
result = Mirror.Execute(selection, mirrorPlane, options, None)
# EndBlock

# Create Volume
selection = Selection.Create(GetRootPart().Bodies[0].Edges[16])
secondarySelection = Selection()
result = VolumeExtract.Create(selection, secondarySelection)
# EndBlock

# Delete Objects
selection = Selection.Create(GetRootPart().Components[0].Content.Bodies[0])
result = Delete.Execute(selection)
# EndBlock

# Split Faces
options = SplitFaceOptions()
selection = Selection.Create(GetRootPart().Bodies[0].Faces[10])
point = Selection.Create(GetRootPart().Bodies[0].Faces[10]).Items[0].EvalProportion(0.5, 0.7).Point
result = SplitFace.Execute(selection, point, FaceSplitType.UV, options)
# EndBlock

# Create Named Selection Group
primarySelection = Selection.Create(GetRootPart().Bodies[0].Faces[9])
secondarySelection = Selection()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "inlet")
# EndBlock

# Create Named Selection Group
primarySelection = Selection.Create(GetRootPart().Bodies[0].Faces[10])
secondarySelection = Selection()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "outlet")
# EndBlock