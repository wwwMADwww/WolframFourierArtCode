from math import sin;
from FourierFunc import Coordinates;
from FourierFunc import FourierFuncBase;
from FourierFunc import FourierSeriesBase;

# This file is autogenerated by WolframFourierArtCode

class SkullFourierFunc(FourierFuncBase):
    def _init_series(self):
        self._series = [
            _SkullFourierFunc00(),
            _SkullFourierFunc01(),
            _SkullFourierFunc02(),
            _SkullFourierFunc03(),
            _SkullFourierFunc04(),
            _SkullFourierFunc05(),
            _SkullFourierFunc06(),
		]


class _SkullFourierFunc00(FourierSeriesBase):

    min_t = 72.25663103256524
    max_t = 84.82300164692441
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = (-31.0/5.0 * sin(20.0/13.0 - 16.0 * t) - 67.0/15.0 * sin(26.0/17.0 - 15.0 * t) - 13.0/6.0 * sin(35.0/23.0 - 13.0 * t) - 13.0/8.0 * sin(23.0/15.0 - 12.0 * t) - 46.0/31.0 * sin(23.0/15.0 - 9.0 * t) + 764.0/9.0 * sin(t + 11.0/7.0) + 6.0/5.0 * sin(2.0 * t + 21.0/13.0) + 41.0/4.0 * sin(3.0 * t + 11.0/7.0) + 3.0/8.0 * sin(4.0 * t + 5.0/3.0) + 9.0/7.0 * sin(5.0 * t + 8.0/5.0) + 12.0/13.0 * sin(6.0 * t + 13.0/8.0) + 9.0/14.0 * sin(7.0 * t + 14.0/3.0) + 3.0/10.0 * sin(8.0 * t + 14.0/3.0) + 8.0/15.0 * sin(10.0 * t + 32.0/21.0) + 1.0/4.0 * sin(11.0 * t + 13.0/9.0) + 4.0/7.0 * sin(14.0 * t + 8.0/5.0) + 50.0/7.0 * sin(17.0 * t + 21.0/13.0) + 9.0/10.0 * sin(18.0 * t + 17.0/10.0) + 21.0/8.0 * sin(19.0 * t + 13.0/8.0) + 6.0/7.0 * sin(20.0 * t + 33.0/7.0) + 7.0/13.0 * sin(21.0 * t + 27.0/16.0) + 4.0/11.0 * sin(22.0 * t + 26.0/15.0) + 14.0/15.0 * sin(23.0 * t + 23.0/14.0) + 2.0/5.0 * sin(24.0 * t + 22.0/13.0) + 5.0/11.0 * sin(25.0 * t + 8.0/5.0) + 4.0/13.0 * sin(26.0 * t + 19.0/12.0) + 1.0/5.0 * sin(27.0 * t + 13.0/8.0) + 1.0/4.0 * sin(28.0 * t + 13.0/7.0) + 5.0/7.0 * sin(29.0 * t + 27.0/16.0) + 3.0/4.0 * sin(30.0 * t + 5.0/3.0) + 3.0/10.0 * sin(31.0 * t + 23.0/13.0) + 7.0/5.0 * sin(32.0 * t + 5.0/3.0) - 134.0/7.0)

        y = (-5.0/4.0 * sin(3.0/2.0 - 31.0 * t) - 2.0/5.0 * sin(10.0/7.0 - 28.0 * t) - 4.0/7.0 * sin(16.0/11.0 - 27.0 * t) - 4.0/7.0 * sin(17.0/11.0 - 25.0 * t) - 5.0/7.0 * sin(17.0/11.0 - 23.0 * t) - 20.0/19.0 * sin(20.0/13.0 - 21.0 * t) - 115.0/29.0 * sin(35.0/23.0 - 17.0 * t) - 74.0/9.0 * sin(26.0/17.0 - 16.0 * t) - 11.0/6.0 * sin(29.0/19.0 - 14.0 * t) - 16.0/13.0 * sin(37.0/25.0 - 13.0 * t) - 3.0/11.0 * sin(28.0/19.0 - 12.0 * t) - 9.0/13.0 * sin(14.0/9.0 - 10.0 * t) + 2.0/3.0 * sin(t + 13.0/8.0) + 175.0/16.0 * sin(2.0 * t + 11.0/7.0) + 27.0/16.0 * sin(3.0 * t + 11.0/7.0) + 23.0/4.0 * sin(4.0 * t + 19.0/12.0) + 3.0/11.0 * sin(5.0 * t + 37.0/8.0) + 11.0/8.0 * sin(6.0 * t + 8.0/5.0) + 8.0/7.0 * sin(7.0 * t + 8.0/5.0) + 3.0/7.0 * sin(8.0 * t + 37.0/8.0) + 1.0/14.0 * sin(9.0 * t + 41.0/9.0) + 7.0/11.0 * sin(11.0 * t + 19.0/12.0) + 5.0/3.0 * sin(15.0 * t + 19.0/12.0) + 11.0/5.0 * sin(18.0 * t + 8.0/5.0) + 3.0/14.0 * sin(19.0 * t + 17.0/10.0) + 5.0/4.0 * sin(20.0 * t + 8.0/5.0) + 2.0/3.0 * sin(22.0 * t + 28.0/17.0) + 11.0/17.0 * sin(24.0 * t + 13.0/8.0) + 1.0/9.0 * sin(26.0 * t + 11.0/9.0) + 5.0/16.0 * sin(29.0 * t + 51.0/11.0) + 19.0/18.0 * sin(30.0 * t + 13.0/8.0) + 23.0/14.0 * sin(32.0 * t + 5.0/3.0) - 4278.0/17.0)

        return Coordinates(x, y)

class _SkullFourierFunc01(FourierSeriesBase):

    min_t = 59.690260418206066
    max_t = 72.25663103256524
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = + (-1.0/7.0 * sin(10.0/7.0 - 26.0 * t) - 109.0/15.0 * sin(11.0/7.0 - 15.0 * t) - 9.0/17.0 * sin(13.0/9.0 - 11.0 * t) - 3.0/2.0 * sin(3.0/2.0 - 4.0 * t) + 449.0/5.0 * sin(t + 11.0/7.0) + 1.0/2.0 * sin(2.0 * t + 37.0/8.0) + 47.0/6.0 * sin(3.0 * t + 11.0/7.0) + 7.0/5.0 * sin(5.0 * t + 11.0/7.0) + 2.0/5.0 * sin(6.0 * t + 11.0/7.0) + 7.0/10.0 * sin(7.0 * t + 12.0/7.0) + 9.0/7.0 * sin(8.0 * t + 75.0/16.0) + 9.0/10.0 * sin(9.0 * t + 19.0/13.0) + 10.0/7.0 * sin(10.0 * t + 17.0/11.0) + 4.0/9.0 * sin(12.0 * t + 27.0/14.0) + 25.0/11.0 * sin(13.0 * t + 47.0/10.0) + 3.0/5.0 * sin(14.0 * t + 13.0/9.0) + 35.0/8.0 * sin(16.0 * t + 33.0/7.0) + 86.0/13.0 * sin(17.0 * t + 11.0/7.0) + 2.0/7.0 * sin(18.0 * t + 28.0/17.0) + 27.0/16.0 * sin(19.0 * t + 11.0/7.0) + 1.0/6.0 * sin(20.0 * t + 1.0/6.0) + 11.0/9.0 * sin(21.0 * t + 8.0/5.0) + 1.0/9.0 * sin(22.0 * t + 16.0/7.0) + 11.0/8.0 * sin(23.0 * t + 11.0/7.0) + 1.0/6.0 * sin(24.0 * t + 41.0/9.0) + 3.0/8.0 * sin(25.0 * t + 15.0/11.0) + 1.0/8.0 * sin(27.0 * t + 41.0/20.0) + 1.0/13.0 * sin(28.0 * t + 48.0/11.0) + 1.0/7.0 * sin(29.0 * t + 7.0/5.0) + 1.0/18.0 * sin(30.0 * t + 1.0/4.0) + 2.0/5.0 * sin(31.0 * t + 11.0/7.0) + 6.0/7.0 * sin(32.0 * t + 11.0/7.0) - 182.0/11.0)

        y = + (-19.0/9.0 * sin(14.0/9.0 - 31.0 * t) - 1.0/16.0 * sin(4.0/15.0 - 30.0 * t) - 17.0/10.0 * sin(3.0/2.0 - 21.0 * t) - 7.0/2.0 * sin(11.0/7.0 - 17.0 * t) - 135.0/14.0 * sin(11.0/7.0 - 16.0 * t) - 2.0/11.0 * sin(4.0/3.0 - 11.0 * t) + 9.0/8.0 * sin(t + 47.0/10.0) + 39.0/5.0 * sin(2.0 * t + 11.0/7.0) + 4.0/7.0 * sin(3.0 * t + 14.0/3.0) + 19.0/10.0 * sin(4.0 * t + 19.0/12.0) + 8.0/15.0 * sin(5.0 * t + 47.0/10.0) + 1.0/10.0 * sin(6.0 * t + 15.0/11.0) + 31.0/30.0 * sin(7.0 * t + 20.0/13.0) + 5.0/8.0 * sin(8.0 * t + 23.0/14.0) + 7.0/11.0 * sin(9.0 * t + 61.0/13.0) + 5.0/9.0 * sin(10.0 * t + 23.0/14.0) + 4.0/5.0 * sin(12.0 * t + 10.0/7.0) + 1.0/11.0 * sin(13.0 * t + 149.0/50.0) + 1.0/2.0 * sin(14.0 * t + 37.0/8.0) + 5.0/3.0 * sin(15.0 * t + 19.0/12.0) + 7.0/10.0 * sin(18.0 * t + 8.0/5.0) + 5.0/3.0 * sin(19.0 * t + 79.0/17.0) + 1.0/15.0 * sin(20.0 * t + 49.0/12.0) + 1.0/15.0 * sin(22.0 * t + 59.0/15.0) + 11.0/15.0 * sin(23.0 * t + 14.0/3.0) + 7.0/8.0 * sin(24.0 * t + 13.0/8.0) + 2.0/11.0 * sin(25.0 * t + 11.0/7.0) + 2.0/5.0 * sin(26.0 * t + 9.0/7.0) + 3.0/10.0 * sin(27.0 * t + 14.0/3.0) + 1.0/6.0 * sin(28.0 * t + 38.0/9.0) + 33.0/34.0 * sin(29.0 * t + 14.0/3.0) + 22.0/9.0 * sin(32.0 * t + 19.0/12.0) - 1446.0/7.0)

        return Coordinates(x, y)

class _SkullFourierFunc02(FourierSeriesBase):

    min_t = 47.12388980384689
    max_t = 59.690260418206066
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = + (-15.0/14.0 * sin(7.0/10.0 - 13.0 * t) - 13.0/9.0 * sin(13.0/10.0 - 11.0 * t) - 43.0/9.0 * sin(6.0/7.0 - 3.0 * t) + 2125.0/12.0 * sin(t + 13.0/7.0) + 3.0 * sin(2.0 * t + 8.0/11.0) + 35.0/8.0 * sin(4.0 * t + 31.0/21.0) + 11.0/12.0 * sin(5.0 * t + 59.0/14.0) + 16.0/7.0 * sin(6.0 * t + 7.0/3.0) + 35.0/12.0 * sin(7.0 * t + 34.0/9.0) + 7.0/9.0 * sin(8.0 * t + 52.0/17.0) + 26.0/11.0 * sin(9.0 * t + 59.0/14.0) + 2.0/5.0 * sin(10.0 * t + 17.0/9.0) + 4.0/11.0 * sin(12.0 * t + 17.0/5.0) - 495.0/31.0)

        y = + (-17.0/12.0 * sin(7.0/15.0 - 11.0 * t) - 3.0/10.0 * sin(13.0/11.0 - 10.0 * t) - 63.0/25.0 * sin(8.0/17.0 - 9.0 * t) - 29.0/9.0 * sin(15.0/14.0 - 7.0 * t) + 265.0/9.0 * sin(t + 37.0/11.0) + 641.0/8.0 * sin(2.0 * t + 15.0/7.0) + 139.0/12.0 * sin(3.0 * t + 75.0/19.0) + 246.0/17.0 * sin(4.0 * t + 19.0/7.0) + 65.0/9.0 * sin(5.0 * t + 61.0/13.0) + 26.0/7.0 * sin(6.0 * t + 16.0/5.0) + 5.0/7.0 * sin(8.0 * t + 61.0/14.0) + 2.0/13.0 * sin(12.0 * t + 151.0/50.0) + 12.0/7.0 * sin(13.0 * t + 64.0/63.0) - 1724.0/7.0)

        return Coordinates(x, y)

class _SkullFourierFunc03(FourierSeriesBase):

    min_t = 34.55751918948772
    max_t = 47.12388980384689
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = + (-9.0/4.0 * sin(1.0/13.0 - 4.0 * t) + 749.0/17.0 * sin(t + 19.0/12.0) + 6.0/13.0 * sin(2.0 * t + 17.0/12.0) + 29.0/11.0 * sin(3.0 * t + 30.0/29.0) + 5.0/16.0 * sin(5.0 * t + 26.0/9.0) + 11.0/15.0 * sin(6.0 * t + 15.0/16.0) - 224.0/13.0)

        y = + (-6.0/7.0 * sin(3.0/4.0 - 6.0 * t) - 4.0/5.0 * sin(4.0/7.0 - 5.0 * t) - 149.0/10.0 * sin(14.0/11.0 - 2.0 * t) + 309.0/7.0 * sin(t + 49.0/15.0) + 72.0/11.0 * sin(3.0 * t + 35.0/11.0) + 65.0/12.0 * sin(4.0 * t + 9.0/5.0) - 73.0)

        return Coordinates(x, y)

class _SkullFourierFunc04(FourierSeriesBase):

    min_t = 21.991148575128552
    max_t = 34.55751918948772
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = + (-11.0/5.0 * sin(11.0/15.0 - 2.0 * t) + 494.0/7.0 * sin(t + 11.0/4.0) + 23.0/9.0 * sin(3.0 * t + 37.0/19.0) + 8.0/9.0 * sin(4.0 * t + 8.0/17.0) + 1051.0/12.0)

        y = + (-22.0/9.0 * sin(10.0/19.0 - 3.0 * t) + 431.0/6.0 * sin(t + 35.0/8.0) + 12.0/5.0 * sin(2.0 * t + 29.0/9.0) + 3.0/2.0 * sin(4.0 * t + 31.0/11.0) + 179.0/4.0)

        return Coordinates(x, y)

class _SkullFourierFunc05(FourierSeriesBase):

    min_t = 9.42477796076938
    max_t = 21.991148575128552
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = + (-33.0/16.0 * sin(3.0/8.0 - 3.0 * t) + 1105.0/16.0 * sin(t + 27.0/7.0) + 53.0/10.0 * sin(2.0 * t + 17.0/6.0) + sin(4.0 * t + 18.0/13.0) - 799.0/6.0)

        y = + (-1088.0/15.0 * sin(7.0/8.0 - t) + 51.0/14.0 * sin(2.0 * t + 6.0/7.0) + 11.0/9.0 * sin(3.0 * t + 112.0/25.0) + 7.0/3.0 * sin(4.0 * t + 22.0/9.0) + 742.0/15.0)

        return Coordinates(x, y)

class _SkullFourierFunc06(FourierSeriesBase):

    min_t = 0
    max_t = 9.42477796076938
    
    def calc(self, t: float) -> Coordinates:
        if not (self.min_t <= t <= self.max_t):
            return None

        if sin(t/2) < 0:
            return None

        x = + (-2.0/9.0 * sin(11.0/9.0 - 21.0 * t) - 11.0/6.0 * sin(1.0/2.0 - 13.0 * t) - 2.0/9.0 * sin(7.0/11.0 - 11.0 * t) - 46.0/11.0 * sin(8.0/7.0 - 6.0 * t) - 37.0/6.0 * sin(1.0/7.0 - 5.0 * t) - 207.0/5.0 * sin(9.0/14.0 - 3.0 * t) + 1631.0/6.0 * sin(t + 19.0/10.0) + 216.0/11.0 * sin(2.0 * t + 48.0/13.0) + 37.0/4.0 * sin(4.0 * t + 31.0/7.0) + 74.0/13.0 * sin(7.0 * t + 31.0/8.0) + 13.0/11.0 * sin(8.0 * t + 27.0/8.0) + 29.0/4.0 * sin(9.0 * t + 49.0/11.0) + 103.0/26.0 * sin(10.0 * t + 29.0/9.0) + 13.0/8.0 * sin(12.0 * t + 63.0/62.0) + 24.0/13.0 * sin(14.0 * t + 4.0/3.0) + 5.0/2.0 * sin(15.0 * t + 3.0/10.0) + 2.0/3.0 * sin(16.0 * t + 3.0/10.0) + 13.0/14.0 * sin(17.0 * t + 19.0/15.0) + 7.0/6.0 * sin(18.0 * t + 33.0/16.0) + 5.0/6.0 * sin(19.0 * t + 51.0/26.0) + 3.0/8.0 * sin(20.0 * t + 49.0/16.0) + 11.0/12.0 * sin(22.0 * t + 43.0/10.0) - 183.0/11.0)

        y = + (-3.0/7.0 * sin(7.0/9.0 - 22.0 * t) - 21.0/22.0 * sin(13.0/11.0 - 20.0 * t) - 6.0/17.0 * sin(1.0/38.0 - 19.0 * t) - 9.0/13.0 * sin(11.0/8.0 - 13.0 * t) - 7.0 * sin(4.0/5.0 - 12.0 * t) - 7.0/5.0 * sin(10.0/7.0 - 11.0 * t) - 181.0/17.0 * sin(10.0/7.0 - 10.0 * t) + 3.0/10.0 * sin(21.0 * t) + 1167.0/5.0 * sin(t + 52.0/15.0) + 148.0/7.0 * sin(2.0 * t + 9.0/4.0) + 245.0/4.0 * sin(3.0 * t + 19.0/20.0) + 97.0/7.0 * sin(4.0 * t + 23.0/8.0) + 291.0/10.0 * sin(5.0 * t + 21.0/13.0) + 246.0/13.0 * sin(6.0 * t + 37.0/11.0) + 203.0/12.0 * sin(7.0 * t + 16.0/7.0) + 56.0/5.0 * sin(8.0 * t + 33.0/8.0) + 29.0/6.0 * sin(9.0 * t + 10.0/3.0) + 13.0/10.0 * sin(14.0 * t + 5.0/6.0) + 5.0/2.0 * sin(15.0 * t + 14.0/9.0) + 9.0/7.0 * sin(16.0 * t + 23.0/24.0) + 1.0/2.0 * sin(17.0 * t + 7.0/4.0) + 3.0/5.0 * sin(18.0 * t + 32.0/9.0) + 1678.0/13.0)

        return Coordinates(x, y)

