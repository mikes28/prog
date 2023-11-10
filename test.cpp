#include <iostream>
#include <string>
#include <locale>

int main() {
    std::locale::global(std::locale("en_US.UTF-8"));
    std::wcout.imbue(std::locale());

    std::string str = "नमस्ते";

    std::cout << str.substr(4,5) << "\n";
    std::cout << str.substr(3,4) << "\n";
}
