# page is the HTML of the scroll down menu at this link:  http://www.ramaz.org/course/ 
page = '<OPTION VALUE="08/25/2013" >08/25/2013</OPTION><OPTIONVALUE="09/01/2013">09/01/2013</OPTION><OPTION VALUE="09/08/2013" >09/08/2013</OPTION><OPTION VALUE="09/15/2013" >09/15/2013</OPTION><OPTION VALUE="09/22/2013" >09/22/2013</OPTION><OPTION VALUE="09/29/2013" >09/29/2013</OPTION><OPTION VALUE="10/06/2013" >10/06/2013</OPTION><OPTION VALUE="10/13/2013" >10/13/2013</OPTION><OPTION VALUE="10/20/2013">10/20/2013</OPTION><OPTIONVALUE="10/27/2013">10/27/2013</OPTION><OPTION VALUE="11/03/2013" >11/03/2013</OPTION><OPTION VALUE="11/10/2013" >11/10/2013</OPTION><OPTION VALUE="11/17/2013" >11/17/2013</OPTION><OPTION VALUE="11/24/2013" >11/24/2013</OPTION><OPTION VALUE="12/01/2013" >12/01/2013</OPTION><OPTION VALUE="12/08/2013" >12/08/2013</OPTION><OPTION VALUE="12/15/2013" >12/15/2013</OPTION>OPTION VALUE="12/22/2013" >12/22/2013</OPTION><OPTION VALUE="12/29/2013" >12/29/2013</OPTION><OPTION VALUE="01/05/2014" >01/05/2014</OPTION><OPTION VALUE="01/12/2014" >01/12/2014</OPTION><OPTION VALUE="01/19/2014" >01/19/2014</OPTION><OPTION VALUE="01/26/2014" >01/26/2014</OPTION><OPTION VALUE="02/02/2014" >02/02/2014</OPTION><OPTION VALUE="02/09/2014" >02/09/2014</OPTION><OPTION VALUE="02/16/2014" >02/16/2014</OPTION><OPTION VALUE="02/23/2014" >02/23/2014</OPTION><OPTION VALUE="03/02/2014" >03/02/2014</OPTION><OPTION VALUE="03/09/2014" >03/09/2014</OPTION><OPTION VALUE="03/16/2014" >03/16/2014</OPTION><OPTION VALUE="03/23/2014" >03/23/2014</OPTION><OPTION VALUE="03/30/2014" >03/30/2014</OPTION><OPTION VALUE="04/06/2014" >04/06/2014</OPTION><OPTION VALUE="04/13/2014" >04/13/2014</OPTION><OPTION VALUE="04/20/2014" >04/20/2014</OPTION><OPTION VALUE="04/27/2014" >04/27/2014</OPTION><OPTION VALUE="05/04/2014" >05/04/2014</OPTION><OPTION VALUE="05/11/2014" >05/11/2014</OPTION><OPTION VALUE="05/18/2014" >05/18/2014</OPTION><OPTION VALUE="05/25/2014" >05/25/2014</OPTION><OPTION VALUE="06/01/2014" >06/01/2014</OPTION><OPTION VALUE="06/08/2014" >06/08/2014</OPTION><OPTION VALUE="06/15/2014" >06/15/2014</OPTION>'

def search_13(page):  # CUTS THE DATE OUT OF var PAGE IN 00/00/0000 format
    starter = '<OPTION VALUE="' # find the position where this starts
    start_link = page.find(starter)
    starter = len(starter)
    if start_link == -1:
        return None , 0, None 
  
    start_date = start_link + starter #position of the start of the date
    end_date = start_date + 10 # end date position

    dateText  =str(page[start_date: end_date]) # the cut  date  in the 00/00/0000 format
    return dateText, start_date, end_date

def remove_zero_date(normal_date):  #used in the funct  making_ order_dic
    # make 01/01/2013 to 1/1/2013
    first_nom_date = normal_date[:1]
    changed_first_zero = first_nom_date.replace("0","") #replace a starting zero of a month
    day = normal_date[1:]
    change_day = day.replace("/0","/")
    full_date_changed = changed_first_zero + change_day
    return full_date_changed

def web_link(enter_web_link): #used in the funct  making_ordered_dic
	#from 11/10/2013 to  11%2F10%2F2013
    web_link =  enter_web_link.replace("/","%2F") #00%00%0000
    return  web_link


def get_all_dates(page): #none changed dates, cut form HTML, not changed as a list
    dates = []
    while True:
        dateText, start_date, end_date = search_13(page)
        if dateText:
           dates.append(dateText)
           page = page[end_date:]
        else:
            break
    return dates

dates  = get_all_dates(page) 

def making_ordered_dict(dates): # I did it this way because if I did this in a normal dictionary then it will be out of order and will be annoying for users in the drop down menu on the site.
	json = "{"
	for date in dates:
		link = 'http://www.ramaz.org/course/view_weekly_planner.cfm?id_student=replace&date_from=' + web_link(date)		
		json +="'"+remove_zero_date(date) +"'"+  ': ' +"'"+ link+"'" + ', '
	json = json[:-2] # Get rid of the last ", "
	json += "};"
	print json
	
making_ordered_dict(dates)


