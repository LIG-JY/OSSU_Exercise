import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n  # 7을 입력했습니다.
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3  # 7을 3으로 나눈 몫은 2이다.
    
        for i in range(numVowels):  # 반복을 2번합니다.
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]  # 모음 중에서 random으로 하나 뽑는다.
            self.hand[x] = self.hand.get(x, 0) + 1  # 예를들어 a를 뽑았다고 하면 key:a , a의 value값에 1을 추가합니다.
            # key가 dict에 존재하면 value값을 불러와서 1을 더하고, 없으면 default로 vlaue를 0으로 설정하고 1을 더합니다.
        
        for i in range(numVowels, self.HAND_SIZE):  # 2~6 즉 5번 반복합니다. 이게 모음은 전체가 적으니 적게 뽑고, 자음은 많이 뽑겠다는 의도로 예상합니다.
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            # 자음을 key로해서 위 처럼 뽑은 자음들과 각각의 개수를 세는 코드
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.
        >> 즉 random으로 자음과 모음을 뽑는 것이 아니라, 임의로 설정해서 dummy test

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}  #setDummyHand 메소드를 실행하면, self.hand 변수에 새로 빈 dictionary를 할당합니다.
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand. 사실 그냥 처음에 입력 받은 int값을 return합니다.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())  # key즉 모음과 자음을 sort합니다.
        for letter in hand_keys: # 각각의 글자마다
            for j in range(self.hand[letter]):  # 각각의 value만큼 for문을 돌면서 output에 글자를 더 해줍니다.
                output += letter  # 즉 결과적으로 동일한 문자끼리는 이웃해서 output에 할당됩니다.
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.

        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Make a copy of the hand, and try to update it
        new_hand = self.hand.copy()
        for letter in word:  # za
            try:
                new_hand[letter] -= 1  # 주어진 word가 hand에 모두 개수도(이상)으로 있어야 합니다.
            except KeyError:
                # if 'letter' isn't in the hand, we can't make the word from this hand.
                return False
        for letter in new_hand.keys():
            # If any of the letter counts of the new hand are less than zero after the
            # update, then we can't make the word from this hand. 업데이트 실행하지 않는다.
            if new_hand[letter] < 0:
                return False
        # If we've gotten to here, we must be able to make the word from this hand.
        # Set self.hand to the new, updated hand and return True.
        self.hand = new_hand
        return True

    
myHand = Hand(7)
print(myHand)
print(myHand.calculateLen())

myHand.setDummyHand('aazzmsp')
print(myHand)
print(myHand.calculateLen())

myHand.update('zazza')
print(myHand)
print(myHand.calculateLen())

