using CommandLine;

namespace WolframFourierArtCode;

public class CommandLineParams
{
    [Option('i', "input", HelpText = "Formula file", Required = true)]
    public string InputFilename { get; set; }

    [Option('l', "lang", HelpText = "Output code language, case sensitive. Supported languages: " 
        + nameof(CodeLanguageEnum.Text) + ", " 
        + nameof(CodeLanguageEnum.CSharp) + ", " 
        + nameof(CodeLanguageEnum.Cpp) + ", " 
        + nameof(CodeLanguageEnum.Python)
        , Required = true)]
    public string LangString { get; set; }

    public CodeLanguageEnum Lang { get; set; }

    [Option('c', "classname", HelpText = "Generated class name", Default = null)]
    public string ClassName { get; set; }
}

internal class CommandLineParser
{
    public static CommandLineParams Parse(string[] args)
    {
        var parseResult = Parser.Default.ParseArguments<CommandLineParams>(args);

        if (parseResult.Errors.Any()) { return null; }

        if (parseResult.Value.ClassName == null)
        {
            parseResult.Value.ClassName = Path.GetFileNameWithoutExtension(parseResult.Value.InputFilename) + "FourierFunc";
        }

        if (!Enum.TryParse<CodeLanguageEnum>(parseResult.Value.LangString, out var lang))
        {
            Console.Error.WriteLine($"Invalid language {parseResult.Value.LangString}");
            return null;
        }

        parseResult.Value.Lang = lang;

        return parseResult.Value;
    }
}
