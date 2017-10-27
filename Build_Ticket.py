from redminelib import Redmine
import xlrd

def open_excel(file = 'redmine.xlsx'):
      try:
            data = xlrd.open_workbook(file)
            return data
      except Exception as e:
            print(str(e))

def read_excel(file = 'redmine.xlsx'):
      data = open_excel(file)
      table = data.sheets()[0]
      nrows = table.nrows
      ncols = table.ncols
      colnames =  table.row_values(1)
      return colnames
      '''
      list =[]
      app = {}
      for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                  for i in range(len(colnames)):
                        app[colnames[i]] = row[i]
      return app
                  #list.append(app)
      #return list
      '''

def buildTicket(tables):
      redmine = Redmine("http://demo.redmine.org", username = "ChangA", password = '12345678')
      issue = redmine.issue.create(project_id = tables[0],
                                   subject = tables[1],
                                   tracker_id = int(tables[2]),
                                   description = tables[3],
                                   status_id = int(tables[4]),
                                   priority_id = int(tables[5]),
                                   assigned_to_id = tables[6],
                                   watcher_user_ids = tables[7],
                                   start_date = tables[8],
                                   due_date = tables[9])

def main():
      tables = read_excel()
      print(tables[1])
      buildTicket(tables)

if __name__ == "__main__":
      main()
