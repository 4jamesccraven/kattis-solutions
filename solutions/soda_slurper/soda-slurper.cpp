#include<iostream>

int main() {
    unsigned int e, f, c;
    std::cin >> e >> f >> c;

    unsigned int count = e + f;
    const unsigned int price = c;

    unsigned int drunk = 0;

    while (count >= price) {
        unsigned int cbp = count / price;

        count = count % price;
        count += cbp;
        drunk += cbp;
    }

    std::cout << drunk << std::endl;
}
