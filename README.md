# WolframFourierArtCode

Utility to convert some fourier art formulas from WolframAlpha to hardcode in your projects.

Formulas must be in a specific format. Examples of supported and unsupported formulas along with links to their WA page can be found in `Formulas` directory.

To obtain formulas from WolframAlpha go to `Equations` section of the graph, click `Plain Text`, make sure it looks similar to provided examples, copy text to file without any modifications.

Alternative project [WolframFourierArtConverter](https://github.com/wwwMADwww/WolframFourierArtConverter) allows to further decompose and calculate same formulas in runtime without hardcoding.

## Usage

```bash
-i, --input        Required. Formula file

-l, --lang         Required. Output code language, case sensitive. Supported languages: Text, CSharp, Cpp, Python

-c, --classname    Generated class name

--help             Display this help screen.

--version          Display version information.
```

### Usage examples

Generate C# code for formula in `batman.txt`:

`WolframFourierArtCode -i batman.txt --lang=CSharp`


Generate Python code for formula in `007.txt` and name generated class as `JamesBondFunc`:

`WolframFourierArtCode -i 007.txt -c JamesBondFunc --lang=Python`

## Generated files

Generated files contain concrete implementations of some base classes, so code of the latter is required. Base classes files could be found in `WolframFourierArtCode/FourierFuncs` dir or in `TestApp`s, copy them to your project.

`TestApp`s are also providing minimal example of how to use generated classes.
