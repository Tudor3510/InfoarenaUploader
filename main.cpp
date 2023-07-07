#include <fstream>
using namespace std;

int main (int argc, char** argv){
    ifstream fin ("adunare.in");
    int a, b;
    fin >>  a   >>  b;
    fin.close();

    ofstream fout ("adunare.out");
    fout    <<  a + b   <<  "\n";
    fout.close();

    return 0;
}