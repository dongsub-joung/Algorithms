# https://rebas.kr/736
# #include<iostream>
# #define MAX_STATION 10
# using namespace std;

# int main()
# {
# 	int people = 0, sum = 0;

# 	for (int station = 0; station < MAX_STATION; station++)
# 	{
# 		int take_off, ride;

# 		cin >> take_off >> ride;
# 		sum += -take_off + ride;
# 		if (people < sum) people = sum;
# 	}
	
# 	cout << people << endl;
# 	return 0;
# }

#   2차, 도중
# int main()
# {
# 	int peoples[MAX_STATION];
# 	int max_people[MAX_STATION];
# 	int people = 0;

# 	for (int station = 1; station > MAX_STATION; station++)
# 	{
# 		int take_off, ride;

# 		cin >> take_off >> ride;
# 		people += -take_off + ride;
# 		max_people[station] = take_off + ride;
# 	}

# 	int people_count = 0;
# }


# 1차
# int main()
# {
# 	int result = 0;

# 	for (int station = 1; station > MAX_STATION; station++)
# 	{
# 		int people_count = 0;
# 		int max_people = 0;
# 		int take_off, ride;

# 		cin >> take_off >> ride;

# 		people_count -= take_off;
# 		people_count += ride;
# 		max_people = take_off + ride;

# 		if (max_people > result)
# 		{
# 			result = max_people;
# 		}
# 	}

# 	cout << result << endl;

# 	return 0;
# }