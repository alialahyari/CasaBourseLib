#Casabourselib

```python
by Yassine Rhzif & Ahmed Ouaboune 
https://www.linkedin.com/in/Rhzif/
https://www.linkedin.com/in/ahmed-ouaboune/
```

```python
#pour installer le package veuillez ouvrir votre ligne de commands "CMD" et tapez le code suivant 
pip install Casabourselib
```


```python
#c'est comme ca vous pouvez importer le package Casabourselib
#vous pouvez utilisez n'import quoi a la place de 'cbl' mais fait attention de l'utilisez lorsque vous appellez les fonctions 
import Casabourselib  as cbl
```


```python
#cette fonction donne le symbole (Ticker) de chaque entreprise cotée en bourse de casablanca
get_tickers()
```


```python
#exemple d'appel:
cbl.get_tickers()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Titre</th>
      <th>Ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Addoha</td>
      <td>ADH</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AFMA</td>
      <td>AFM</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afric Indus.</td>
      <td>AFI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Afriquia Gaz</td>
      <td>GAZ</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Agma</td>
      <td>AGM</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Timar</td>
      <td>TIM</td>
    </tr>
    <tr>
      <th>72</th>
      <td>TotalMaroc</td>
      <td>TMA</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Unimer</td>
      <td>UMR</td>
    </tr>
    <tr>
      <th>74</th>
      <td>WAFA ASSURANCE</td>
      <td>WAA</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Zellidja</td>
      <td>ZDJ</td>
    </tr>
  </tbody>
</table>
<p>76 rows × 2 columns</p>
</div>




```python
#cette fonction donne le Cour de chaque entreprise cotée en bourse de casablanca
get_stock_price(ticker, from_date, to_date)
```


```python
#exemple d'appel: 
cbl.get_stock_price('CIH', '01/01/2017', '18/10/2021')
#vous pouvez egalement donner l'ISIN a la place de ticker comme argument 
cbl.get_stock_price('MA0000011454', '01/01/2017', '18/10/2021')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
      <th>min</th>
      <th>max</th>
      <th>variation</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>02/01/2017</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-100.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>03/01/2017</th>
      <td>310.00</td>
      <td>300.00</td>
      <td>310.00</td>
      <td>3.33</td>
      <td>347.0</td>
    </tr>
    <tr>
      <th>04/01/2017</th>
      <td>305.40</td>
      <td>302.00</td>
      <td>310.00</td>
      <td>-1.48</td>
      <td>36480.0</td>
    </tr>
    <tr>
      <th>05/01/2017</th>
      <td>311.00</td>
      <td>306.15</td>
      <td>315.00</td>
      <td>1.83</td>
      <td>14916.0</td>
    </tr>
    <tr>
      <th>06/01/2017</th>
      <td>325.00</td>
      <td>320.00</td>
      <td>330.00</td>
      <td>4.50</td>
      <td>128910.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>12/10/2021</th>
      <td>315.10</td>
      <td>315.00</td>
      <td>323.00</td>
      <td>-0.91</td>
      <td>749.0</td>
    </tr>
    <tr>
      <th>13/10/2021</th>
      <td>320.00</td>
      <td>315.10</td>
      <td>320.00</td>
      <td>1.56</td>
      <td>5542.0</td>
    </tr>
    <tr>
      <th>14/10/2021</th>
      <td>320.00</td>
      <td>317.00</td>
      <td>320.00</td>
      <td>0.00</td>
      <td>1047.0</td>
    </tr>
    <tr>
      <th>15/10/2021</th>
      <td>320.95</td>
      <td>314.00</td>
      <td>321.85</td>
      <td>0.30</td>
      <td>2703.0</td>
    </tr>
    <tr>
      <th>18/10/2021</th>
      <td>325.00</td>
      <td>316.00</td>
      <td>325.00</td>
      <td>1.26</td>
      <td>31831.0</td>
    </tr>
  </tbody>
</table>
<p>1189 rows × 5 columns</p>
</div>




```python
#cette fonction donne le Cours de l'indice boursier MADEX
get_madex_price(periode)
```


```python
#exemple d'appel:
cbl.get_madex_price('1y') #'1y' jusqu'au '5y' aussi pour les mois '1m' ...'12m'
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>09/11/2020</th>
      <td>8587.8335</td>
    </tr>
    <tr>
      <th>10/11/2020</th>
      <td>8622.4817</td>
    </tr>
    <tr>
      <th>11/11/2020</th>
      <td>8603.3549</td>
    </tr>
    <tr>
      <th>12/11/2020</th>
      <td>8626.6573</td>
    </tr>
    <tr>
      <th>13/11/2020</th>
      <td>8673.0717</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>01/11/2021</th>
      <td>10946.7580</td>
    </tr>
    <tr>
      <th>02/11/2021</th>
      <td>10995.6448</td>
    </tr>
    <tr>
      <th>03/11/2021</th>
      <td>10991.2126</td>
    </tr>
    <tr>
      <th>04/11/2021</th>
      <td>10927.7211</td>
    </tr>
    <tr>
      <th>05/11/2021</th>
      <td>10848.1172</td>
    </tr>
  </tbody>
</table>
<p>248 rows × 1 columns</p>
</div>




```python
#cette fonction donne le Cour de l'indice boursier MASI
get_masi_price(periode)
```


```python
#exemple d'appel :
cbl.get_masi_price('5y') #'1y' jusqu'au '5y' aussi pour les mois '1m' ...'12m'
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>07/11/2016</th>
      <td>10521.9671</td>
    </tr>
    <tr>
      <th>08/11/2016</th>
      <td>10553.5579</td>
    </tr>
    <tr>
      <th>09/11/2016</th>
      <td>10580.2624</td>
    </tr>
    <tr>
      <th>10/11/2016</th>
      <td>10564.6172</td>
    </tr>
    <tr>
      <th>11/11/2016</th>
      <td>10551.4266</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>01/11/2021</th>
      <td>13507.5453</td>
    </tr>
    <tr>
      <th>02/11/2021</th>
      <td>13562.6362</td>
    </tr>
    <tr>
      <th>03/11/2021</th>
      <td>13569.3304</td>
    </tr>
    <tr>
      <th>04/11/2021</th>
      <td>13506.9925</td>
    </tr>
    <tr>
      <th>05/11/2021</th>
      <td>13413.8017</td>
    </tr>
  </tbody>
</table>
<p>1240 rows × 1 columns</p>
</div>




```python
#Cette fonction donne les dividendes distribués de chaque entreprise cotée en bourse
get_dividends(ticker)
```


```python
#exemple d'appel :
cbl.get_dividends('CIH') 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dividende Ordinaire</th>
      <th>Date de détachement</th>
      <th>Date de paiement</th>
      <th>Dividende Exceptionnel</th>
      <th>Date de détachement.1</th>
      <th>Date de paiement.1</th>
    </tr>
    <tr>
      <th>Année</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020</th>
      <td>8.00</td>
      <td>07/07/2021</td>
      <td>16/07/2021</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>14.00</td>
      <td>21/09/2020</td>
      <td>30/09/2020</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>14.00</td>
      <td>26/06/2019</td>
      <td>05/07/2019</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>14.00</td>
      <td>27/06/2018</td>
      <td>06/07/2018</td>
      <td>2.00</td>
      <td>27/06/2018</td>
      <td>06/07/2018</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>14.00</td>
      <td>28/06/2017</td>
      <td>07/07/2017</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>14.00</td>
      <td>27/06/2016</td>
      <td>11/07/2016</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>14.00</td>
      <td>26/06/2015</td>
      <td>07/07/2015</td>
      <td>2.00</td>
      <td>26/06/2015</td>
      <td>07/07/2015</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>15.00</td>
      <td>25/06/2014</td>
      <td>04/07/2014</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>14.00</td>
      <td>20/06/2013</td>
      <td>01/07/2013</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>11.00</td>
      <td>21/06/2012</td>
      <td>02/07/2012</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>6.00</td>
      <td>22/06/2011</td>
      <td>01/07/2011</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>6.00</td>
      <td>22/06/2010</td>
      <td>01/07/2010</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>18.00</td>
      <td>07/08/2009</td>
      <td>29/09/2009</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>10.00</td>
      <td>19/09/2008</td>
      <td>24/09/2008</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Cette fonction donne les différents indicateurs économique de chaque entreprise cotée en bourse
get_indicators(ticker)
```


```python
#exemple d'appel :
cbl.get_indicators('CIH')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2020</th>
      <th>2019</th>
      <th>2018</th>
    </tr>
    <tr>
      <th>Chiffres</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Comptes consolidés</th>
      <td>Oui</td>
      <td>Oui</td>
      <td>Oui</td>
    </tr>
    <tr>
      <th>Capital social (2)</th>
      <td>2 832 473 500</td>
      <td>2 832 473 500</td>
      <td>2 660 808 500</td>
    </tr>
    <tr>
      <th>Capitaux propres (3)</th>
      <td>5 424 245 000</td>
      <td>5 487 522 000</td>
      <td>5 121 960 000</td>
    </tr>
    <tr>
      <th>Nombre titres(2)</th>
      <td>28 324 735</td>
      <td>28 324 735</td>
      <td>26 608 085</td>
    </tr>
    <tr>
      <th>Produit Net bancaire</th>
      <td>2 759 674 000</td>
      <td>2 501 863 000</td>
      <td>2 248 842 000</td>
    </tr>
    <tr>
      <th>Résultat d'exploitation</th>
      <td>67 190 000</td>
      <td>691 771 000</td>
      <td>603 042 000</td>
    </tr>
    <tr>
      <th>Résultat net (4)</th>
      <td>80 655 000</td>
      <td>426 382 000</td>
      <td>455 043 000</td>
    </tr>
    <tr>
      <th>BPA</th>
      <td>2.85</td>
      <td>15.05</td>
      <td>17.10</td>
    </tr>
    <tr>
      <th>ROE (en %)</th>
      <td>1.49</td>
      <td>7.77</td>
      <td>8.88</td>
    </tr>
    <tr>
      <th>Payout (en %)</th>
      <td>-</td>
      <td>93.00</td>
      <td>81.86</td>
    </tr>
    <tr>
      <th>Dividend yield (en %)</th>
      <td>-</td>
      <td>4.68</td>
      <td>4.67</td>
    </tr>
    <tr>
      <th>PER</th>
      <td>89.55</td>
      <td>19.86</td>
      <td>17.54</td>
    </tr>
    <tr>
      <th>PBR</th>
      <td>1.33</td>
      <td>1.54</td>
      <td>1.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#cette fonction donne la composition de l'indice Masi avec le poid, capitalisation et le facteur flottant de chaque titre.
get_masi_data()
```


```python
#exemple d'appel :
cbl.get_masi_data()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Code Isin</th>
      <th></th>
      <th>Instrument</th>
      <th></th>
      <th>Nombre de titres</th>
      <th></th>
      <th>Cours</th>
      <th></th>
      <th>Facteur flottant</th>
      <th></th>
      <th>Facteur de plafonnement</th>
      <th></th>
      <th>Capitalisation flottante</th>
      <th></th>
      <th>Poids</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td>MA0000012445</td>
      <td></td>
      <td>ATTIJARIWAFA BANK</td>
      <td></td>
      <td>215 140 839</td>
      <td></td>
      <td>496,50</td>
      <td></td>
      <td>0,30</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>32 045 227 969,05</td>
      <td></td>
      <td>0,1825</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td>MA0000011488</td>
      <td></td>
      <td>ITISSALAT AL-MAGHRIB</td>
      <td></td>
      <td>879 095 340</td>
      <td></td>
      <td>143,50</td>
      <td></td>
      <td>0,20</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>25 230 036 258,00</td>
      <td></td>
      <td>0,1437</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td></td>
      <td>MA0000012320</td>
      <td></td>
      <td>LAFARGEHOLCIM MAR</td>
      <td></td>
      <td>23 431 240</td>
      <td></td>
      <td>2220,00</td>
      <td></td>
      <td>0,30</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>15 605 205 840,00</td>
      <td></td>
      <td>0,0889</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td></td>
      <td>MA0000011884</td>
      <td></td>
      <td>BCP</td>
      <td></td>
      <td>203 312 473</td>
      <td></td>
      <td>282,50</td>
      <td></td>
      <td>0,20</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>11 487 154 724,50</td>
      <td></td>
      <td>0,0654</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td></td>
      <td>MA0000012247</td>
      <td></td>
      <td>COSUMAR</td>
      <td></td>
      <td>94 487 143</td>
      <td></td>
      <td>270,00</td>
      <td></td>
      <td>0,40</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>10 204 611 444,00</td>
      <td></td>
      <td>0,0581</td>
      <td></td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>70</th>
      <td></td>
      <td>MA0000011132</td>
      <td></td>
      <td>IB MAROC.COM</td>
      <td></td>
      <td>417 486</td>
      <td></td>
      <td>46,73</td>
      <td></td>
      <td>0,45</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>8 779 104,35</td>
      <td></td>
      <td>0,0000</td>
      <td></td>
    </tr>
    <tr>
      <th>71</th>
      <td></td>
      <td>MA0000011686</td>
      <td></td>
      <td>TIMAR</td>
      <td></td>
      <td>301 100</td>
      <td></td>
      <td>144,60</td>
      <td></td>
      <td>0,20</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>8 707 812,00</td>
      <td></td>
      <td>0,0000</td>
      <td></td>
    </tr>
    <tr>
      <th>72</th>
      <td></td>
      <td>MA0000010571</td>
      <td></td>
      <td>ZELLIDJA S.A</td>
      <td></td>
      <td>572 849</td>
      <td></td>
      <td>87,00</td>
      <td></td>
      <td>0,10</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>4 983 786,30</td>
      <td></td>
      <td>0,0000</td>
      <td></td>
    </tr>
    <tr>
      <th>73</th>
      <td></td>
      <td>MA0000010993</td>
      <td></td>
      <td>REBAB COMPANY</td>
      <td></td>
      <td>176 456</td>
      <td></td>
      <td>107,95</td>
      <td></td>
      <td>0,20</td>
      <td></td>
      <td>1,00</td>
      <td></td>
      <td>3 809 685,04</td>
      <td></td>
      <td>0,0000</td>
      <td></td>
    </tr>
    <tr>
      <th>74</th>
      <td></td>
      <td></td>
      <td></td>
      <td>Total</td>
      <td></td>
      <td>2 680 176 515,00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>175 629 484 694,18</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>75 rows × 17 columns</p>
</div>




```python
#cette fonction donne la composition de l'indice Madex avec le poid, capitalisation et le facteur flottant de chaque titre.
get_madex_data()
```


```python
#exemple d'appel :
cbl.get_madex_data()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Code Isin</th>
      <th>Instrument</th>
      <th>Nombre de titres</th>
      <th>Cours</th>
      <th>Facteur flottant</th>
      <th>Facteur de plafonnement</th>
      <th>Capitalisation flottante</th>
      <th>Poids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MA0000012445</td>
      <td>ATTIJARIWAFA BANK</td>
      <td>215 140 839</td>
      <td>496,50</td>
      <td>0,30</td>
      <td>1,00</td>
      <td>32 045 227 969,05</td>
      <td>0,1930</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MA0000011488</td>
      <td>ITISSALAT AL-MAGHRIB</td>
      <td>879 095 340</td>
      <td>143,50</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>25 230 036 258,00</td>
      <td>0,1519</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MA0000012320</td>
      <td>LAFARGEHOLCIM MAR</td>
      <td>23 431 240</td>
      <td>2 220,00</td>
      <td>0,30</td>
      <td>1,00</td>
      <td>15 605 205 840,00</td>
      <td>0,0940</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MA0000011884</td>
      <td>BCP</td>
      <td>203 312 473</td>
      <td>282,50</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>11 487 154 724,50</td>
      <td>0,0692</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MA0000012247</td>
      <td>COSUMAR</td>
      <td>94 487 143</td>
      <td>270,00</td>
      <td>0,40</td>
      <td>1,00</td>
      <td>10 204 611 444,00</td>
      <td>0,0614</td>
    </tr>
    <tr>
      <th>5</th>
      <td>MA0000012437</td>
      <td>BANK OF AFRICA</td>
      <td>205 606 648</td>
      <td>186,00</td>
      <td>0,25</td>
      <td>1,00</td>
      <td>9 560 709 132,00</td>
      <td>0,0576</td>
    </tr>
    <tr>
      <th>6</th>
      <td>MA0000010506</td>
      <td>CIMENTS DU MAROC</td>
      <td>14 436 004</td>
      <td>1 900,00</td>
      <td>0,30</td>
      <td>1,00</td>
      <td>8 228 522 280,00</td>
      <td>0,0495</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MA0000012312</td>
      <td>SODEP-Marsa Maroc</td>
      <td>73 395 600</td>
      <td>280,35</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>7 201 759 761,00</td>
      <td>0,0434</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MA0000011801</td>
      <td>LABEL VIE</td>
      <td>2 838 962</td>
      <td>4 650,00</td>
      <td>0,45</td>
      <td>1,00</td>
      <td>5 940 527 985,00</td>
      <td>0,0358</td>
    </tr>
    <tr>
      <th>9</th>
      <td>MA0000010928</td>
      <td>WAFA ASSURANCE</td>
      <td>3 500 000</td>
      <td>4 899,00</td>
      <td>0,25</td>
      <td>1,00</td>
      <td>4 286 625 000,00</td>
      <td>0,0258</td>
    </tr>
    <tr>
      <th>10</th>
      <td>MA0000012205</td>
      <td>TAQA MOROCCO</td>
      <td>23 588 542</td>
      <td>1 117,00</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>3 952 260 212,10</td>
      <td>0,0238</td>
    </tr>
    <tr>
      <th>11</th>
      <td>MA0000011611</td>
      <td>HPS</td>
      <td>703 599</td>
      <td>7 050,00</td>
      <td>0,65</td>
      <td>1,00</td>
      <td>3 224 242 417,50</td>
      <td>0,0194</td>
    </tr>
    <tr>
      <th>12</th>
      <td>MA0000012262</td>
      <td>TOTALENERGIES MARKETING MAROC</td>
      <td>8 960 000</td>
      <td>1 751,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>3 137 792 000,00</td>
      <td>0,0189</td>
    </tr>
    <tr>
      <th>13</th>
      <td>MA0000011058</td>
      <td>MANAGEM</td>
      <td>9 991 308</td>
      <td>1 560,00</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>2 337 966 072,00</td>
      <td>0,0141</td>
    </tr>
    <tr>
      <th>14</th>
      <td>MA0000012460</td>
      <td>ARADEI CAPITAL</td>
      <td>10 645 783</td>
      <td>405,00</td>
      <td>0,45</td>
      <td>1,00</td>
      <td>1 940 193 951,75</td>
      <td>0,0117</td>
    </tr>
    <tr>
      <th>15</th>
      <td>MA0000011454</td>
      <td>CIH</td>
      <td>28 324 735</td>
      <td>340,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>1 926 081 980,00</td>
      <td>0,0116</td>
    </tr>
    <tr>
      <th>16</th>
      <td>MA0000010811</td>
      <td>BMCI</td>
      <td>13 279 286</td>
      <td>670,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>1 779 424 324,00</td>
      <td>0,0107</td>
    </tr>
    <tr>
      <th>17</th>
      <td>MA0000010365</td>
      <td>SOCIETE DES BOISSONS DU MAROC</td>
      <td>2 829 653</td>
      <td>2 800,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>1 584 605 680,00</td>
      <td>0,0095</td>
    </tr>
    <tr>
      <th>18</th>
      <td>MA0000011793</td>
      <td>MINIERE TOUISSIT</td>
      <td>1 681 233</td>
      <td>1 710,00</td>
      <td>0,50</td>
      <td>1,00</td>
      <td>1 437 454 215,00</td>
      <td>0,0087</td>
    </tr>
    <tr>
      <th>19</th>
      <td>MA0000012395</td>
      <td>MUTANDIS SCA</td>
      <td>7 996 737</td>
      <td>250,00</td>
      <td>0,70</td>
      <td>1,00</td>
      <td>1 399 428 975,00</td>
      <td>0,0084</td>
    </tr>
    <tr>
      <th>20</th>
      <td>MA0000012031</td>
      <td>LESIEUR CRISTAL</td>
      <td>27 631 510</td>
      <td>188,75</td>
      <td>0,25</td>
      <td>1,00</td>
      <td>1 303 861 878,13</td>
      <td>0,0079</td>
    </tr>
    <tr>
      <th>21</th>
      <td>MA0000011512</td>
      <td>DOUJA PROM ADDOHA</td>
      <td>402 551 254</td>
      <td>10,53</td>
      <td>0,30</td>
      <td>1,00</td>
      <td>1 271 659 411,39</td>
      <td>0,0077</td>
    </tr>
    <tr>
      <th>22</th>
      <td>MA0000012502</td>
      <td>SOTHEMA</td>
      <td>7 200 000</td>
      <td>1 529,00</td>
      <td>0,10</td>
      <td>1,00</td>
      <td>1 100 880 000,00</td>
      <td>0,0066</td>
    </tr>
    <tr>
      <th>23</th>
      <td>MA0000010969</td>
      <td>AUTO HALL</td>
      <td>50 294 528</td>
      <td>108,50</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>1 091 391 257,60</td>
      <td>0,0066</td>
    </tr>
    <tr>
      <th>24</th>
      <td>MA0000011710</td>
      <td>ATLANTASANAD</td>
      <td>60 283 595</td>
      <td>117,00</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>1 057 977 092,25</td>
      <td>0,0064</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MA0000011728</td>
      <td>SNEP</td>
      <td>2 400 000</td>
      <td>747,10</td>
      <td>0,40</td>
      <td>1,00</td>
      <td>717 216 000,00</td>
      <td>0,0043</td>
    </tr>
    <tr>
      <th>26</th>
      <td>MA0000012387</td>
      <td>IMMORENTE INVEST</td>
      <td>9 007 000</td>
      <td>101,00</td>
      <td>0,70</td>
      <td>1,00</td>
      <td>636 794 900,00</td>
      <td>0,0038</td>
    </tr>
    <tr>
      <th>27</th>
      <td>MA0000010019</td>
      <td>SONASID</td>
      <td>3 900 000</td>
      <td>610,00</td>
      <td>0,25</td>
      <td>1,00</td>
      <td>594 750 000,00</td>
      <td>0,0036</td>
    </tr>
    <tr>
      <th>28</th>
      <td>MA0000011850</td>
      <td>DELTA HOLDING</td>
      <td>87 600 000</td>
      <td>31,39</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>549 952 800,00</td>
      <td>0,0033</td>
    </tr>
    <tr>
      <th>29</th>
      <td>MA0000011637</td>
      <td>DISWAY</td>
      <td>1 885 762</td>
      <td>710,00</td>
      <td>0,40</td>
      <td>1,00</td>
      <td>535 556 408,00</td>
      <td>0,0032</td>
    </tr>
    <tr>
      <th>30</th>
      <td>MA0000012163</td>
      <td>MICRODATA</td>
      <td>1 680 000</td>
      <td>635,00</td>
      <td>0,45</td>
      <td>1,00</td>
      <td>480 060 000,00</td>
      <td>0,0029</td>
    </tr>
    <tr>
      <th>31</th>
      <td>MA0000011744</td>
      <td>SALAFIN</td>
      <td>3 124 119</td>
      <td>690,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>431 128 422,00</td>
      <td>0,0026</td>
    </tr>
    <tr>
      <th>32</th>
      <td>MA0000011439</td>
      <td>LYDEC</td>
      <td>8 000 000</td>
      <td>264,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>422 400 000,00</td>
      <td>0,0025</td>
    </tr>
    <tr>
      <th>33</th>
      <td>MA0000012296</td>
      <td>AFMA</td>
      <td>1 000 000</td>
      <td>1 360,00</td>
      <td>0,30</td>
      <td>1,00</td>
      <td>408 000 000,00</td>
      <td>0,0025</td>
    </tr>
    <tr>
      <th>34</th>
      <td>MA0000010068</td>
      <td>SMI</td>
      <td>1 645 090</td>
      <td>1 577,00</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>389 146 039,50</td>
      <td>0,0023</td>
    </tr>
    <tr>
      <th>35</th>
      <td>MA0000012080</td>
      <td>JET CONTRACTORS</td>
      <td>3 029 522</td>
      <td>261,80</td>
      <td>0,40</td>
      <td>1,00</td>
      <td>317 251 543,84</td>
      <td>0,0019</td>
    </tr>
    <tr>
      <th>36</th>
      <td>MA0000011819</td>
      <td>ALLIANCES</td>
      <td>22 078 588</td>
      <td>39,17</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>302 686 402,19</td>
      <td>0,0018</td>
    </tr>
    <tr>
      <th>37</th>
      <td>MA0000012239</td>
      <td>RES DAR SAADA</td>
      <td>26 208 850</td>
      <td>31,94</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>292 988 734,15</td>
      <td>0,0018</td>
    </tr>
    <tr>
      <th>38</th>
      <td>MA0000011934</td>
      <td>COLORADO</td>
      <td>12 088 208</td>
      <td>64,78</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>274 075 939,98</td>
      <td>0,0017</td>
    </tr>
    <tr>
      <th>39</th>
      <td>MA0000011462</td>
      <td>RISMA</td>
      <td>14 326 947</td>
      <td>114,90</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>246 924 931,55</td>
      <td>0,0015</td>
    </tr>
    <tr>
      <th>40</th>
      <td>MA0000010340</td>
      <td>CTM</td>
      <td>1 225 978</td>
      <td>677,20</td>
      <td>0,25</td>
      <td>1,00</td>
      <td>207 558 075,40</td>
      <td>0,0012</td>
    </tr>
    <tr>
      <th>41</th>
      <td>MA0000011678</td>
      <td>M2M Group</td>
      <td>647 777</td>
      <td>850,00</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>192 713 657,50</td>
      <td>0,0012</td>
    </tr>
    <tr>
      <th>42</th>
      <td>MA0000010936</td>
      <td>ALUMINIUM DU MAROC</td>
      <td>465 954</td>
      <td>1 430,00</td>
      <td>0,25</td>
      <td>1,00</td>
      <td>166 578 555,00</td>
      <td>0,0010</td>
    </tr>
    <tr>
      <th>43</th>
      <td>MA0000011942</td>
      <td>ENNAKL</td>
      <td>30 000 000</td>
      <td>37,10</td>
      <td>0,10</td>
      <td>1,00</td>
      <td>111 300 000,00</td>
      <td>0,0007</td>
    </tr>
    <tr>
      <th>44</th>
      <td>MA0000011587</td>
      <td>FENIE BROSSETTE</td>
      <td>1 438 984</td>
      <td>186,00</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>93 677 858,40</td>
      <td>0,0006</td>
    </tr>
    <tr>
      <th>45</th>
      <td>MA0000011140</td>
      <td>NEXANS MAROC</td>
      <td>2 243 520</td>
      <td>200,00</td>
      <td>0,20</td>
      <td>1,00</td>
      <td>89 740 800,00</td>
      <td>0,0005</td>
    </tr>
    <tr>
      <th>46</th>
      <td>MA0000012106</td>
      <td>S.M MONETIQUE</td>
      <td>812 070</td>
      <td>210,00</td>
      <td>0,40</td>
      <td>1,00</td>
      <td>68 213 880,00</td>
      <td>0,0004</td>
    </tr>
    <tr>
      <th>47</th>
      <td>MA0000012114</td>
      <td>AFRIC INDUSTRIES SA</td>
      <td>291 500</td>
      <td>346,00</td>
      <td>0,50</td>
      <td>1,00</td>
      <td>50 429 500,00</td>
      <td>0,0003</td>
    </tr>
    <tr>
      <th>48</th>
      <td>MA0000011447</td>
      <td>MED PAPER</td>
      <td>2 582 555</td>
      <td>33,50</td>
      <td>0,45</td>
      <td>1,00</td>
      <td>38 932 016,63</td>
      <td>0,0002</td>
    </tr>
    <tr>
      <th>49</th>
      <td>MA0000011843</td>
      <td>STOKVIS NORD AFRIQUE</td>
      <td>9 195 150</td>
      <td>20,25</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>27 930 268,13</td>
      <td>0,0002</td>
    </tr>
    <tr>
      <th>50</th>
      <td>MA0000012056</td>
      <td>STROC INDUSTRIE</td>
      <td>1 248 515</td>
      <td>73,23</td>
      <td>0,30</td>
      <td>1,00</td>
      <td>27 428 626,04</td>
      <td>0,0002</td>
    </tr>
    <tr>
      <th>51</th>
      <td>MA0000011868</td>
      <td>CARTIER SAADA</td>
      <td>5 265 000</td>
      <td>34,05</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>26 890 987,50</td>
      <td>0,0002</td>
    </tr>
    <tr>
      <th>52</th>
      <td>MA0000011579</td>
      <td>INVOLYS</td>
      <td>382 716</td>
      <td>138,00</td>
      <td>0,35</td>
      <td>1,00</td>
      <td>18 485 182,80</td>
      <td>0,0001</td>
    </tr>
    <tr>
      <th>53</th>
      <td>MA0000011777</td>
      <td>DELATTRE LEVIVIER MAROC</td>
      <td>1 250 000</td>
      <td>51,36</td>
      <td>0,15</td>
      <td>1,00</td>
      <td>9 630 000,00</td>
      <td>0,0001</td>
    </tr>
    <tr>
      <th>54</th>
      <td>MA0000011132</td>
      <td>IB MAROC.COM</td>
      <td>417 486</td>
      <td>46,73</td>
      <td>0,45</td>
      <td>1,00</td>
      <td>8 779 104,35</td>
      <td>0,0001</td>
    </tr>
    <tr>
      <th>55</th>
      <td></td>
      <td>Total</td>
      <td>2 626 647 303,00</td>
      <td></td>
      <td></td>
      <td></td>
      <td>166 072 820 493,20</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>

