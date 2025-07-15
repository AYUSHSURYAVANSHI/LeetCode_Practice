from typing import List, Set

"""Class to store reusable constan values."""
class Constants:
    vowels: Set[str] = set(['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'])

"""Interface class for a rule. All rule classes must implement the is_valid method."""
class RuleInterface:
    def is_valid(word: str) -> bool:
        raise("Not implemented error")

"""Rule class implementing check on minimum length of a word."""
class MinimumLengthRule(RuleInterface):
    def is_valid(word: str) -> bool:
        return len(word) >= 3

"""Rule class implementing allowed characters in a word."""
class CharacterRule(RuleInterface):
    def is_valid(word: str) -> bool:
        for char in word:
            if char.isdigit() == False and (ord('A') <= ord(char) <= ord('z')) == False:
                return False
        return True

"""Rule class implementing minimum number of vowels in a word."""
class MinimumVowelRule(RuleInterface):
    def is_valid(word: str) -> bool:
        for char in word:
            if char in Constants.vowels:
                return True
        return False

"""Rule class implementing minimum number of consonants in a word."""
class MinimumConsonantRule(RuleInterface):
    def is_valid(word: str) -> bool:
        for char in word:
            if char.isdigit():
                continue
            elif char not in Constants.vowels:
                return True
        return False

class Solution:
    def isValid(self, word: str) -> bool:
        # Define the rules to apply onto the word
        rules: List[RuleInterface] = [MinimumLengthRule, CharacterRule, MinimumVowelRule, MinimumConsonantRule]
        
        # Evlauate each rule, one-by-one
        for rule in rules:
            # If any rule fails, return the word as invalid
            if rule.is_valid(word) == False:
                return False
        # If all rules pass, then the word must be valid
        return True