#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Module: lib.indicators
Purpose: AutoTrader custom indicators library
Author: Kieran Mackle
'''

from finta import TA
import numpy as np
import pandas as pd


def supertrend(data, period = 10, ATR_multiplier = 3.0, source=None):
    ''' Based on the SuperTrend indicator by KivancOzbilgic on TradingView '''
    
    if source is None:
        source = (data.High.values + data.Low.values) / 2
    
    # Calculate ATR
    atr             = TA.ATR(data, period)
    
    up              = source - (ATR_multiplier*atr)
    up_list         = [up[0]]
    up_times        = [data.index[0]]
    N_up            = 0
    
    dn              = source + (ATR_multiplier*atr)
    dn_list         = [dn[0]]
    dn_times        = [data.index[0]]
    N_dn            = 0
    
    trend           = 1
    trend_list      = [trend]
    
    for i in range(1, len(data)):
        
        if trend == 1:
            if data.Close.values[i] > max(up[N_up:i]):
                up_list.append(max(up[N_up:i]))
                up_times.append(data.index[i])
                
                dn_list.append(np.nan)
                dn_times.append(data.index[i])
                
            else: 
                trend = -1
                N_dn = i
                dn_list.append(dn[i])
                dn_times.append(data.index[i])
                
                up_list.append(np.nan)
                up_times.append(data.index[i])
                
        else:
            if data.Close.values[i] < min(dn[N_dn:i]):
                dn_list.append(min(dn[N_dn:i]))
                dn_times.append(data.index[i])
                
                up_list.append(np.nan)
                up_times.append(data.index[i])
                
            else:
                trend = 1
                N_up = i
                up_list.append(up[i])
                up_times.append(data.index[i])
                
                dn_list.append(np.nan)
                dn_times.append(data.index[i])
        
        trend_list.append(trend)
    
    # up_trend = pd.DataFrame({'uptrend': up_list}, index = up_times)
    # dn_trend = pd.DataFrame({'downtrend': dn_list}, index = dn_times)
    
    supertrend_df = pd.DataFrame({'uptrend': up_list,
                                  'downtrend': dn_list,
                                  'trend': trend_list}, 
                                 index = up_times)
    
    return supertrend_df


def stoch_rsi(data, K_period=3, D_period=3, RSI_length=14, Stochastic_length=14):

    rsi1 = TA.RSI(data, period=RSI_length)
    stoch = stochastic(rsi1, rsi1, rsi1, Stochastic_length)
    
    K = sma(stoch, K_period)
    D = sma(K, D_period)
    
    return K, D


def stochastic(high, low, close, period=14):
    
    K = np.zeros(len(high))
    
    for i in range(period, len(high)):
        low_val     = min(low[i-period+1:i+1])
        high_val    = max(high[i-period+1:i+1])
        
        K[i]        = 100 * (close[i] - low_val)/(high_val - low_val)
        
    return K
    

def sma(data, period=14):
    
    sma_list = []
    
    for i in range(len(data)):
        average = sum(data[i-period+1:i+1])/period
        sma_list.append(average)
    
    return sma_list


def ema(data, period=14, smoothing=2):
    
    ema = [sum(data[:period]) / period]
    
    for price in data[period:]:
        ema.append((price * (smoothing / (1 + period))) + ema[-1] * (1 - (smoothing / (1 + period))))
    
    for i in range(period-1):
        ema.insert(0, np.nan)
    
    return ema


def true_range(data, period=14):
    high_low = data['High'] - data['Low']
    high_close = np.abs(data['High'] - data['Close'].shift())
    low_close = np.abs(data['Low'] - data['Close'].shift())
    
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    
    return true_range


def atr(data, period=14):
    
    tr = true_range(data, period)
    
    atr = tr.rolling(period).sum()/period
    
    return atr


def rsi():
    return

def crossover(list_1, list_2):
    ''' 
    Returns a list of length len(list_1) with 1 when list_1 crosses above
    list_2 and -1 when list_1 crosses below list_2.
    '''
    
    sign_list = []
    for i in range(len(list_1)):
        if np.isnan(list_1[i]):
            sign_list.append(np.nan)
        else:
            difference = list_1[i] - list_2[i]
            if difference < 0:
                sign_list.append(-1)
            else:
                sign_list.append(1)
    
    crossover_list = [0]
    
    for i in range(1, len(sign_list)):
        if sign_list[i] - sign_list[i-1] != 0:
            val = sign_list[i]
        else:
            val = 0
        
        crossover_list.append(val)

    return crossover_list


def cross_values(a, b, ab_crossover):
    cross_point_list = [0]
    last_cross_point = 0
    for i in range(1, len(ab_crossover)):
        if ab_crossover[i] != 0:
            i0 = 0
            m_a = a[i] - a[i-1]
            m_b = b[i] - b[i-1]
            ix = (b[i-1] - a[i-1])/(m_a-m_b) + i0
            
            cross_point = m_a*(ix - i0) + a[i-1]
            
            last_cross_point = cross_point
            
        else:
            cross_point = last_cross_point #0
        
        cross_point_list.append(cross_point)
    
    # Replace nans with 0
    cross_point_list = [0 if x!=x  else x for x in cross_point_list]
    
    return cross_point_list


def candles_between_crosses(cross_list):
    '''
    Returns candles since last cross
    
    
    Behaviour:
    in:  [0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1]
    out: [1, 2, 0, 1, 2, 3,  0, 1, 2, 3, 4, 5, 0]
    '''
    
    count = 0
    count_list = []
    
    for i in range(len(cross_list)):

        if cross_list[i] == 0:
            # Change in signal - reset count
            count += 1
        else:
            count = 0
        
        count_list.append(count)
    
    return count_list


def bullish_engulfing(data, detection = None):
    ''' Bullish engulfing pattern detection. '''
    
    if detection == "SMA50":
        sma50       = sma(data.Close.values, 50)
        
        down_trend  = np.where(data.Close.values < sma50, True, False)
        up_trend    = np.where(data.Close.values > sma50, True, False)
        
    elif detection == "SMA50/200":
        sma50       = sma(data.Close.values, 50)
        sma200      = sma(data.Close.values, 200)
        
        down_trend  = np.where((data.Close.values < sma50) & 
                               (data.Close.values < sma200), 
                               True, False)
        up_trend    = np.where((data.Close.values > sma50) & 
                               (data.Close.values > sma200), 
                               True, False)
    else:
        down_trend  = np.full(len(data), True)
        up_trend    = np.full(len(data), True)
    
    body_len        = 14    # ema depth for bodyAvg
    shadow_pc       = 100.0   # size of shadows 
    doji_pc         = 5.0
    shadow_factor   = 2.0 # number of times shadow dominates candle body
    
    body_high       = np.maximum(data.Close.values, data.Open.values)
    body_low        = np.minimum(data.Close.values, data.Open.values)
    body            = body_high - body_low
    
    body_avg        = ema(body, body_len)
    short_body      = body < body_avg
    long_body       = body > body_avg
    up_shadow       = data.High.values - body_high
    down_shadow     = body_low - data.Low.values
    
    has_up_shadow   = up_shadow > (shadow_pc / 100 * body)
    has_dn_shadow   = down_shadow > (shadow_pc / 100 * body)
    white_body      = data.Open.values < data.Close.values
    black_body      = data.Open.values > data.Close.values
    candle_range    = data.High.values - data.Low.values
    
    inside_bar = [False]
    for i in range(1, len(data)):
        val  = (body_high[i-1] > body_high[i]) and (body_low[i-1] < body_low[i])
        inside_bar.append(val)
        
    body_mid        = body/2 + body_low
    shadow_equals   = (up_shadow == down_shadow) | \
                          (
                              ((abs(up_shadow - down_shadow) / down_shadow * 100) < shadow_pc) & \
                              ((abs(down_shadow - up_shadow) / up_shadow * 100) < shadow_pc)
                          )
    doji_body       = (candle_range > 0) & (body <= candle_range * doji_pc / 100)
    doji            = doji_body & shadow_equals
    
    
    engulfing_bullish = [False]
    for i in range(1, len(data)):
        condition = down_trend[i] & \
                    white_body[i] & \
                    long_body[i] & \
                    black_body[i-1] & \
                    short_body[i-1] & \
                    (data.Close.values[i] >= data.Open.values[i-1]) & \
                    (data.Open.values[i] <= data.Close.values[i-1]) & \
                    ((data.Close.values[i] > data.Open.values[i-1]) | (data.Open.values[i] < data.Close.values[i-1]))
        
        engulfing_bullish.append(condition)
        
    return engulfing_bullish


def bearish_engulfing(data, detection = None):
    ''' Bearish engulfing pattern detection. '''
    
    if detection == "SMA50":
        sma50       = sma(data.Close.values, 50)
        
        down_trend  = np.where(data.Close.values < sma50, True, False)
        up_trend    = np.where(data.Close.values > sma50, True, False)
        
    elif detection == "SMA50/200":
        sma50       = sma(data.Close.values, 50)
        sma200      = sma(data.Close.values, 200)
        
        down_trend  = np.where((data.Close.values < sma50) & 
                               (data.Close.values < sma200), 
                               True, False)
        up_trend    = np.where((data.Close.values > sma50) & 
                               (data.Close.values > sma200), 
                               True, False)
    else:
        down_trend  = np.full(len(data), True)
        up_trend    = np.full(len(data), True)
    
    body_len        = 14    # ema depth for bodyAvg
    shadow_pc       = 100.0   # size of shadows 
    doji_pc         = 5.0
    shadow_factor   = 2.0 # number of times shadow dominates candle body
    
    body_high       = np.maximum(data.Close.values, data.Open.values)
    body_low        = np.minimum(data.Close.values, data.Open.values)
    body            = body_high - body_low
    
    body_avg        = ema(body, body_len)
    short_body      = body < body_avg
    long_body       = body > body_avg
    up_shadow       = data.High.values - body_high
    down_shadow     = body_low - data.Low.values
    
    has_up_shadow   = up_shadow > (shadow_pc / 100 * body)
    has_dn_shadow   = down_shadow > (shadow_pc / 100 * body)
    white_body      = data.Open.values < data.Close.values
    black_body      = data.Open.values > data.Close.values
    candle_range    = data.High.values - data.Low.values
    
    inside_bar = [False]
    for i in range(1, len(data)):
        val  = (body_high[i-1] > body_high[i]) and (body_low[i-1] < body_low[i])
        inside_bar.append(val)
        
    body_mid        = body/2 + body_low
    shadow_equals   = (up_shadow == down_shadow) | \
                          (
                              ((abs(up_shadow - down_shadow) / down_shadow * 100) < shadow_pc) & \
                              ((abs(down_shadow - up_shadow) / up_shadow * 100) < shadow_pc)
                          )
    doji_body       = (candle_range > 0) & (body <= candle_range * doji_pc / 100)
    doji            = doji_body & shadow_equals
    
    
    engulfing_bearish = [False]
    for i in range(1, len(data)):
        condition = up_trend[i] & \
                    black_body[i] & \
                    long_body[i] & \
                    white_body[i-1] & \
                    short_body[i-1] & \
                    (data.Close.values[i] <= data.Open.values[i-1]) & \
                    (data.Open.values[i] >= data.Close.values[i-1]) & \
                    ((data.Close.values[i] < data.Open.values[i-1]) | (data.Open.values[i] > data.Close.values[i-1]))
        
        engulfing_bearish.append(condition)
        
    return engulfing_bearish


def heikin_ashi(data):
    ''' 
        Calculates the Heikin-Ashi candlesticks from Japanese candlestick 
        data. 
    '''
    ha_close    = (data.Open + data.High + data.Low + data.Close)/4
    ha_open     = data.Open
    ha_low      = data.Low
    ha_high     = data.High
    
    for i in range(1, len(data)):
        ha_open[i]  = (data.Open[i-1] + data.Close[i-1])/2
        ha_low[i]   = min(data.Low[i], ha_open[i], ha_close[i])
        ha_high[i]  = max(data.High[i], ha_open[i], ha_close[i])
    
    ha_data = pd.concat([ha_open, ha_high, ha_low, ha_close], axis=1)
    ha_data.columns = ['Open', 'High', 'Low', 'Close']
    
    return ha_data
 

def find_swings(data, use_body = False):
    '''
        Locates the recent swings in price and returns a rolling list of 
        swing prices.
    '''
    
    # TODO - include resampling option to find swings on higher timeframe
    
    # use_body flag currently not implemented. Idea is to use body close/open
    # instead of high/low (wicks) of candle for swings.
    
    # oc2     = (data.Open.values + data.Close.values)/2
    hl2     = (data.High.values + data.Low.values)/2
    n       = 2
    EMA     = ema(hl2, n)
    
    grad    = np.gradient(EMA)
    
    swings   = np.zeros(len(grad))
    for i in range(1, len(grad)):
        if not np.isnan(grad[i-1]):
            if np.sign(grad[i]) != np.sign(grad[i-1]):
                swings[i] = -np.sign(grad[i])

    swing_df = pd.DataFrame(data=swings, index=data.index, columns=['swing'])
    
    low_list    = []
    high_list   = []
    for i in range(len(data)):
        if swing_df.swing[i] == -1:
            low_list.append(min(data.Low.values[i-1:i+2]))
            high_list.append(0)
        elif swing_df.swing[i] == 1:
            high_list.append(max(data.High.values[i-1:i+2]))
            low_list.append(0)
        else:
            low_list.append(0)
            high_list.append(0)
    
    swings_list     = merge_signals(low_list, high_list)
    last_swing      = rolling_signal_list(swings_list)
    last_swing[0:n] = list(data.High.values[0:n])
    
    # Need to return both a last swing low and last swing high list
    last_low        = rolling_signal_list(low_list)
    last_low[0:n]   = list(data.Low.values[0:n])
    last_high       = rolling_signal_list(high_list)
    last_high[0:n]  = list(data.High.values[0:n])
    
    swings          = pd.DataFrame(data={'Highs': last_high, 
                                         'Lows' : last_low,
                                         'Last' : last_swing},
                                   index = data.index)
    
    return swings
    

def rolling_signal_list(signals):
        ''' 
            Returns a list which maintains the previous signal, until a new 
            signal is given.
            
            [0,1,0,0,0,-1,0,0,1,0,0] ->  [0,1,1,1,1,-1,-1,-1,1,1,1]
            
        '''
        
        rolling_signals = [0]
        last_signal     = rolling_signals[0]
        
        for i in range(1, len(signals)):
            if signals[i] != 0:
                last_signal = signals[i]
            
            rolling_signals.append(last_signal)
        
        return rolling_signals

def unroll_signal_list(signals):
    ''' Unrolls a signal list. '''
    new_list = np.zeros(len(signals))
    
    for i in range(len(signals)):
        if signals[i] != signals[i-1]:
            new_list[i] = signals[i]
    
    return new_list


def merge_signals(signal_1, signal_2):
     ''' 
         Returns a single signal list which has merged two signal lists. 
     '''
     
     merged_signal_list = signal_1
     
     for i in range(len(signal_1)):
         if signal_2[i] != 0:
             merged_signal_list[i] = signal_2[i]
     
     return merged_signal_list


def ha_candle_run(ha_data):
    '''
        Returns a list for the number of consecutive green and red 
        Heikin-Ashi candles.
        
    '''
    green_candle    = np.where(ha_data.Close - ha_data.Open > 0, 1, 0)
    red_candle      = np.where(ha_data.Close - ha_data.Open < 0, 1, 0)
    
    green_run   = []
    red_run     = []
    
    green_sum   = 0
    red_sum     = 0
    
    for i in range(len(ha_data)):
        if green_candle[i] == 1:
            green_sum += 1
        else:
            green_sum = 0
        
        if red_candle[i] == 1:
            red_sum += 1
        else:
            red_sum = 0
        
        green_run.append(green_sum)
        red_run.append(red_sum)
        
    return green_run, red_run


def build_grid_price_levels(grid_origin, grid_space, grid_levels, 
                            grid_price_space=None, pip_value=0.0001):
    
    # Calculate grid spacing in price units
    if grid_price_space is None:
        grid_price_space = grid_space*pip_value
    
    # Generate order_limit_price list 
    grid_price_levels = np.linspace(grid_origin - grid_levels*grid_price_space, 
                                     grid_origin + grid_levels*grid_price_space, 
                                     2*grid_levels + 1)
    
    return grid_price_levels

def build_grid(grid_origin, grid_space, grid_levels, order_direction, 
               order_type='stop-limit', grid_price_space=None, pip_value=0.0001, 
               take_distance=None, stop_distance=None, stop_type=None):
    '''
    grid_origin: origin of grid, specified as a price
    grid_space: spacing between grid levels, specified as pip distance
    grid_levels: number of grid levels either side of origin
    order_direction: the direction of each grid level order (1 for long, -1 for short)
    order_type: the order type of each grid level order
    '''
    # TODO - could add a limit price buffer, then use it to move the limit price
    # slightly away from the stop price
    
    # Check if stop_distance was provided without a stop_type
    if stop_distance is not None and stop_type is None:
        # set stop_type to 'limit' by default
        stop_type = 'limit'
    
    # Calculate grid spacing in price units
    if grid_price_space is None:
        grid_price_space = grid_space*pip_value
    
    # Generate order_limit_price list 
    order_limit_prices = np.linspace(grid_origin - grid_levels*grid_price_space, 
                                     grid_origin + grid_levels*grid_price_space, 
                                     2*grid_levels + 1)
    
    # Construct nominal order
    nominal_order = {}
    nominal_order["order_type"]         = order_type
    nominal_order["direction"]          = order_direction
    nominal_order["stop_distance"]      = stop_distance
    nominal_order["stop_type"]          = stop_type
    nominal_order["take_distance"]      = take_distance
    
    # Build grid
    grid = {}

    for order, limit_price in enumerate(order_limit_prices):
        grid[order] = nominal_order.copy()
        grid[order]["order_stop_price"]  = order_limit_prices[order]
        grid[order]["order_limit_price"] = order_limit_prices[order]
        
    
    return grid

def merge_grid_orders(grid_1, grid_2):
    '''
    Merges grid dictionaries into one and re-labels order numbers so each
    order number is unique.
    '''
    # TODO - use **args/**kwargs to generalise how many grids are inputted
    order_offset = len(grid_1)
    grid = grid_1.copy()
    
    for order_no in grid_2:
        grid[order_no + order_offset] = grid_2[order_no]
    
    return grid
    
def last_level_crossed(data, base):
    ''' 
    Returns a list containing the last grid level touched.
    The grid levels are determined by the base input variable, 
    which corresponds to the pip_space x pip_value.
    '''
    # base = 20*0.0001
    
    last_level_crossed = np.nan
    levels_crossed = []
    for i in range(len(data)):
        high = data.High.values[i]
        low = data.Low.values[i]
        
        upper_prices = []
        lower_prices = []
        
        for price in [high, low]:    
            upper_prices.append(base*np.ceil(price/base))
            lower_prices.append(base*np.floor(price/base))
        
        if lower_prices[0] != lower_prices[1]:
            # Candle has crossed a level
            last_level_crossed = lower_prices[0]
        
        levels_crossed.append(last_level_crossed)
    
    return levels_crossed


def build_multiplier_grid(origin, direction, multiplier, no_levels, precision, spacing):
    '''
    Constructs grid levels with a multiplying grid space.
    
        Parameters:
            origin (float): origin of grid as price amount.
            
            direction (int): direction of grid (1 for long, -1 for short).
            
            multiplier (float): grid space multiplier when price moves away 
            from the origin opposite to direction.
            
            no_levels (int): number of levels to calculate either side of the 
            origin.
            
            precision (int): instrument precision (eg. 4 for most currencies, 2 
            for JPY).
            
            spacing (float): spacing of grid in price units.
    '''
    
    levels = [i for i in range(1, no_levels + 1)]

    pos_levels = [round(origin + direction*spacing*i, precision) for i in levels]
    neg_spaces = [spacing*multiplier**(i) for i in levels]
    neg_levels = []
    prev_neg_level = origin
    for i in range(len(levels)):
        next_neg_level = prev_neg_level - direction*neg_spaces[i]
        prev_neg_level = next_neg_level
        neg_levels.append(round(next_neg_level, precision))
    
    grid = neg_levels + [origin] + pos_levels
    grid.sort()
    
    return grid


def last_level_touched(data, grid):
    '''
    Calculates the grid levels touched by price data.
    '''
    
    # initialise with nan
    last_level_crossed = np.nan 
    
    levels_touched = []
    for i in range(len(data)):
        high = data.High.values[i]
        low = data.Low.values[i]
        
        upper_prices = []
        lower_prices = []
        
        for price in [high, low]:    
            # Calculate level above
            upper_prices.append(grid[next(x[0] for x in enumerate(grid) if x[1] > price)])
            
            # calculate level below
            first_level_below_index = next(x[0] for x in enumerate(grid[::-1]) if x[1] < price)
            lower_prices.append(grid[-(first_level_below_index+1)])
        
        if lower_prices[0] != lower_prices[1]:
            # Candle has crossed a level, since the level below the candle high
            # is different to the level below the candle low.
            # This essentially means the grid level is between candle low and high.
            last_level_crossed = lower_prices[0]
        
        levels_touched.append(last_level_crossed)
    
    return levels_touched


# def TDI(data):
#     rsiPeriod = input(11, minval = 1, title = "RSI Period")
#     bandLength = input(31, minval = 1, title = "Band Length")
#     lengthrsipl = input(1, minval = 0, title = "Fast MA on RSI")
#     lengthtradesl = input(9, minval = 1, title = "Slow MA on RSI")
    
#     src = close                                                             // Source of Calculations (Close of Bar)
#     r = rsi(src, rsiPeriod)                                                 // RSI of Close
#     ma = sma(r, bandLength)                                                 // Moving Average of RSI [current]
#     offs = (1.6185 * stdev(r, bandLength))                                  // Offset
#     up = ma + offs                                                          // Upper Bands
#     dn = ma - offs                                                          // Lower Bands
#     mid = (up + dn) / 2                                                     // Average of Upper and Lower Bands
#     fastMA = sma(r, lengthrsipl)                                            // Moving Average of RSI 2 bars back
#     slowMA = sma(r, lengthtradesl)                                          // Moving Average of RSI 7 bars back
    
#     hline(30)                                                               // Oversold
#     hline(50)                                                               // Midline
#     hline(70)                                                               // Overbought
    
#     upl = plot(up, "Upper Band", color = blue)                              // Upper Band
#     dnl = plot(dn, "Lower Band", color = blue)                              // Lower Band
#     midl = plot(mid, "Middle of Bands", color = orange, linewidth = 2)      // Middle of Bands
    
#     plot(slowMA, "Slow MA", color=green, linewidth=2)                       // Plot Slow MA
#     plot(fastMA, "Fast MA", color=red, linewidth=2)                         // Plot Fast MA
    
#     fill(upl, midl, red, transp=90)                                         // Fill Upper Half Red
#     fill(midl, dnl, green, transp=90)                                       // Fill Lower Half Green



