#include <iostream>
#include <vector>
#include <random>


std::vector<bool> SequenceGenerate(const size_t& size)
{
	std::random_device seed;
	std::mt19937 engine(seed());
	std::vector<bool> sequence(size);
	for (size_t i = 0; i < size; ++i)
		sequence[i] = engine() % 2;

	return sequence;
}


int main()
{
	std::vector<bool> binary_sequence;
	binary_sequence = SequenceGenerate(128);
	std::cout<< "Ѕинарна€ последовальность из 128 случайных битов: "
	for (auto bit : binary_sequence)
		std::cout << bit;
}