import unittest
import pytest

from black_jack import (
                        value_of_card,
                        higher_card,
                        value_of_ace,
                        is_blackjack,
                        can_split_pairs,
                        can_double_down
                        )


class BlackJackTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_value_of_card(self):
        data = [
                ('2', 2), ('5', 5), ('8', 8),
                ('A', 1), ('10', 10), ('J', 10),
                ('Q', 10), ('K', 10)]

        for variant, (card, value) in enumerate(data, 1):
            with self.subTest('variation #{}'.format(variant), input=card, output=value):
                error_msg = 'Expected {} as the value of {}.'.format(value, card)

                self.assertEqual(value_of_card(card), value, msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_higher_card(self):
        data = [
                ('A', 'A', ('A', 'A')),
                ('10', 'J', ('10', 'J')),
                ('3', 'A', '3'),
                ('3', '6', '6'),
                ('Q', '10', ('Q', '10')),
                ('4', '4', ('4', '4')),
                ('9',  '10', '10'),
                ('6', '9', '9'),
                ('4', '8', '8')]

        for variant, (card_one, card_two, result) in enumerate(data, 1):
            with self.subTest('variation #{}'.format(variant), card_one=card_one, card_two=card_two, output=result):
                error_msg = 'Expected {} as the higher value of the cards {}, {}.'.format(result, card_one, card_two)

                self.assertEqual(higher_card(card_one, card_two), result, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_value_of_ace(self):
        data = [
                ('2', '3', 11), ('3', '6', 11), ('5', '2', 11),
                ('8', '2', 11), ('5', '5', 11), ('Q', 'A', 1),
                ('10', '2', 1), ('7', '8', 1), ('J', '9', 1),
                ('K', 'K', 1), ('2', 'A', 1)]

        for variant, (card_one, card_two, ace_value) in enumerate(data, 1):
            with self.subTest('variation #{}'.format(variant), card_one=card_one, card_two=card_two, ace_value=ace_value):
                error_msg = 'Expected {} as the value of an ace card when the hand has {}, {}.'.format(ace_value, card_one, card_two)

                self.assertEqual(value_of_ace(card_one, card_two), ace_value, msg=error_msg)


    @pytest.mark.task(taskno=4)
    def test_is_blackjack(self):
        data = [
                (('A', 'K'), True), (('10', 'A'), True),
                (('10', '9'), False), (('A', 'A'), False),
                (('4', '7'), False), (('9', '2'), False),
                (('Q', 'K'), False)]

        for variant, (hand, blackjack) in enumerate(data, 1):
            with self.subTest('variation #{}'.format(variant), input=hand, output=blackjack):
                error_msg='Hand {} {} a blackjack.'.format(hand, "is" if blackjack else "is not")

                self.assertEqual( is_blackjack(*hand), blackjack, msg=error_msg)


    @pytest.mark.task(taskno=5)
    def test_can_split_pairs(self):
        data = [
                (('Q', 'K'), True), (('6', '6'), True), (('A', 'A'), True),
                (('10', 'A'), False), (('10', '9'), False)]

        for variant, (hand, split_pairs) in enumerate(data, 1):
            with self.subTest('variation #{}'.format(variant), input=hand, output=split_pairs):
                error_msg='Hand {} {} be split into pairs.'.format(hand, "can" if split_pairs else "cannot")

                self.assertEqual(can_split_pairs(*hand), split_pairs, msg=error_msg)


    @pytest.mark.task(taskno=6)
    def test_can_double_down(self):
        data = [
                (('A', '9'), True), (('K', 'A'), True), (('4', '5'), True),
                (('A', 'A'), False), (('10', '2'), False), (('10', '9'), False)]

        for variant, (hand, double_down) in enumerate(data, 1):
            with self.subTest('variation #{}'.format(variant), input=hand, output=double_down):
                error_msg = 'Hand {} {} be doubled down.'.format(hand, "can" if double_down else "cannot")

                self.assertEqual(can_double_down(*hand), double_down, msg=error_msg)
