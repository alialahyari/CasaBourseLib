import requests 
import pandas as pd   
import codecs
import matplotlib.pyplot as plt
import json

def get_price(ticker, from_date, to_date):
  from_date = from_date[6:]+'-'+from_date[3:5]+'-'+from_date[0:2]
  to_date = to_date[6:]+'-'+to_date[3:5]+'-'+to_date[0:2]
  data =  { "ADH": "MA0000011512", "AFM": "MA0000012296", "AFI": "MA0000012114", "GAZ": "MA0000010951", "AGM": "MA0000010944", "ADI": "MA0000011819", "ALM": "MA0000010936",
 "ARD": "MA0000012460", "ATL": "MA0000011710", "ATW": "MA0000012445", "ATH": "MA0000010969", "NEJ": "MA0000011009", "BAL": "MA0000011991", "BOA": "MA0000012437",
 "BCP": "MA0000011884", "BCI": "MA0000010811", "CRS": "MA0000011868", "CDM": "MA0000010381", "CDA": "MA0000012049", "CIH": "MA0000011454", "CMA": "MA0000010506",
 "CMT": "MA0000011793", "COL": "MA0000011934", "CSR": "MA0000012247", "CTM": "MA0000010340", "DRI": "MA0000011421", "DLM": "MA0000011777", "DHO": "MA0000011850",
 "DIS": "MA0000010639", "DWY": "MA0000011637", "NKL": "MA0000011942", "EQD": "MA0000010357", "FBR": "MA0000011587", "HPS": "MA0000011611", "IBC": "MA0000011132",
 "IMO": "MA0000012387", "INV": 
 "MA0000011579", "JET": "MA0000012080", "LBV": "MA0000011801", "LHM": "MA0000012320", "LES": "MA0000012031", "LYD": "MA0000011439",
 "M2M": "MA0000011678", "MOX": "MA0000010985", "MAB": "MA0000011215", "MNG": "MA0000011058", "MLE": "MA0000010035", "IAM": "MA0000011488", "MDP": "MA0000011447",
 "MIC": "MA0000012163", "MUT": "MA0000012395", "NEX": "MA0000011140", "OUL": "MA0000010415", "PRO": "MA0000011660", "REB": "MA0000010993", "RDS": "MA0000012239",
 "RISMA": "MA0000011462", "S2M": "MA0000012106", "SAH": "MA0000012007", "SLF": "MA0000011744", "SAM": "MA0000010803", "SMI": "MA0000010068", "SNA": "MA0000011843",
 "SNP": "MA0000011728", "MSA": "MA0000012312", "SID": "MA0000010019", "SOT": "MA0000012502", "SRM": "MA0000011595", "SBM": "MA0000010365", "STR": "MA0000012056",
 "TQM": "MA0000012205", "TIM": "MA0000011686", "TMA": "MA0000012262", "UMR": "MA0000012023", "WAA": "MA0000010928", "ZDJ": "MA0000010571"  }

  url='https://www.leboursier.ma/api?method=getPriceHistory&ISIN='+str(data[ticker])+'&format=json&from='+str(from_date)+'&to='+str(to_date)
  r = requests.get(url)
  data = json.loads(codecs.decode(r.text.encode(), 'utf-8-sig'))
  df = pd.json_normalize(data['result'])
  return df 

  
