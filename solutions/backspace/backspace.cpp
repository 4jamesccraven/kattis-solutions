#include<iostream>
#include<string>

int main(int argc, char* argv[]) {
    std::string input {};

    std::getline(std::cin, input);

    auto index = input.find('<');
    while (index != std::string::npos) {
        input.erase(index - 1, 1);
        input.erase(index - 1, 1);
        index = input.find('<');
    }

    std::cout << input << std::endl;

    return 0;
}
