#include <iostream>
using namespace std;

class Grundwert {
    private:
    short int prozentsatzprivat;
    short int prozentwertprivat;
    public:
    void Grundwertrechnen(short int prozentsatz, short int prozentwert);
    int Grundwertausgabe();
    int gw;
};
void Grundwert::Grundwertrechnen(short int prozentsatz, short int prozentwert) {
    prozentsatzprivat = prozentsatz;
    prozentwertprivat = prozentwert;
    gw = prozentwert / prozentsatz * 100;
}

int Grundwert::Grundwertausgabe() {
    return gw;
}




int main() {
    short int prozentsatz;
    short int prozentwert;
    std::cout << "Geben Sie Prozentsatz an." << endl;
    std::cin >> prozentsatz;
    std::cout << "Geben Sie Prozentwert an." << endl;
    std::cin >> prozentwert;  
    Grundwert gwr;
    gwr.Grundwertrechnen(prozentsatz, prozentwert);
    std::cout << gwr.Grundwertausgabe() << endl;
}
