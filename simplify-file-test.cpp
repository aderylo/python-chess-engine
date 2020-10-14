#include <bits/stdc++.h>
#define for(i , n) for(int i=0;i!=n;i++)
#define mp make_pair
#define pb push_back
#define e1 first
#define e2 second
using namespace std;
typedef pair<int , int> PII;
typedef long long int ll;

///variables
short int elo_min; //minimal elo we are interested in

///struct of a game
struct game
{
    short int w_elo;
    short int b_elo;
    string time;
    string moves;
    string result;
};

///arrays
vector<game>games; //all the games stored in a vector
map<string, bool> visited; //was this game already in the dataset

///convert string to short int
short int to_int(string s)
{
    short int licznik = 0;
    short int mn = 1;

    for (i , s.length()) {licznik += (s[s.length()-1-i] - '0') * mn; mn*=10;}

    return licznik;
}

///convert int to string
string to_strings(ll a)
{
    string s = "";
    while (a > 0)
    {
        s += (char)(a%10 + '0');
        a/=10;
    }

    string s2 = "";
    for (i , s.length()) {s2 += s[s.length()-1-i];}

    return s2;
}

///reading the file
bool read(string dir)
{
    ifstream plik;
    plik.open(dir);
    if (!plik.good()) {return 0;}

    short int licz = 0;
    game a;

    int c = 0;
    while (!plik.eof())
    {
        string s;
        getline(plik, s);

        string h = s.substr(0, 7);

        if (s.length() == 0) {licz++; if (licz == 1) {continue;} else {games.pb(a); a = {}; licz = 0; continue;} }
        if (h == "[WhiteE") {a.w_elo = to_int(s.substr(11, 4)); continue;}
        if (h == "[BlackE") {a.b_elo = to_int(s.substr(11, 4)); continue;}
        if (h == "[TimeCo") {a.time = s.substr(14, s.length()-16); continue;}
        if (h == "[Result") {a.result = s.substr(9, 3); continue;}
        if (licz == 1)
        {
            string b = s;
            while(s.length() != 0 & !plik.eof())
            {
                getline(plik, s);

                b = b + " " + s;

            }
                a.moves = b;
                games.pb(a); a = {}; licz = 0; continue;
        }
    }

    return 1;
}

///is this game ok(ELO, time requirements) and didnt it occur before?
bool ok(game a)
{
    if (!visited[a.moves])
    {visited[a.moves] = 1;}
    else
    {return 0;}

    if ((a.w_elo >= elo_min || a.b_elo >= elo_min) & a.result != "1/2")
    {return 1;}
    return 0;
}

///moving information from the vector to separate files
void dataset()
{
    //int x = 1;
    for (i , games.size())
    {
        if (ok(games[i]))
        {
            ofstream xd; // + to_strings(x)
            xd.open("dataset/file", std::ofstream::app );
            xd<<games[i].moves<<endl; //games[i].time
            xd.close();
            //x++;
        }
    }
    games.clear();
}

///copy all the files into the vector
void copy_all()
{
    ll x = 1;

    while (read("unzipped/file" + to_strings(x))) {cout<<x<<endl; dataset();  x++;}
}



int main()
{
    elo_min = 2200;

    copy_all();



return 0;
}
