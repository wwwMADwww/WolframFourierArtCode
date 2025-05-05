namespace WolframFourierArtCode;

public static class Program
{

    public static async Task Main(string[] args)
    {
        Console.WriteLine("Start");

        var cmdParams = CommandLineParser.Parse(args);

        if (cmdParams == null) { return; }

        var inputFilename = Path.GetFullPath(cmdParams.InputFilename);

        await new FourierFuncCodeGenerator().Generate(
            formulaFilename: inputFilename,
            formulaFuncClassName: cmdParams.ClassName,
            language: cmdParams.Lang
            );
    }

}