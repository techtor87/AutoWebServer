from datetime import date, datetime

class summary_data(object):
   def __init__(self, date_val, cmu_active, cmu_pending, cmu_val, cca_active, cca_pending, cca_val, tot_active='', tot_pending='', tot_val=''):
      self.date_val = datetime.strptime(date_val, "%m/%d/%Y")
      self.cmu_active = int(cmu_active)
      self.cmu_pending = int(cmu_pending)
      self.cmu_val = int(cmu_val)
      self.cca_active = int(cca_active)
      self.cca_pending = int(cca_pending)
      self.cca_val = int(cca_val)
      self.tot_active = self.cmu_active + self.cca_active
      self.tot_pending = self.cmu_pending + self.cca_pending
      self.tot_val = self.cmu_val + self.cca_val

   def print(self):
      strOut = ""
      strOut += str(self.date_val) + ", "
      strOut += str(self.cmu_active) + ", "
      strOut += str(self.cmu_pending) + ", "
      strOut += str(self.cmu_val) + ", "
      strOut += str(self.cca_active) + ", "
      strOut += str(self.cca_pending) + ", "
      strOut += str(self.cca_val) + ", "
      strOut += str(self.tot_active) + ", "
      strOut += str(self.tot_pending) + ", "
      strOut += str(self.tot_val)
      return strOut

   def print_line(self, fout):
      fout.write(self.date_val.strftime("%m/%d/%Y"))
      fout.write(", ")
      fout.write(str(self.cmu_active))
      fout.write(", ")
      fout.write(str(self.cmu_pending))
      fout.write(", ")
      fout.write(str(self.cmu_val))
      fout.write(", ")
      fout.write(str(self.cca_active))
      fout.write(", ")
      fout.write(str(self.cca_pending))
      fout.write(", ")
      fout.write(str(self.cca_val))
      fout.write(", ")
      fout.write(str((self.cmu_active + self.cmu_pending + self.cca_active + self.cca_pending)))
      fout.write(", ")
      fout.write(str(self.tot_active))
      fout.write(", ")
      fout.write(str(self.tot_pending + self.cca_pending))
      fout.write(", ")
      fout.write(str(self.tot_val))
      fout.write("\n")

   @classmethod
   def load_line(cls, fin):
      inputs = fin.split(", ")
      line = cls(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6])
      return line

   @classmethod
   def load_file(cls, fin_str):
      class_data = []
      try:
         fin = open(fin_str,'r')
      except IOError:
         return class_data

      for line in fin:
         class_data.append(summary_data.load_line(line))

      fin.close()
      return class_data

# fout = open("test.txt",'w+')
# data = []
# for i in range( 0 , 10):
   # data.append(summary_data("9/1"+str(i)+"/2016",i,2,3,4,5,6))
#
# # for i in data:
   # i.print_line(fout)
#
# fout.close()
# data_input = summary_data.load_file("test.txt")
# print(len(data_input))
# for i in data:
   # print(i.print())

