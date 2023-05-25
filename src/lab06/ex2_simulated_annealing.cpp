#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <algorithm>
#include <ctime>

#define IT_MAX 10000

struct Point
{
    double x;
    double y;
};

double distance(Point a, Point b)
{
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double circuit_length(std::vector<Point> points)
{
    double length = 0.0;
    for (int i = 0; i < points.size() - 1; ++i)
        length += distance(points[i], points[i + 1]);

    length += distance(points[points.size() - 1], points[0]);
    return length;
}

std::vector<Point> simulated_annealing(std::vector<Point> points)
{
    int n = points.size();
    // p = dowolny cykl startowy
    std::vector<Point> P;
    for (int i = 0; i < n; i++)
    {
        P.push_back(points[i]);
    }

    std::random_shuffle(P.begin(), P.end());

    // petla chlodzenia
    int T{10};
    for (int i = 100; i >= 1; --i)
    {
        T = 0.001 * i * i;
        for (int it = 0; it < IT_MAX; ++it)
        {
            // losowanie (a, b) oraz (c, d) należące do cyklu
            int a{0}, b{0}, c{0}, d{0};
            while (true)
            {
                a = rand() % n;
                b = (a + 1) % n;
                c = rand() % n;
                d = (c + 1) % n;
                if (a != c && a != d && b != c && b != d)
                    break;
            }

            std::vector<Point> P_new(P);
            int i{0}, j{0};
            if (a < b) { i = b; j = c; }
            else { i = c; j = b; }

            while (i < j)
            {
                auto tmp = P_new[i];
                P_new[i] = P_new[j];
                P_new[j] = tmp;
                i++; j--;
            }

            double P_cost = circuit_length(P);
            double P_new_cost = circuit_length(P_new);

            if (P_new_cost < P_cost)
                P = P_new;
            else
            {
                double r = (double)rand() / RAND_MAX;
                if (r < exp(-(P_new_cost - P_cost) / (T)))
                    P = P_new;
                else
                    std::swap(P_new[b], P_new[c]);
            }
        }
    }

    return P;
}

int main()
{
    srand(time(NULL));
    std::vector<Point> points;

    std::ifstream file("input_150.dat");
    if (!file)
    {
        std::cerr << "Nie udalo sie otworzyc pliku" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(file, line))
    {
        Point point;
        sscanf(line.c_str(), "%lf %lf", &point.x, &point.y);
        points.push_back(point);
    }
    file.close();

    // for (auto& a : points)
    //     std::cout << a.x << " " << a.y << std::endl;

    std::vector<Point> P = simulated_annealing(points), tmp_P;
    double min_distance = circuit_length(P);
    // std::cout << "\nIter 1: " << circuit_length(P);

    for (int i = 0; i < 5; ++i)
    {
        tmp_P = simulated_annealing(P);
        double tmp_distance = circuit_length(tmp_P);
        if (tmp_distance < min_distance)
        {
            P = tmp_P;
            min_distance = tmp_distance;
        }
        std::cout << "\nDistance [iter=" << i + 1 << "] " << min_distance;
    }

    std::ofstream outfile("out.dat");
    for (const auto &p : P)
        outfile << p.x << " " << p.y << '\n';
    outfile << P[0].x << " " << P[0].y << '\n';
    outfile.close();

    return 0;
}