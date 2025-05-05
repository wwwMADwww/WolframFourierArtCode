namespace TestAppCsharp;

internal class Program
{
    static async Task Main(string[] args)
    {
        using var sw = new StreamWriter("coords.txt", new FileStreamOptions()
        {
            Access = FileAccess.Write,
            BufferSize = 4096 * 1024,
            Mode = FileMode.OpenOrCreate,
            Options = FileOptions.Asynchronous,
            Share = FileShare.Read
        });
        sw.BaseStream.SetLength(0);

        var func = new SkullFourierFunc();

        for (int i = 0; i <= 10000; i++)
        {
            double t = i / 10000.0;

            var c = func.CalcNormal(t);

            if (c == null) continue;

            await sw.WriteLineAsync($"{c.X}\t{c.Y}");
        }

    }
}
