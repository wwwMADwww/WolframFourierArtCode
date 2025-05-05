#include "FourierFunc.h"

Coordinates::Coordinates(double x, double y)
{
    X = x;
    Y = y;
}

////////////////////////////////////////////////////////////////////////////////////////////
// FourierSeriesBase 

double FourierSeriesBase::getMinT() { return _minT; }

double FourierSeriesBase::getMaxT() { return _maxT; }

Coordinates* FourierSeriesBase::calcNormal(double t)
{
    auto scaledT = scaleArgument(t);
    return calc(scaledT);
}

double FourierSeriesBase::sin(double a)
{
    return std::sin(a);
}

double FourierSeriesBase::scaleArgument(double t)
{
    return _minT + t * (_maxT - _minT);
}


////////////////////////////////////////////////////////////////////////////////////////////
// FourierFuncBase 

FourierFuncBase::~FourierFuncBase()
{
    for (FourierSeriesBase* s : _series)
    {
        delete s;
    }
    _series.clear();
}

void FourierFuncBase::init() 
{
    initSeries();
    _minT = _series.back()->getMinT();
    _maxT = _series.front()->getMaxT();
}

double FourierFuncBase::getMinT() { return _minT; }

double FourierFuncBase::getMaxT() { return _maxT; }

std::vector<FourierSeriesBase*> FourierFuncBase::getSeries() { return _series; }

Coordinates* FourierFuncBase::calcNormal(double t)
{
    auto denormT = mapRange(t, 0, 1, _minT, _maxT);

    return calc(denormT);
}

Coordinates* FourierFuncBase::calc(double t)
{
    auto seriesIndex = findSeriesIndex(t);

    if (seriesIndex < 0)
    {
        return NULL;
    }

    auto series = _series[seriesIndex];

    return series->calc(t);
}

double FourierFuncBase::mapRange(
    double value,
    double sourceMin, double sourceMax,
    double targetMin, double targetMax)
{
    auto scale = (targetMax - targetMin) / (sourceMax - sourceMin);
    return targetMin + (value - sourceMin) * scale;
}

int FourierFuncBase::findSeriesIndex(double t)
{
    auto result{ std::find_if(
        _series.begin(),
        _series.end(),
        [t](FourierSeriesBase* c) { return c->getMinT() <= t && t <= c->getMaxT(); }) };

    if (result == _series.end())
        return -1;
    
    return result - _series.begin();
}
