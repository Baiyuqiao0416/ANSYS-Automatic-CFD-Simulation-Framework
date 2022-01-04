#MESH_Script 
#d change by main
#ParallelCPU change by main
#region Details View Action
#mesh1 = Model.Mesh   #new by main
mesh1.ElementSize = Quantity(0.35, "mm")
#endregion

#region Details View Action
mesh1.UseAutomaticInflation = 1
#endregion

#region Details View Action
#mesh1.NumberOfCPUsForParallelPartMeshing = NumberOfProcessors
#endregion
#throat
#region Context Menu Action
throat_sizing = mesh1.AddSizing()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [52, 36, 18, 21, 53, 39, 20, 54, 38, 19, 55, 37]
throat_sizing.Location = selection
#endregion

#region Details View Action
throat_sizing.ElementSize = Quantity(0.075*d, "mm")
#endregion
#out tube
#region Context Menu Action
out_tube_sizing = mesh1.AddSizing()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [10]
out_tube_sizing.Location = selection
#endregion

#region Details View Action
out_tube_sizing.ElementSize = Quantity(0.2*d, "mm")
#endregion

#region Context Menu Action
mesh1.GenerateMesh()
#endregion

