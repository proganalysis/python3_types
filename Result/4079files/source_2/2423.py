import random

from .MarkovChain import MarkovChain, _wordIter, _db_factory


class DynamicMarkovChain(MarkovChain):
    def generateDatabase(self, textSample, sentenceSep='[.!?\n]', n=2):
        self.textSample = _wordIter(textSample, sentenceSep)
        # get an array for the 'sentences'
        self.sentenceSep = sentenceSep
        self.n = n
        self.db = _db_factory()

    def _temporaryDatabase(self, textSample):
        """ Generate word probability database from iterable of sentences """
        # I'm using the database to temporarily store word counts
        # We're using '' as special symbol for the beginning
        # of a sentence
        self.db[('',)][''] = 0.0
        for line in textSample:
            words = line.strip().split()  # split words in line
            if len(words) == 0:
                continue
            # first word follows a sentence end
            self.db[("",)][words[0]] += 1

            for order in range(1, self.n + 1):
                for i in range(len(words) - 1):
                    if i + order >= len(words):
                        continue
                    word = tuple(words[i:i + order])
                    self.db[word][words[i + order]] += 1

                # last word precedes a sentence end
                self.db[tuple(words[len(words) - order:len(words)])][""] += 1

        # We've now got the self.db filled with parametrized word counts
        # We still need to normalize this to represent probabilities
        for word in self.db:
            wordsum = 0
            for nextword in self.db[word]:
                wordsum += self.db[word][nextword]
            if wordsum != 0:
                for nextword in self.db[word]:
                    self.db[word][nextword] /= wordsum

    def _relevantSentences(self, seedwords):
        for sentence in self.textSample:
            for seedword in seedwords:
                if seedword in sentence:
                    yield sentence

    def _databaseFromSeed(self, seedwords):
        return self._temporaryDatabase(self._relevantSentences(seedwords))

    def generateStringWithSeed(self, seed):
        """ Generate a "sentence" with the database and a given word """
        # using str.split here means we're contructing the list in memory
        # but as the generated sentence only depends on the last word of the seed
        # I'm assuming seeds tend to be rather short.
        words = seed.split()
        return self._accumulateWithSeed(words)

    def _accumulateWithSeed(self, seed):
        self._databaseFromSeed(seed)
        return MarkovChain._accumulateWithSeed(self, seed)

    def _nextWord(self, lastwords):
        lastwords = tuple(lastwords)
        if lastwords != ('',):
            while lastwords not in self.db:
                lastwords = lastwords[1:]
                if not lastwords:
                    return ''
        probmap = self.db[lastwords]
        sample = random.random()
        # since rounding errors might make us miss out on some words
        maxprob = 0.0
        maxprobword = ""
        for candidate in probmap:
            # remember which word had the highest probability
            # this is the word we'll default to if we can't find anythin else
            if probmap[candidate] > maxprob:
                maxprob = probmap[candidate]
                maxprobword = candidate
            if sample > probmap[candidate]:
                sample -= probmap[candidate]
            else:
                return candidate
        # getting here means we haven't found a matching word. :(
        return maxprobword

    def flushDatabase(self):
        """ Deletes the current state of the database to free up memory """
        self.db = _db_factory()
