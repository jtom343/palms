from django.shortcuts import render
from django.views.generic import TemplateView
import bs4, requests



# def BloombergPrice(XUrl):
#     res = requests.get(XUrl)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text,'lxml')
#     elems = soup.select('#content > div > div > div.basic-quote > div > div.price-container > div.price')
#     elems2 = soup.select('#content > div > div > div.basic-quote > div > div.price-datetime')
#     ExchangeRate = elems[0].text.strip()
#     ExchangeTime = elems2[0].text.strip()
#     return elems[0].text.strip(), elems2[0].text.strip()
# xrate,rdate = BloombergPrice('https://www.bloomberg.com/quote/USDDOP:CUR')



def XEUSD(XUrl):
  res = requests.get(XUrl)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text,'lxml')
  elems = soup.select('#ucc-container > span.uccAmountWrap > span.uccResultAmount')
  elems2 = soup.select('#ucc-container > span.uccResultTitle.clearfix > span')
  ExchangeRate = elems[0].text.strip()
  ExchangeTime2 = elems2[0].text.strip()
  return elems[0].text.strip(),elems2[0].text.strip()
USRate,USDate = XEUSD('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=DOP')



def XEEuro(XUrl):
  res = requests.get(XUrl)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text,'lxml')
  elems = soup.select('#ucc-container > span.uccAmountWrap > span.uccResultAmount')
  elems2 = soup.select('#ucc-container > span.uccResultTitle.clearfix > span')
  ExchangeRate = elems[0].text.strip()
  ExchangeTime2 = elems2[0].text.strip()
  return elems[0].text.strip(),elems2[0].text.strip()
EurRate,EurDate = XEEuro('https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=DOP')

#function to store exchange rate in model db

# from celery.schedules import crontab
#
# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'tasks.add',
#         'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'args': (16, 16),
#     },
# }

# #this is Stack Overflow answer
# from celery.schedules import crontab
# from celery.task import periodic_task
#
# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
# def every_monday_morning():
#     print("This is run every Monday morning at 7:30")
#
# def DBStore(self):
#     pass





class HomeView(TemplateView):
    template_name = 'city/home.html'
    def get_context_data(self, **kwargs):
        context = {'USRate':USRate,'USDate':USDate, 'EurRate':EurRate, 'EurDate':EurDate}
        # context = {'EurRate':EurRate, 'EurDate':EurDate}
        return context


def allcities(request):
    return render(request,'city/all/all.html')
