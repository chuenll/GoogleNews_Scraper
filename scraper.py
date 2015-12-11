import urllib2
from xml.dom.minidom import parseString

def get_google_new_results( term, site, startdate, enddate, count ):
    results = []
    obj = parseString( urllib2.urlopen('https://www.google.com/search?hl=en&gl=ca&as_drrb=b&authuser=0&tbs=cdr:1%2Ccd_min:{}%2Ccd_max:{}&tbm=nws&q={}+site:{}&output=rss' .format(startdate, enddate, term,site)).read() )
    elements = obj.getElementsByTagName('title')[2:] # To get rid of unwanted title elements in XML doc    
    links = obj.getElementsByTagName('link')[2:]
    print links
    for element in elements[:count]:
        headline =  element.childNodes[0].data
        for link in links:
            url = link.childNodes[0].data.split('=')[-1]
        newssearch = headline + ' -> ' + url
        results.append( newssearch )

    return results

items = get_google_new_results( 'Beirut+attack', 'www.theglobeandmail.com','2015-11-01','2015-11-30', 7)
for i,e in enumerate(items):
    print '%d: %s' % (i+1,e,)
