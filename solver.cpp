#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>
#include <chrono>
using namespace std;
using namespace std::chrono;

void writeCSV(vector<vector<float> > V) {
	cout << fixed << setprecision(6);
	for (vector<float> row_el : V) {
		int i = 0, L = row_el.size();
		for (float el : row_el) {
			cout << el;
			if (i < (L-1)) cout << ",";
			i++;
		}
		cout << "\n";
	}
}

vector<vector<float> > poissonEquation(int L = 10, float V0 = 1, float epsilon = 1e-5) {
	vector<float> T0(2*L, 0);
	vector<vector<float> > V(2*L, T0);
	for (int i = 0; i < L; i++) {
		V[i][L] = i * V0 / L;
		V[L][i+L] = (L-i) * V0 / L;
	}
	vector<vector<float> > VPrev(V), VDiff(V);

	while (true) {
		float maxVal = 0;
		for (int i = 1; i < (2*L - 1); i++) {
			for (int j = 1; j < (2*L - 1); j++) {
				if ((i < L && j < L) || (i > L && j > L)) {
					V[i][j] = 0.25 * (VPrev[i+1][j] + VPrev[i-1][j] + VPrev[i][j+1] + VPrev[i][j-1]);
					if (abs(V[i][j] - VPrev[i][j]) > maxVal) maxVal = abs(V[i][j] - VPrev[i][j]);
				}
			}
		}
		if (maxVal < epsilon) break;
		VPrev = V;
	}

	return V;
}

int main(int argc, char *argv[]) {
	int L = 10;
	if (argc > 1) L = stoi(argv[1]);
	auto start = high_resolution_clock::now();
	vector<vector<float> > V = poissonEquation(L);
	auto stop = high_resolution_clock::now();
	double t = (duration_cast<nanoseconds>(stop - start)).count() / 10e6;
	writeCSV(V);
	cout << fixed << setprecision(6) << ";" << t;

	return 0;
}