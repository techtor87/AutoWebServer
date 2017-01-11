from consts import *
from time import strftime, localtime
from datetime import timedelta, date
from summary_data import *
from build_plot import *

summary_values = {}
all_summary_values = []

def build_proj_index( ):

    fout = open(consts.proj_name_str + '-index.html', 'w+')
    import_values()

    build_status_header( fout )
    build_status_table( fout )

    build_val_plan_status( fout )

    build_completion_graphs( fout )

    build_assignment_list( fout )
    build_edr_assigment_list( fout )

    fout.write("<p>&nbsp;</p>\n")
    fout.write("<p><a href='index.html'><span style='font-size:18.0pt;color:#1F497D'>Return to Project List</span></a><p>\n</html>\n")
    fout.close()
    return

def import_values():
   global summary_values
   global all_summary_values
   all_summary_values = summary_data.load_file("summary_data.db")

   for val in all_summary_values:
      if val.date_val.date() == date.today():
         summary_values['today'] = val
      elif val.date_val.date() == (date.today() - timedelta(1)):
         summary_values['yest'] = val
      elif val.date_val.date() == (date.today() - timedelta(7)):
         summary_values['week'] = val

   return

def build_status_header( fout ):
    fout.write("<style><!--p{margin-top:0in; margin-bottom:0in; font-size:11.0pt; font-family:""Calibri"",cans-serif;}-->\n")
    fout.write("<!--td{border:none; border-top:solid #5B9BD5 1.0pt; border-bottom:solid #5B9BD5 1.0pt; padding:0in 5.4pt 0in 5.4pt; white-space: nowrap}</style>\n<html>\n")
    fout.write("<p><b><u><span style='font-size:22.0pt;color:#1F497D'>")
    fout.write(consts.proj_name_str)
    fout.write(" Status")
    fout.write(" &#8211; ")
    fout.write(strftime("%B %d, %Y", localtime() ))
    fout.write("</span></u></b></p>\n")
    fout.write("<p>&nbsp;</p>\n")
    fout.write("<p><b><u><span style='font-size:18.0pt;color:#1F497D'>SCN/Defect Status (All Customers)</span></u></b></p>\n")
    return

def Cells(x,y):
    return ""
def Format(x,y):
    return ""

def build_status_table( fout ):

    # Defect Table
    fout.write("<table Table border=0 cellspaceing=0 width 1042 style='width:781.6pt;margin-left:-.15pt;border-collapse:collapse'>\n")
    # Headers
    fout.write("<tr style='height:21.0pt'>\n")
    fout.write("<td valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;background:#5B9BD5;height:21.0pt'><p><b><span style='color:white'>Item Type</span></b></p></td>\n")
    fout.write("<td valign=bottom style='width:160.0pt;background:#5B9BD5;height:21.0pt'><p align=center style='text-align:center'><b><span style='font-size:16.0pt;color:white'>Active</span></b></p></td>\n")
    fout.write("<td valign=bottom style='width:230.0pt;background:#5B9BD5;height:21.0pt'><p align=center style='text-align:center'><b><span style='font-size:16.0pt;color:white'>Pending Validation/Confirmation</span></b></p></td>\n")
    fout.write("<td valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;background:#5B9BD5;height:21.0pt'><p align=center style='text-align:center'><b><span style='font-size:16.0pt;color:white'>Validated/Confirmed</span></b></p></td></tr>\n")

    # CMU Defects
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;height:15.0pt'><p><span style='color:black'>CMU Defects</span></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(0, 0) + "</span></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(0, 0) + "</span></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(0, 0) + "</span></p></td></tr>\n")

    # CMU SCNs
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;height:15.0pt'><p ><span style='color:black'>CMU SCNs</span></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(3, 2) + "</span></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(3, 3) + "</span></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(3, 4) + "</span></p></td></tr>\n")

    # CMU TOTAL
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;background:#BDD7EE;height:15.0pt'><p ><b><span style='color:black'>CMU Totals</span></b></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;background:#BDD7EE;height:15.0pt'><p align=center style='text-align:center'><b><span style='color:black'>" + str(summary_values['today'].cmu_active) + "</span></b></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;background:#BDD7EE;height:15.0pt'><p align=center style='text-align:center'><b><span style='color:black'>" + str(summary_values['today'].cmu_pending) + "</span></b></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;background:#BDD7EE;height:15.0pt'><p align=center style='text-align:center'><b><span style='color:black'>" + str(summary_values['today'].cmu_val) + "</span></b></p></td></tr>\n")

    # Blank
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;height:15.0pt'></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;height:15.0pt'></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;height:15.0pt'></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;height:15.0pt'></td></tr>\n")

    # CCA Defects
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;height:15.0pt'><p><span style='color:black'>CCA Defects</span></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(6, 2) + "</span></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(6, 3) + "</span></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(6, 4) + "</span></p></td></tr>\n")

    # CCA SCNs
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;height:15.0pt'><p ><span style='color:black'>CCA SCNs</span></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(7, 2) + "</span></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(7, 3) + "</span></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;height:15.0pt'><p align=center style='text-align:center'><span style='color:black'>" + Cells(7, 4) + "</span></p></td></tr>\n")

    # CCA TOTAL
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;background:#BDD7EE;height:15.0pt'><p ><b><span style='color:black'>CCA Totals</span></b></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;background:#BDD7EE;height:15.0pt'><p align=center style='text-align:center'><b><span style='color:black'>" + str(summary_values['today'].cca_active) + "</span></b></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;background:#BDD7EE;height:15.0pt'><p align=center style='text-align:center'><b><span style='color:black'>" + str(summary_values['today'].cca_pending) + "</span></b></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;background:#BDD7EE;height:15.0pt'><p align=center style='text-align:center'><b><span style='color:black'>" + str(summary_values['today'].cca_val) + "</span></b></p></td></tr>\n")

    # Blank
    fout.write("<tr style='height:15.0pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;height:15.0pt'></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;height:15.0pt'></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;height:15.0pt'></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;height:15.0pt'></td></tr>\n")

    # Total Today
    if summary_values['today'].tot_active < summary_values['yest'].tot_active:
        act_color = 'green'
        pass
    elif summary_values['today'].tot_active == summary_values['yest'].tot_active:
        act_color = 'yellow'
        pass
    else:
        act_color = 'red'
        pass

    if summary_values['today'].tot_pending < summary_values['yest'].tot_pending:
        pend_color = 'green'
        pass
    elif summary_values['today'].tot_pending == summary_values['yest'].tot_pending:
        pend_color = 'yellow'
        pass
    else:
        pend_color = 'red'
        pass

    if summary_values['today'].tot_val > summary_values['yest'].tot_val:
        val_color = 'green'
        pass
    elif summary_values['today'].tot_val == summary_values['yest'].tot_val:
        val_color = 'yellow'
        pass
    else:
        val_color = 'red'
        pass

    fout.write("<tr style='height:18.75pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;background-color:#BDD7EE;height:18.75pt'><p ><b><span style='font-size:14.0pt;color:black'>CCA &amp; CMU Totals Today</span></b></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;                                background-color:" + act_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['today'].cmu_active + summary_values['today'].cca_active) + "</span></b></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;                                background-color:" + pend_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['today'].cmu_pending + summary_values['today'].cca_pending) + "</span></b></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;background-color:" + val_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['today'].cmu_val + summary_values['today'].cca_val) + "</span></b></p></td></tr>\n")

    # Total Yesterday
    if summary_values['yest'].tot_active < summary_values['week'].tot_active:
        act_color = 'green'
        pass
    elif summary_values['yest'].tot_active == summary_values['week'].tot_active:
        act_color = 'yellow'
        pass
    else:
        act_color = 'red'
        pass

    if summary_values['yest'].tot_pending < summary_values['week'].tot_pending:
        pend_color = 'green'
        pass
    elif summary_values['yest'].tot_pending == summary_values['week'].tot_pending:
        pend_color = 'yellow'
        pass
    else:
        pend_color = 'red'
        pass

    if summary_values['yest'].tot_val > summary_values['week'].tot_val:
        val_color = 'green'
        pass
    elif summary_values['yest'].tot_val == summary_values['week'].tot_val:
        val_color = 'yellow'
        pass
    else:
        val_color = 'red'

    fout.write("<tr style='height:18.75pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;background-color:#BDD7EE;height:18.75pt'><p ><b><span style='font-size:14.0pt;color:black'>CCA &amp; CMU Totals Yesterday</span></b></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;                                background-color:" + act_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['yest'].cmu_active + summary_values['yest'].cca_active) + "</span></b></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;                                background-color:" + pend_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['yest'].cmu_pending + summary_values['yest'].cca_pending) + "</span></b></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;background-color:" + val_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['yest'].cmu_val + summary_values['yest'].cca_val) + "</span></b></p></td></tr>\n")

    # Total Week Ago
    act_color = 'green'
    pend_color = 'green'
    val_color = 'green'

    fout.write("<tr style='height:18.75pt'>\n")
    fout.write("<td width=256 valign=bottom style='width:192.0pt;border-left:solid #5B9BD5 1.0pt;background-color:#BDD7EE;height:18.75pt'><p ><b><span style='font-size:14.0pt;color:black'>CCA &amp; CMU Totals 1 Week Ago</span></b></p></td>\n")
    fout.write("<td width=213 valign=bottom style='width:160.0pt;                                background-color:" + act_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['week'].cmu_active + summary_values['week'].cca_active) + "</span></b></p></td>\n")
    fout.write("<td width=307 valign=bottom style='width:230.0pt;                                background-color:" + pend_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['week'].cmu_pending + summary_values['week'].cca_pending) + "</span></b></p></td>\n")
    fout.write("<td width=264 valign=bottom style='width:2.75in;border-right:solid #5B9BD5 1.0pt;background-color:" + val_color + ";height:18.75pt'><p align=center style='text-align:center'><b><span style='font-size:14.0pt;color:black'>" + str(summary_values['week'].cmu_val + summary_values['week'].cca_val) + "</span></b></p></td></tr></table>\n")

    return

def build_completion_graphs( fout ):
    weeks = mdate.WeekdayLocator()
    days  = mdate.DayLocator()

    all_date  = []
    cmu_act   = []
    cmu_pend  = []
    cmu_val   = []
    cca_act   = []
    cca_pend  = []
    cca_val   = []
    total_act = []
    total_pend= []
    total_val = []

    for record in all_summary_values:
        all_date.append(record.date_val)
        cmu_act.append(record.cmu_active)
        cmu_pend.append(record.cmu_pending)
        cmu_val.append(record.cmu_val)
        cca_act.append(record.cca_active)
        cca_pend.append(record.cca_pending)
        cca_val.append(record.cca_val)
        total_act.append(record.cmu_active + record.cca_active)
        total_pend.append(record.cmu_pending + record.cca_pending)
        total_val.append(record.cmu_val + record.cca_val)


    cust_burndown_plot( 'CMU SCN/Defects All Customers',
                        all_date,
                        [
                            [cmu_act, 'CMU Active'],
                            [cmu_pend, 'CMU Pending Validation/Confirmation']
                        ],
                        consts.proj_name_str + '_cmu_plot.png')


    cust_burndown_plot( 'CCA SCN/Defects All Customers',
                        all_date,
                        [
                            [cca_act, 'CCA Active'],
                            [cca_pend, 'CCA Pending Validation/Confirmation']
                        ],
                        consts.proj_name_str + '_cca_plot.png')


    cust_burndown_plot( consts.proj_name_str + ' SCN/Defects Totals (CMU & CCA) - All Customers',
                        all_date,
                        [
                            [total_act, consts.proj_name_str + ' Total Active'],
                            [total_pend, consts.proj_name_str + ' Total Pending Val/Confirm']
                        ],
                        consts.proj_name_str + '_total_plot.png')


    fout.write("<p>&nbsp;</p>\n")
    fout.write("<p><img src='" + consts.proj_name_str + "_total_plot.png' width=600 height=500></p>\n")
    fout.write("<p><img src='" + consts.proj_name_str + "_cmu_plot.png' width=300 height=250>\n")
    fout.write("<img src='" + consts.proj_name_str + "_cca_plot.png' width=300 height=250></p>\n")
    return

def build_val_plan_status( fout ):


    fout.write("<p>&nbsp;</p>\n")
    fout.write("<p ><b><u><span style='font-size:18.0pt;color:#1F497D'>Overall " + consts.proj_name_str)
    fout.write(" Val Plan execution status as of " + consts.proj_last_val_update + "</span></u></b></p>\n")

    fout.write("<table Table border=0 cellspacing=0 cellpadding=0 width=1038 style='width:778.5pt;border-collapse:collapse'>\n")

    fout.write("<tr style='height:21.0pt'>\n")
    fout.write("<td width=414               style='border-top:none;border-bottom:none;width:310.5pt;padding:0in 5.4pt 0in 5.4pt;height:21.0pt'>\n")
    fout.write("<p><b><span style='font-size:16.0pt;color:#4F81BD'>" + Cells(3, 8) + ":</span></b></p></td>\n")
    fout.write("<td width=624 valign=bottom style='border-top:none;border-bottom:none;width:6.5in;  padding:0in 5.4pt 0in 5.4pt;height:21.0pt'>\n")
    fout.write("<p><b><span style='font-size:16.0pt;color:#4F81BD'>" + Format(Cells(3, 9), "Percent") + " Complete</span></b></p></td></tr>\n")

    fout.write("<tr style='height:21.0pt'>\n")
    fout.write("<td width=414               style='border-top:none;border-bottom:none;width:310.5pt;padding:0in 5.4pt 0in 5.4pt;height:21.0pt'>\n")
    fout.write("<p><b><span style='font-size:16.0pt;color:#4F81BD'>" + Cells(4, 8) + ":</span></b></p></td>\n")
    fout.write("<td width=624 valign=bottom style='border-top:none;border-bottom:none;width:6.5in;  padding:0in 5.4pt 0in 5.4pt;height:21.0pt'>\n")
    fout.write("<p><b><span style='font-size:16.0pt;color:#4F81BD'>" + Format(Cells(4, 9), "Percent") + " Complete</span></b></p></td></tr>\n")

    fout.write("<tr style='height:21.0pt'>\n")
    fout.write("<td width=414               style='border-top:none;border-bottom:none;width:310.5pt;padding:0in 5.4pt 0in 5.4pt;height:21.0pt'>\n")
    fout.write("<p><b><span style='font-size:16.0pt;color:#4F81BD'>" + Cells(5, 8) + ":</span></b></p></td>\n")
    fout.write("<td width=624 valign=bottom style='border-top:none;border-bottom:none;width:6.5in;  padding:0in 5.4pt 0in 5.4pt;height:21.0pt'>\n")
    fout.write("<p><b><span style='font-size:16.0pt;color:#4F81BD'>" + Format(Cells(5, 9), "Percent") + " Complete</span></b></p></td></tr></table>\n")
    return

def build_assignment_list( fout ):
    fout.write("<p>&nbsp;</p>\n")
    build_assignment_header( fout )

    return

def build_assignment_header( fout ):
    fout.write("<p><b><u><span style='font-size:16.0pt;color:#1F497D'>Current ")
    fout.write(consts.proj_name_str)
    fout.write(" SCN/Defect Assignments (ALL CUSTOMERS)</span></u></b></p>\n")
    fout.write("<p><span style='font-size:16.0pt;color:#1F497D'>")
    fout.write("Spreadsheet with more assignment detail can be found here:</span></p>\n")
    fout.write("<p><a href='" + consts.proj_assignment_spreadsheet_link + "'><span style='font-size:16.0pt'>")
    fout.write(consts.proj_assignment_spreadsheet_link + "</span></a></p>\n")
    return

def build_edr_assigment_list( fout ):
    fout.write("<p>&nbsp;</p>\n")
    build_edr_header( fout )
    # Open Action Items by Engineer

    # Open DRs by Engineer

    return

def build_edr_header( fout ):
    fout.write("<p><b><u><span style='font-size:16.0pt;color:#1F497D'>Current ")
    fout.write(consts.proj_name_str)
    fout.write(" eDR Assignments (ALL CUSTOMERS)</span></u></b></p>\n")
    fout.write("<p><span style='font-size:16.0pt;color:#1F497D'>")
    fout.write("Spreadsheet with more eDR assignment detail can be found here:</span></p>\n")
    fout.write("<p><a href='" + consts.proj_edr_spreadsheet_link + "'><span style='font-size:16.0pt'>")
    fout.write(consts.proj_edr_spreadsheet_link + "</span></a></p>\n")
    return

if __name__ == '__main__':
    build_proj_index()
