#include <iostream>
#include <string>
#include <locale>

int main() {
    std::locale::global(std::locale("en_US.UTF-8"));
    std::wcout.imbue(std::locale());

    std::wstring str = L"नमस्ते";

    //get the forst 2 elemets of "नमस्ते"
    std::wstring str2 = str.substr(0, 2);
    // now print it

    std::wcout << str2 << std::endl;

}
