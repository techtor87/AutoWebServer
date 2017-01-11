#from build_proj_index import build_proj_index

proj_list = [
                'Missouri',
                'LCCM'
              ]

def build_index():
    fout = open('index.html', 'w+')
    fout.write("<style><!--p{margin-top:0in; margin-bottom:0in; font-size:11.0pt; font-family:""Calibri"",cans-serif;}-->\n")
    fout.write("<!--td{border:none; border-top:solid #5B9BD5 1.0pt; border-bottom:solid #5B9BD5 1.0pt; padding:0in 5.4pt 0in 5.4pt; white-space: nowrap}</style>\n<html>\n")
    fout.write("<p>&nbsp;</p>\n")
    fout.write("<p><b><span style='font-size:22.0pt;color:#1F497D'>GE Transportation Project Management Dashboard</span></b></p>\n")
    fout.write("<dl>\n")
    for proj in proj_list:
       fout.write("<p>&nbsp;</p>\n")
       fout.write("<li><a href='" + proj + "-index.html'><span style='font-size:16.0pt;color:#1F497D'>\t" + proj + "</span></a></li>\n")

    fout.write("</dl></html>\n")

    fout.close()

    #for proj in proj_list:
        #build_proj_index(proj)
    return


if __name__ == '__main__':
    build_index()
