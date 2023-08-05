Price-Fetch: Real time Stock and Option tools
--------------------------------------------

Price-Fetch is a Python 3 library for monitoring and analyzing real time Stock and
Option data. Quotes are provided from the Yahoo Finance API and Google Finance API.
Price-Fetch requires minimal input from the user, it uses available online data to
calculate option greeks and even scrapes the US Treasury website to get the current risk free rate.

Authors
-------

Devesh Todarwal - <todarwal.devesh@gmail.com>
Rutuvi Narang   - <rutuvinarang@gmail.com>

Usage
-----

Stocks:

.. code-block:: Python

  from pricefetch import Stock, Call, Put

  >>> s = Stock('AAPL')
  >>> c
  96.44
  >>> s.price
  96.48
  >>> s.change
  -0.35
  >>> s.last_trade
  '21 Jan 2016 13:32:12'

Options:

.. code-block:: Python

  >>> g = Call('GOOG', d=12, m=2, y=2016, strike=700)
  >>> g.price
  38.2
  >>> g.implied_volatility()
  0.49222968442691889
  >>> g.delta()
  0.56522039722040063
  >>> g.vega()
  0.685034827159825
  >>> g.underlying.price
  706.59

Alternative construction:

.. code-block:: Python

  >>> g = Call('GOOG', d=12, m=2, y=2016)
  >>> g
  Call(ticker=GOOG, expiration='12-02-2016')
  >>> g.strikes
  (580, 610, 620, 630, 640, 650, 660, 670, 680, 690, 697.5, 700, 702.5, 707.5, 710, 712.5, 715, 720, ...)
  >>> g.set_strike(712.5)
  >>> g
  Call(ticker=GOOG, expiration='12-02-2016', strike=712.5)

or

.. code-block:: Python

  >>> g = Put("GOOG")
  'No options listed for given date, using 22-01-2016 instead'
  >>> g.expirations
  ['22-01-2016', '29-01-2016', '05-02-2016', '12-02-2016', '19-02-2016', '26-02-2016', '04-03-2016', ...]
  >>> g
  Put(ticker=GOOG, expiration='22-01-2016')

Yahoo Finance Support (keep in mind that YF quotes might be delayed):

.. code-block:: Python

    >>> apple = Stock('AAPL', source='yahoo')
    >>> call = Call('AAPL', strike=apple.price, source='yahoo')
    No options listed for given date, using '26-05-2017' instead
    No option for given strike, using 155 instead

Download historical data (requires pandas)

.. code-block:: Python

    s = Stock('BTC-USD')
    >>> df = s.historical(days_back=30, frequency='d')
    >>> df
             Date          Open          High           Low         Close     Adj Close       Volume
    0  2021-10-05  49174.960938  51839.984375  49072.839844  51514.812500  51514.812500  35873904236
    1  2021-10-06  51486.664063  55568.464844  50488.191406  55361.449219  55361.449219  49034730168
    2  2021-10-07  55338.625000  55338.625000  53525.468750  53805.984375  53805.984375  36807860413
    3  2021-10-08  53802.144531  55922.980469  53688.054688  53967.847656  53967.847656  34800873924
    4  2021-10-09  53929.781250  55397.945313  53735.144531  54968.222656  54968.222656  32491211414
    5  2021-10-10  54952.820313  56401.304688  54264.257813  54771.578125  54771.578125  39527792364
    6  2021-10-11  54734.125000  57793.039063  54519.765625  57484.789063  57484.789063  42637331698
    7  2021-10-12  57526.832031  57627.878906  54477.972656  56041.058594  56041.058594  41083758949
    8  2021-10-13  56038.257813  57688.660156  54370.972656  57401.097656  57401.097656  41684252783
    9  2021-10-14  57372.832031  58478.734375  56957.074219  57321.523438  57321.523438  36615791366
    10 2021-10-15  57345.902344  62757.128906  56868.144531  61593.949219  61593.949219  51780081801
    11 2021-10-16  61609.527344  62274.476563  60206.121094  60892.179688  60892.179688  34250964237
    12 2021-10-17  60887.652344  61645.523438  59164.468750  61553.617188  61553.617188  29032367511
    13 2021-10-18  61548.804688  62614.660156  60012.757813  62026.078125  62026.078125  38055562075
    14 2021-10-19  62043.164063  64434.535156  61622.933594  64261.992188  64261.992188  40471196346
    15 2021-10-20  64284.585938  66930.390625  63610.675781  65992.835938  65992.835938  40788955582
    16 2021-10-21  66002.234375  66600.546875  62117.410156  62210.171875  62210.171875  45908121370
    17 2021-10-22  62237.890625  63715.023438  60122.796875  60692.265625  60692.265625  38434082775
    18 2021-10-23  60694.628906  61743.878906  59826.523438  61393.617188  61393.617188  26882546034
    19 2021-10-24  61368.343750  61505.804688  59643.343750  60930.835938  60930.835938  27316183882
    20 2021-10-25  60893.925781  63729.324219  60691.800781  63039.824219  63039.824219  31064911614
    21 2021-10-26  63032.761719  63229.027344  59991.160156  60363.792969  60363.792969  34878965587
    22 2021-10-27  60352.000000  61435.183594  58208.187500  58482.386719  58482.386719  43657076893
    23 2021-10-28  58470.730469  62128.632813  58206.917969  60622.136719  60622.136719  45257083247
    24 2021-10-29  60624.871094  62927.609375  60329.964844  62227.964844  62227.964844  36856881767
    25 2021-10-30  62239.363281  62330.144531  60918.386719  61888.832031  61888.832031  32157938616
    26 2021-10-31  61850.488281  62406.171875  60074.328125  61318.957031  61318.957031  32241199927
    27 2021-11-01  61320.449219  62419.003906  59695.183594  61004.406250  61004.406250  36150572843
    28 2021-11-02  60963.253906  64242.792969  60673.054688  63226.402344  63226.402344  37746665647
    29 2021-11-03  63254.335938  63516.937500  61184.238281  62970.046875  62970.046875  36124731509
    30 2021-11-04  62898.691406  63088.773438  61446.257813  61863.878906  61863.878906  35562352640


Installation
------------
Simply

.. code-block:: bash

    $ pip install wallstreet


# API Attributes

Stock Attributes
----------------

- ticker
- price
- id
- exchange
- last_trade
- change   (change in currency)
- cp   (percentage change)


Option Attributes and Methods
-----------------------------

- strike
- expiration
- underlying  (underlying stock object)
- ticker
- bid
- ask
- price (option price)
- id
- exchange
- change  (in currency)
- cp  (percentage change)
- volume
- open_interest
- code
- expirations (list of possible expiration dates for option chain)
- strikes (list of possible strike prices)

- set_strike()
- implied_volatility()
- delta()
- gamma()
- vega()
- theta()
- rho()
