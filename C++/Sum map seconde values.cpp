#include <vector>
#include <map>
#include <string>
#include <iostream>

using namespace std;

void main()
{
	string n = "nanan";
	map<string, double> m_fileID;
	m_fileID.insert(make_pair(n, 40));
	m_fileID.insert(make_pair("kljasjkl", 10));

	map<string, double>::iterator iter;
	double sum{ 0 };

	for (iter = m_fileID.begin(); iter != m_fileID.end(); iter++)
	{
		auto key = iter->second;
		sum += key;
	}
	cout << sum << endl;
}