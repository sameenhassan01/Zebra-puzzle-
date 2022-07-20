#include <iostream>
#include <complex>



enum { Color, Beverage, Pet, Cigarets, Nationality };
enum { Englishman, Spaniard, Ukrainian, Norwegian, Japanese };
enum { OldGold, Kools, Chesterfields, LuckyStrike, Parliaments };
enum { Red, Green, Ivory, Yellow, Blue };
enum { Dog, Snails, Fox, Horse, Zebra };
enum { Coffee, Tea, Milk, OrangeJuice, Water };
enum { _ = -1 };




const auto PropertiesCount = 5;

// There are five houses.
const auto HousesCount = 5;


int s[HousesCount][PropertiesCount];

bool move_next(int house, int property, int value)
{
	return (house > 0 && (s[house - 1][property] == _ || s[house - 1][property] == value)) ||
		(house < HousesCount - 1 && (s[house + 1][property] == _ || s[house + 1][property] == value));
}

bool check()
{
	
	// the five houses is painted a different color
	//  with different pets, drinks, beverages and smoke different brands of American cigrates 
	
	for (auto i = 0; i < HousesCount; ++i)
	{
		for (auto j = 0; j < PropertiesCount; ++j)
		{
			for (auto k = i + 1; k < HousesCount; ++k)
				if (s[i][j] != _ && s[k][j] != _ && s[i][j] == s[k][j])
					return false;
		}
	}

	// The Englishman lives in the red house.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Nationality] == Englishman && s[i][Color] != Red && s[i][Color] != _)
			return false;
	// The Spaniard owns the dog.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Nationality] == Spaniard && s[i][Pet] != Dog && s[i][Pet] != _)
			return false;

	// Coffee is drunk in the green house.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Color] == Green && s[i][Beverage] != Coffee && s[i][Beverage] != _)
			return false;
	// The Ukrainian drinks tea.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Nationality] == Ukrainian && s[i][Beverage] != Tea && s[i][Beverage] != _)
			return false;
	// The green house is immediately to the right of the ivory house.
	for (auto i = 0; i < HousesCount; ++i)
		if ((i == 0 && s[i][Color] == Green) || (s[i][Color] == Green && s[i - 1][Color] != Ivory && s[i - 1][Color] != _))
			return false;
	// The Old Gold smoker owns snails.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Cigarets] == OldGold && s[i][Pet] != Snails && s[i][Pet] != _)
			return false;
	// Kools are smoked in the yellow house.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Cigarets] == Kools && s[i][Color] != Yellow && s[i][Color] != _)
			return false;
	// Milk is drunk in the middle house.
	if (s[2][Beverage] != Milk && s[2][Beverage] != _)
		return false;
	// The Norwegian lives in the first house.
	if (s[0][Nationality] != Norwegian && s[0][Nationality] != _)
		return false;
	// The man who smokes Chesterfields lives in the house next to the man with the fox.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Cigarets] == Chesterfields && !move_next(i, Pet, Fox))
			return false;

	// Kools are smoked in the house next to the house where the horse is kept.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Cigarets] == Kools && !move_next(i, Pet, Horse))
			return false;
	// The Lucky Strike smoker drinks orange juice.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Cigarets] == LuckyStrike && s[i][Beverage] != OrangeJuice && s[i][Beverage] != _)
			return false;
	// The Japanese smokes Parliaments.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Nationality] == Japanese && s[i][Cigarets] != Parliaments && s[i][Cigarets] != _)
			return false;
	// The Norwegian lives next to the blue house.
	for (auto i = 0; i < HousesCount; ++i)
		if (s[i][Nationality] == Norwegian && !move_next(i, Color, Blue))
			return false;

	return true;
}

bool result(int house, int property)
{
	auto oldValue = s[house][property];
	for (auto i = 0; i < 5; ++i)
	{
		s[house][property] = i;
		if (check())
		{
			auto newHouse = (house + 1) % HousesCount;
			auto newProperty = property + (newHouse == 0 ? 1 : 0);
			if (newProperty >= PropertiesCount || result(newHouse, newProperty))
				return true;
		}
	}
	s[house][property] = oldValue;
	return false;
}

#define STR(x) case x: return #x

std::string Colors(int value)
{
	switch (value)
	{
		STR(Red);
		STR(Green);
		STR(Ivory);
		STR(Yellow);
		STR(Blue);
	}
	return "?";
}

std::string beverages(int value)
{
	switch (value)
	{
		STR(Coffee);
		STR(Tea);
		STR(Milk);
		STR(OrangeJuice);
		STR(Water);
	}
	return "?";
}

std::string Pets(int value)
{
	switch (value)
	{
		STR(Dog);
		STR(Snails);
		STR(Fox);
		STR(Horse);
		STR(Zebra);
	}
	return "?";
}

std::string cigarets(int value)
{
	switch (value)
	{
		STR(OldGold);
		STR(Kools);
		STR(Chesterfields);
		STR(LuckyStrike);
		STR(Parliaments);
	}
	return "?";
}

std::string Nationalities(int value)
{
	switch (value)
	{
		STR(Englishman);
		STR(Spaniard);
		STR(Ukrainian);
		STR(Norwegian);
		STR(Japanese);
	}
	return "?";
}

// Now, who drinks water? Who owns the zebra?
int main()
{
	std::cout << " Who Owns The Zebra ? \n \n " ;
	for (auto p = 0; p < PropertiesCount; ++p)
		for (auto h = 0; h < HousesCount; ++h)
			s[h][p] = _;
	if (result(0, 0))
	{
		for (auto h = 0; h < HousesCount; ++h)
			std::cout << h + 1 << " " <<
			Colors(s[h][Color]) << " " <<
			beverages(s[h][Beverage]) << " " <<
			Pets(s[h][Pet]) << " " <<
			cigarets(s[h][Cigarets]) << " " <<
			Nationalities(s[h][Nationality]) << "\n";
	}
	else
		std::cout << "sorry try again \n";
}
