using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace WolframFourierArtCode.FourierFuncs;

/// <summary>
/// Point coordinates
/// </summary>
public class Coordinates(double x, double y)
{
    public double X { get; set; } = x;
    public double Y { get; set; } = y;
}

public interface IFourierFunc: IFourierSeries
{
    /// <summary>
    /// Get all series
    /// </summary>
    IFourierSeries[] GetSeries();
}

public interface IFourierSeries
{
    /// <summary>
    /// Min argument value
    /// </summary>
    double MinT { get; }

    /// <summary>
    /// Max argument value
    /// </summary>
    double MaxT { get; }

    /// <summary>
    /// Calculate coordinates by normalized agrument <paramref name="t"/>.
    /// Argument must belong to [0.0, 1.0] range.
    /// </summary>
    Coordinates CalcNormal(double t);

    /// <summary>
    /// Calculate coordinates by agrument <paramref name="t"/>.
    /// Argument must belong to [<see cref="MinT"/>, <see cref="MaxT"/>] range.
    /// </summary>
    Coordinates Calc(double t);
}

public abstract class FourierFuncBase : IFourierFunc
{
    protected IFourierSeries[] _series = null!;

    protected FourierFuncBase()
    {
        InitSeries();
    }

    public double MinT => _series[^1].MinT;

    public double MaxT => _series[ 0].MaxT;

    public IFourierSeries[] GetSeries() => _series;

    public Coordinates CalcNormal(double t)
    {
        var denormT = MapRange(t, 0d, 1d, MinT, MaxT);

        return Calc(denormT);
    }

    public Coordinates Calc(double t)
    {
        var series = _series
            .Where(s => s.MinT <= t && t <= s.MaxT)
            .FirstOrDefault();

        return series?.Calc(t);
    }

    protected abstract void InitSeries();

    private static double MapRange(
        double value,
        double sourceMin, double sourceMax,
        double targetMin, double targetMax
        )
    {
        var scale = (targetMax - targetMin) / (sourceMax - sourceMin);
        return targetMin + (value - sourceMin) * scale;
    }
}


public abstract class FourierSeriesBase: IFourierSeries
{
    protected double sin(double a) => Math.Sin(a);

    protected const double π = Math.PI;

    public abstract double MinT { get; }

    public abstract double MaxT { get; }

    public Coordinates CalcNormal(double t)
    {
        var scaledT = ScaleArgument(t);
        return Calc(scaledT);
    }

    public abstract Coordinates Calc(double t);

    protected double ScaleArgument(double t) => (MinT + t * (MaxT - MinT));
}
