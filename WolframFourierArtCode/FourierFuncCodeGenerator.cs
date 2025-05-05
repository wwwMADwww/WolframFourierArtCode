using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WolframFourierArtCode;

public enum CodeLanguageEnum
{ 
    Text,
    CSharp,
    Cpp,
    Python
}

internal class FourierFuncCodeGenerator
{
    public async Task Generate(
        string formulaFilename,
        string formulaFuncClassName,
        CodeLanguageEnum language)
    {
        var parser = new FourierFuncParser();

        var seriesData = await parser.Parse(formulaFilename);

        var funcData = new FourierFuncData()
        {
            FormulaName = Path.GetFileNameWithoutExtension(formulaFilename),
            ClassName = formulaFuncClassName,
            Series = seriesData
        };

        var session = new Dictionary<string, object>() { { "funcData", funcData } };

        switch (language)
        {
            case CodeLanguageEnum.Text:
                await GenerateText(formulaFuncClassName, session);
                break;

            case CodeLanguageEnum.CSharp:
                await GenerateCsharp(formulaFuncClassName, session);
                break;

            case CodeLanguageEnum.Cpp:
                await GenerateCpp(formulaFuncClassName, session);
                break;

            case CodeLanguageEnum.Python:
                await GeneratePyton(formulaFuncClassName, session);
                break;

            default: throw new NotSupportedException($"Unknown language {language}");
        }

    }

    private static async Task GenerateText(string formulaFilenameOut, Dictionary<string, object> session)
    {
        var codeGenTxt = new FourierFuncImpl_text();
        codeGenTxt.Session = session;
        codeGenTxt.Initialize();
        var text = codeGenTxt.TransformText();
        await File.WriteAllTextAsync(formulaFilenameOut + ".txt", text);
    }

    private static async Task GenerateCsharp(string formulaFilenameOut, Dictionary<string, object> session)
    {
        var codeGenCs = new FourierFuncImpl_cs();
        codeGenCs.Session = session;
        codeGenCs.Initialize();
        var csCode = codeGenCs.TransformText();
        await File.WriteAllTextAsync(formulaFilenameOut + ".cs", csCode);
    }

    private static async Task GenerateCpp(string formulaFilenameOut, Dictionary<string, object> session)
    {
        var codeGenH = new FourierFuncImpl_cpp_h();
        codeGenH.Session = session;
        codeGenH.Initialize();
        var hCode = codeGenH.TransformText();
        await File.WriteAllTextAsync(formulaFilenameOut + ".h", hCode);

        var codeGenCpp = new FourierFuncImpl_cpp_cpp();
        codeGenCpp.Session = session;
        codeGenCpp.Initialize();
        var cppCode = codeGenCpp.TransformText();
        await File.WriteAllTextAsync(formulaFilenameOut + ".cpp", cppCode);
    }

    private static async Task GeneratePyton(string formulaFilenameOut, Dictionary<string, object> session)
    {
        var codeGenPython = new FourierFuncImpl_python();
        codeGenPython.Session = session;
        codeGenPython.Initialize();
        var pythonCode = codeGenPython.TransformText();
        await File.WriteAllTextAsync(formulaFilenameOut + ".py", pythonCode);
    }

}
