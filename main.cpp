#include <iostream>
using namespace std;

class Grundwert {
    private:
    short int prozentsatzprivat;
    short int prozentwertprivat;
    public:
    Grundwert(int prozentsatz, int prozentwert);
}
Grundwert::Grundwert(short int prozentsatz, short int prozentwert)
    : prozentsatprivat(prozentsatz), prozentwertprivat(prozentwert) {
    short int gw; 
    std::cout << "Geben Sie Prozentsatz an." << endl;
    std::cin >> prozentsatz;
    std::cout << "Geben Sie Prozentwert an." << endl;
    std::cin >> prozentwert;
    
}
