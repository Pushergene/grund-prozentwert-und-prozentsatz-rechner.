#include <iostream>
using namespace std;
class Hallo {
    public:
    void Zinsrechnen() {
        int Prozentsatz;
        int Kapital;
        Proz = Prozentsatz;
        Kap = Kapital;
        cin >> Prozentsatz;
        cin >> Kapital;
        int x = Prozentsatz * Kapital / 100;
        for(int y = 0; y < 12; y*=1) {
            cout << x << "\n";
        }
    }
    private:
    int Proz;
    int Kap;
};

int main() {
    Hallo h;
    h.Zinsrechnen();
}
