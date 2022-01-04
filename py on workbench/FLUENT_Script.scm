/file/set-tui-version "19.4"
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Laminar)"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Laminar)"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (Laminar)"))
(cx-gui-do cx-set-toggle-button2 "Viscous Model*Table1*ToggleBox1(Model)*k-omega (2 eqn)" #t)
(cx-gui-do cx-activate-item "Viscous Model*Table1*ToggleBox1(Model)*k-omega (2 eqn)")
(cx-gui-do cx-set-toggle-button2 "Viscous Model*Table1*ToggleBox7(k-omega Model)*SST" #t)
(cx-gui-do cx-activate-item "Viscous Model*Table1*ToggleBox7(k-omega Model)*SST")
(cx-gui-do cx-activate-item "Viscous Model*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Models|Viscous (SST k-omega)"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|air"))
(cx-gui-do cx-activate-item "Create/Edit Materials*Table1*Frame1*Frame2*ButtonBox2*PushButton2(User-Defined Database)")
material database dir
(cx-gui-do cx-activate-item "Open Database*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-set-list-selections "User-Defined Database Materials*Table1*Frame1*List1(Materials)" '( 0))
(cx-gui-do cx-activate-item "User-Defined Database Materials*Table1*Frame1*List1(Materials)")
(cx-gui-do cx-activate-item "User-Defined Database Materials*PanelButtons*PushButton6(Copy)")
(cx-gui-do cx-activate-item "User-Defined Database Materials*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Cell Zone Conditions|fff___ (fluid, id=3)"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Cell Zone Conditions|fff___ (fluid, id=3)"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Cell Zone Conditions|fff___ (fluid, id=3)"))
(cx-gui-do cx-set-list-selections "Fluid*Table2*Table1*DropDownList1(Material Name)" '( 0))
(cx-gui-do cx-activate-item "Fluid*Table2*Table1*DropDownList1(Material Name)")
(cx-gui-do cx-activate-item "Fluid*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|blood"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|_1 (wall, id=6)"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|_1 (wall, id=6)"))
(cx-gui-do cx-list-tree-right-click "NavigationPane*List_Tree1" )
(cx-gui-do cx-activate-item "MenuBar*TypeSubMenu*mass-flow-inlet")
(cx-gui-do cx-set-expression-entry "Mass-Flow Inlet*Frame3*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Mass Flow Rate)" '("0.1055" . 0))
(cx-gui-do cx-set-list-selections "Mass-Flow Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList15(Direction Specification Method)" '( 1))
(cx-gui-do cx-activate-item "Mass-Flow Inlet*Frame3*Frame1(Momentum)*Table1*DropDownList15(Direction Specification Method)")
(cx-gui-do cx-activate-item "Mass-Flow Inlet*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|_2 (wall, id=7)"))
(cx-gui-do cx-list-tree-right-click "NavigationPane*List_Tree1" )
(cx-gui-do cx-activate-item "MenuBar*TypeSubMenu*pressure-outlet")
(cx-gui-do cx-activate-item "Pressure Outlet*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-set-toggle-button2 "Ribbon*Frame1*Frame3(Physics)*Table1*Table3(Solver)*ButtonBox1(Time)*Transient" #t)
(cx-gui-do cx-activate-item "Ribbon*Frame1*Frame3(Physics)*Table1*Table3(Solver)*ButtonBox1(Time)*Transient")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Methods"))
(cx-gui-do cx-set-list-selections "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList4(Turbulent Kinetic Energy)" '( 1))
(cx-gui-do cx-activate-item "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList4(Turbulent Kinetic Energy)")
(cx-gui-do cx-set-list-selections "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList5(Specific Dissipation Rate)" '( 1))
(cx-gui-do cx-activate-item "Solution Methods*Table1*Table3(Spatial Discretization)*DropDownList5(Specific Dissipation Rate)")
(cx-gui-do cx-set-list-selections "Solution Methods*Table1*Table4*DropDownList1(Transient Formulation)" '( 1))
(cx-gui-do cx-activate-item "Solution Methods*Table1*Table4*DropDownList1(Transient Formulation)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")
(cx-gui-do cx-activate-item "MenuBar*Surface ReportSubMenu*Mass-Weighted Average...")
(cx-gui-do cx-set-text-entry "Surface Report Definition*Table1*Table1*TextEntry1(Name)" "p-head")
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table1*TextEntry1(Name)")
(cx-gui-do cx-set-list-selections "Surface Report Definition*Table1*Table2*Table6*List1(Surfaces)" '( 0))
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table2*Table6*List1(Surfaces)")
(cx-gui-do cx-set-toggle-button2 "Surface Report Definition*Table1*Table1*Table6(Create)*CheckButton1(Report File)" #t)
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table1*Table6(Create)*CheckButton1(Report File)")
(cx-gui-do cx-set-toggle-button2 "Surface Report Definition*Table1*Table1*Table6(Create)*CheckButton2(Report Plot)" #t)
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table1*Table6(Create)*CheckButton2(Report Plot)")
(cx-gui-do cx-set-toggle-button2 "Surface Report Definition*Table1*Table1*Table6(Create)*CheckButton4(Print to Console)" #t)
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table1*Table6(Create)*CheckButton4(Print to Console)")
(cx-gui-do cx-activate-item "Surface Report Definition*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Report Definitions*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Residual"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Residual"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Residual"))
(cx-gui-do cx-set-real-entry-list "Residual Monitors*Table1*Table2*Table1*Table1(Equations)*RealEntry11" '( 1e-05))
(cx-gui-do cx-set-real-entry-list "Residual Monitors*Table1*Table2*Table1*Table1(Equations)*RealEntry17" '( 1e-05))
(cx-gui-do cx-set-real-entry-list "Residual Monitors*Table1*Table2*Table1*Table1(Equations)*RealEntry23" '( 1e-05))
(cx-gui-do cx-set-real-entry-list "Residual Monitors*Table1*Table2*Table1*Table1(Equations)*RealEntry29" '( 1e-05))
(cx-gui-do cx-set-real-entry-list "Residual Monitors*Table1*Table2*Table1*Table1(Equations)*RealEntry35" '( 1e-05))
(cx-gui-do cx-set-real-entry-list "Residual Monitors*Table1*Table2*Table1*Table1(Equations)*RealEntry41" '( 1e-05))
(cx-gui-do cx-activate-item "Residual Monitors*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Files"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Files"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Files"))
(cx-gui-do cx-activate-item "Report File Definitions*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots|p-head-rplot"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots|p-head-rplot"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots|p-head-rplot"))
(cx-gui-do cx-set-list-selections "Edit Report Plot*Table1*Table5(Options)*Table2*DropDownList3" '( 1))
(cx-gui-do cx-activate-item "Edit Report Plot*Table1*Table5(Options)*Table2*DropDownList3")
(cx-gui-do cx-activate-item "Edit Report Plot*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Report Plot Definitions*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")
(cx-gui-do cx-activate-item "MenuBar*Surface ReportSubMenu*Mass Flow Rate...")
(cx-gui-do cx-set-text-entry "Surface Report Definition*Table1*Table1*TextEntry1(Name)" "mfr-out")
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table1*TextEntry1(Name)")
(cx-gui-do cx-set-list-selections "Surface Report Definition*Table1*Table2*Table6*List1(Surfaces)" '( 1))
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table2*Table6*List1(Surfaces)")
(cx-gui-do cx-activate-item "Surface Report Definition*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")
(cx-gui-do cx-activate-item "MenuBar*Surface ReportSubMenu*Mass Flow Rate...")
(cx-gui-do cx-set-text-entry "Surface Report Definition*Table1*Table1*TextEntry1(Name)" "mfr-in")
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table1*TextEntry1(Name)")
(cx-gui-do cx-set-list-selections "Surface Report Definition*Table1*Table2*Table6*List1(Surfaces)" '( 0))
(cx-gui-do cx-activate-item "Surface Report Definition*Table1*Table2*Table6*List1(Surfaces)")
(cx-gui-do cx-activate-item "Surface Report Definition*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Report Definitions*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Report Definitions"))
(cx-gui-do cx-activate-item "Report Definitions*Table1*ButtonBox3*PushButton1(New)")
(cx-gui-do cx-activate-item "MenuBar*PopupMenuCreateMonitor*Expression...")
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*ButtonBox2*PushButton6(-)")
(cx-gui-do cx-set-list-selections "Expression Report Definition*Table1*Frame3(Select Operand Field Functions from)*Table1*DropDownList2" '( 4))
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*Frame3(Select Operand Field Functions from)*Table1*DropDownList2")
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*Frame3(Select Operand Field Functions from)*PushButton2(Select)")
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*ButtonBox2*PushButton16(/)")
(cx-gui-do cx-set-list-selections "Expression Report Definition*Table1*Frame3(Select Operand Field Functions from)*Table1*DropDownList2" '( 5))
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*Frame3(Select Operand Field Functions from)*Table1*DropDownList2")
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*Frame3(Select Operand Field Functions from)*PushButton2(Select)")
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*ButtonBox2*PushButton6(-)")
(cx-gui-do cx-activate-item "Expression Report Definition*Table1*ButtonBox2*PushButton8(1)")
(cx-gui-do cx-set-text-entry "Expression Report Definition*Table1*TextEntry4(New Function Name)" "diff-mfr")
(cx-gui-do cx-set-toggle-button2 "Expression Report Definition*Table2*Table1*Table6(Create)*CheckButton1(Report File)" #t)
(cx-gui-do cx-activate-item "Expression Report Definition*Table2*Table1*Table6(Create)*CheckButton1(Report File)")
(cx-gui-do cx-set-toggle-button2 "Expression Report Definition*Table2*Table1*Table6(Create)*CheckButton2(Report Plot)" #t)
(cx-gui-do cx-activate-item "Expression Report Definition*Table2*Table1*Table6(Create)*CheckButton2(Report Plot)")
(cx-gui-do cx-set-toggle-button2 "Expression Report Definition*Table2*Table1*Table6(Create)*CheckButton4(Print to Console)" #t)
(cx-gui-do cx-activate-item "Expression Report Definition*Table2*Table1*Table6(Create)*CheckButton4(Print to Console)")
(cx-gui-do cx-activate-item "Expression Report Definition*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Report Definitions*PanelButtons*PushButton1(Close)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots|diff-mfr-rplot"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots|diff-mfr-rplot"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Monitors|Report Plots|diff-mfr-rplot"))
(cx-gui-do cx-set-list-selections "Edit Report Plot*Table1*Table5(Options)*Table2*DropDownList3" '( 1))
(cx-gui-do cx-activate-item "Edit Report Plot*Table1*Table5(Options)*Table2*DropDownList3")
(cx-gui-do cx-activate-item "Edit Report Plot*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Initialization"))
(cx-gui-do cx-set-toggle-button2 "Solution Initialization*Table1*ToggleBox3(Initialization Methods)*Hybrid  Initialization" #t)
(cx-gui-do cx-activate-item "Solution Initialization*Table1*ToggleBox3(Initialization Methods)*Hybrid  Initialization")
(cx-gui-do cx-activate-item "Solution Initialization*Table1*Frame11*PushButton2(Initialize)")
(cx-gui-do cx-activate-item "Ribbon*Frame1*Frame5(Solution)*Table1*Table3(Activities)*PushButton2(Create)")
(cx-gui-do cx-activate-item "MenuBar*PopupMenuCreate*Execute Commands...")
(cx-gui-do cx-set-integer-entry "Execute Commands*IntegerEntry1(Defined Commands)" 1)
(cx-gui-do cx-activate-item "Execute Commands*IntegerEntry1(Defined Commands)")
(cx-gui-do cx-set-toggle-button2 "Execute Commands*Table2*CheckButton6" #t)
(cx-gui-do cx-activate-item "Execute Commands*Table2*CheckButton6")
(cx-gui-do cx-set-text-entry "Execute Commands*Table2*TextEntry11" "/file/read-journal output_residual.jou")
(cx-gui-do cx-activate-item "Execute Commands*PanelButtons*PushButton1(OK)")
(define port)  
(set! port (open-output-file "residuals.dat"))  
(do ((i 0 (+ i 1))) ((= i (length (solver-residuals)))) (format port "~a ~2t" (car (list-ref (solver-residuals) i))))  
(newline port)  
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))
(cx-gui-do cx-activate-item "NavigationPane*List_Tree1")
(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Solution|Run Calculation"))
(cx-gui-do cx-set-expression-entry "Run Calculation*Table1*Table7*ExpressionEntry1(Time Step Size)" '("1e-5" . 0))
(cx-gui-do cx-activate-item "Run Calculation*Table1*Table7*ExpressionEntry1(Time Step Size)")
(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*Table7*IntegerEntry2(Number of Time Steps)" 240)
(cx-gui-do cx-activate-item "Run Calculation*Table1*Table7*IntegerEntry2(Number of Time Steps)")
(cx-gui-do cx-set-integer-entry "Run Calculation*Table1*IntegerEntry10(Number of Iterations)" 25)
(cx-gui-do cx-activate-item "Run Calculation*Table1*IntegerEntry10(Number of Iterations)")
(cx-gui-do cx-activate-item "Run Calculation*Table1*PushButton22(Calculate)")


