using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace WolframFourierArtCode;

internal partial class FourierFuncParser
{
    const char theta = 'θ';
    const string formulaEnding = ") θ(sqrt(sgn(sin(t/2))))";

    [GeneratedRegex(@"(?<num>\d+|\))\s(?<identifier>\w+)")]
    private static partial Regex RegexMul();
    private static readonly Regex _regexMul = RegexMul();

    [GeneratedRegex(@"(?<num>\d+)")]
    private static partial Regex RegexNum();
    private static readonly Regex _regexNum = RegexNum();

    [GeneratedRegex(@"(?<thetas>θ\((?<start>\d+) π - t\) ((θ\(t - (?<end>\d+) π\))|(θ\(t \+ π\))))")]
    private static partial Regex RegexThetas();
    private static readonly Regex _regexThetas = RegexThetas();

    public async Task<ICollection<FourierSeriesData>> Parse(string formulaFile)
    {
        var formulas = await File.ReadAllLinesAsync(formulaFile);

        var xformula = formulas[0]["x(t) = ".Length..];
        var yformula = formulas[1]["y(t) = ".Length..];

        var xfuncs = SplitToRangeFuncs(xformula);
        var yfuncs = SplitToRangeFuncs(yformula);

        var seriesList = new List<FourierSeriesData>(xfuncs.Length);

        for (var i = 0; i < xfuncs.Length; i++)
        {
            var fx = xfuncs[i];
            var fy = yfuncs[i];

            var series = new FourierSeriesData()
            {
                Index = i,
                MinT = fx.minT * Math.PI, // minT and maxT values always same in x and y
                MaxT = fx.maxT * Math.PI,
                FormulaX = fx.func,
                FormulaY = fy.func,
            };

            seriesList.Add(series);
        }

        return seriesList;
    }

    private (string func, double minT, double maxT)[] SplitToRangeFuncs(string formula)
    {
        var funcs = new List<(string, double, double)>();

        if (!formula.Contains(theta))
        {
            funcs.Add((ConvertToCodeSyntax(formula), 0, 2));
        }
        else
        {
            var thetaMatches = _regexThetas.Matches(formula);

            formula = formula["(".Length..^formulaEnding.Length];

            var prevPos = 0;

            foreach (Match thetaMatch in thetaMatches)
            {
                var maxTstr = thetaMatch.Groups["start"].Value;
                var minTstr = thetaMatch.Groups["end"].Value;

                var minT = minTstr.Length > 0 ? double.Parse(minTstr) : 0;
                var maxT = double.Parse(maxTstr);

                var func = formula[prevPos..(thetaMatch.Index - 2)];
                func = ConvertToCodeSyntax(func);

                prevPos = thetaMatch.Index + thetaMatch.Length;

                funcs.Add((func, minT, maxT));
            }
        }

        return funcs.ToArray();
    }

    private string ConvertToCodeSyntax(string s)
    {
        // "2x" -> "2 * x"
        s = _regexMul.Replace(s, @"${num} * ${identifier}");

        // "2 * x"-> "2.0 * x"
        s = _regexNum.Replace(s, @"${num}.0");
        return s;
    }

}
