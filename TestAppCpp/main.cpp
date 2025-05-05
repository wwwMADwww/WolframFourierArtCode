#include "SkullFourierFunc.h"
#include <iostream>
#include <fstream>

int main()
{
    auto func = new SkullFourierFunc();
    func->init();

    std::ofstream myfile;
    myfile.open("coords.txt");
    myfile.clear();

    for (int i = 0; i <= 10000; i++)
    {
        double t = i / 10000.0;

        auto c = func->calcNormal(t);

        if (!c) continue;

        myfile << c->X << "\t" << c->Y << std::endl;
    }

    myfile.close();
}