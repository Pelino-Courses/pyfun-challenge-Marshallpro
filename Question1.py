from  datetime import date,datetime

def dif_date( date1:str,date2:str,date_format ="%Y-%m-%d")->int:
   '''
   this is function to calculate difference between two dates
   '''
   try :
      
       dat1 = datetime.strptime(date1,date_format)
       dat2 = datetime.strptime(date2,date_format)
   except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
   deff = abs((dat2-dat1).days)
   return deff

if __name__ == "__main__":
   try: 
      st = input("enter intial date in this format Year-Month-Day:")
      end= input("enter end date in this format Year-Month-Day:")
      result = dif_date(st,end)
      print(f"Number of days between {st} and {end} is {result} days.")
   
   except ValueError:
       print (f"Error")
