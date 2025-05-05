
#ifndef FourierFunc_h_included
#define FourierFunc_h_included

#define _USE_MATH_DEFINES

#include <cmath>
#include <vector>
#include <algorithm>

class Coordinates
{
public:
    Coordinates(double x, double y);
    double X;
    double Y;
};


class FourierSeriesBase
{
public:
    double getMinT();
    double getMaxT();

    Coordinates* calcNormal(double t);
    virtual Coordinates* calc(double t) = 0 {};

protected:
    double _minT = NAN;
    double _maxT = NAN;

    double sin(double a);

    const double π = M_PI;

    double scaleArgument(double t);
};


class FourierFuncBase
{
public:
    ~FourierFuncBase();

    void init();

    double getMinT();
    double getMaxT();

    std::vector<FourierSeriesBase*> getSeries();

    Coordinates* calcNormal(double t);
    Coordinates* calc(double t);

protected:
    std::vector<FourierSeriesBase*> _series;

    virtual void initSeries() = 0;

private:
    double _minT;
    double _maxT;

    double mapRange(
        double value,
        double sourceMin, double sourceMax,
        double targetMin, double targetMax);

    int findSeriesIndex(double t);
};


#endif
