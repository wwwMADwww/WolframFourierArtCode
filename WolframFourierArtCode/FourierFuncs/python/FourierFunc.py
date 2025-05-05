from math import sin;
from math import pi as π;

class Coordinates:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class FourierFuncBase:

    _series = None

    min_t = None
    max_t = None
        
    def __init__(self):
        if type(self) is FourierFuncBase:
            raise Exception('FourierFuncBase is an abstract class and cannot be instantiated directly')
        self._init_series()
        self.min_t = self._series[-1].min_t
        self.max_t = self._series[ 0].max_t

    def get_series(self):
        return self._series


    def calc_normal(self, t: float) -> Coordinates:
        denorm_t = self._map_range(t, 0.0, 1.0, self.min_t, self.max_t)

        return self.calc(denorm_t)


    def calc(self, t: float) -> Coordinates:
        series = next((x for x in self._series if x.min_t <= t <= x.max_t), None)
        if series == None:
            return None

        return series.calc(t)


    def _init_series(self):
        return NotImplementedError


    def _map_range(self, value, source_min, source_max, target_min, target_max):
        scale = (target_max - target_min) / (source_max - source_min)
        return target_min + (value - source_min) * scale



class FourierSeriesBase:

    min_t = None
    max_t = None

    def __init__(self):
        if type(self) is FourierSeriesBase:
            raise Exception('FourierSeriesBase is an abstract class and cannot be instantiated directly')

    def calc_normal(self, t: float) -> Coordinates:
        denorm_t = self._scale_argument(t)
        return self.calc(denorm_t)

    def calc(self, t: float) -> Coordinates:
        return NotImplementedError
        
    def _scale_argument(self, t):
        return (self.min_t + t * (self.max_t - self.min_t))
