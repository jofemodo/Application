# -*- coding: utf-8 -*-


class Banks(object):
    index = 0
    banks = {}

    def __init__(self):
        self.banks = {}

    @property
    def json(self):
        banks = []
        for bank in self.all:
            banks.append(bank.json)

        return banks

    @property
    def all(self):
        return sorted(list(self.banks.values()), key=lambda bank: bank.index)

    def __len__(self):
        return len(self.banks)

    def __getitem__(self, index):
        try:
            return self.banks[index]
        except KeyError:
            raise IndexError("Bank not found")

    def __delitem__(self, index):
        try:
            del self.banks[index]
        except KeyError:
            raise IndexError("Bank not found")

    def append(self, bank):
        if bank.index == -1:
            bank.index = self.index
            self.index = bank.index + 1

        elif bank.index >= self.index:
            self.index = bank.index + 1

        self.banks[bank.index] = bank

    def swap(self, bankA, bankB):
        bankA.index, bankB.index = bankB.index, bankA.index

        self.banks[bankA.index] = bankA
        self.banks[bankB.index] = bankB