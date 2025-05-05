using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WolframFourierArtCode;

public class FourierFuncData
{
    public string FormulaName { get; set; }
    public string ClassName { get; set; }
    public ICollection<FourierSeriesData> Series { get; set; }
}

public class FourierSeriesData
{
    public int Index { get; set; }
    public double MinT { get; set; }
    public double MaxT { get; set; }
    public string FormulaX { get; set; }
    public string FormulaY { get; set; }
}
