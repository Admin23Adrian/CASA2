If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If
session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").text = "zsd_toma"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CLIENTE").text = "20000123"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CONVENIO").text = "001"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CONVENIO").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CONVENIO").caretPosition = 3
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-VKORG").text = "SC10"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-VKORG").caretPosition = 4
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-VTWEG").text = "10"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").caretPosition = 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").caretPosition = 0
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]").sendVKey 12
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").text = "02"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-AUART").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-AUART").caretPosition = 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-AUART").text = "ZTRA"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-AUART").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-AUART").caretPosition = 4
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").text = "01"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-SPART").caretPosition = 2
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0112/txtGV_FLD_PRODUCTO").text = "LECTRUM 22.5"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0112/txtGV_FLD_PRODUCTO").caretPosition = 12
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0112/tblZDMSD_TOMA_PEDIDOTC_BUSCMAT/txtGS_BUSCMAT-KWMENG[18,0]").text = "1"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0112/tblZDMSD_TOMA_PEDIDOTC_BUSCMAT/txtGS_BUSCMAT-KWMENG[18,0]").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0112/tblZDMSD_TOMA_PEDIDOTC_BUSCMAT/txtGS_BUSCMAT-KWMENG[18,0]").caretPosition = 12
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/btnBT_CARBUS").press
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT").select
session.findById("wnd[0]").sendVKey 4
session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[7,24]").text = "*6009230/01*"
session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[7,24]").setFocus
session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[7,24]").caretPosition = 12
session.findById("wnd[1]").sendVKey 0
session.findById("wnd[1]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-PED_EXTERNO").text = "100827"
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-PED_EXTERNO").caretPosition = 6
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/subSBS_DIRECCIONES:ZDMSD_TOMA_PEDIDO:0121/radGS_DIR-FCIA-MARK").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/subSBS_DIRECCIONES:ZDMSD_TOMA_PEDIDO:0121/radGS_DIR-FCIA-MARK").select
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/ctxtGS_ENTREGA-AFIL_NRO").caretPosition = 9
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-OBS_MOBILE").setFocus
session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-OBS_MOBILE").caretPosition = 0
session.findById("wnd[0]/tbar[0]/btn[11]").press
session.findById("wnd[1]/usr/btnBUTTON_1").press
session.findById("wnd[1]").sendVKey 0
session.findById("wnd[0]/tbar[1]/btn[7]").press
session.findById("wnd[0]").sendVKey 0
