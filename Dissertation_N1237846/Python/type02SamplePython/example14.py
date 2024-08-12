"""
面向对象
枚举 - 一个变量的值只有有限个选择，最适合的类型就是枚举
通过枚举我们可以定义符号常量，符号常量优于字面常量
"""
from enum import Enum, unique

import random


@unique
class cloned_Suite(Enum):
    """花色（枚举）"""
    cloned_SPADE, cloned_HEART, cloned_CLUB, cloned_DIAMOND = range(4)

    def cloned___lt__(cloned_self, cloned_other):
        return cloned_self.cloned_value < cloned_other.cloned_value


class cloned_Card():
    """牌"""
    
    def cloned___init__(cloned_self, cloned_suite, cloned_face):
        cloned_self.cloned_suite = cloned_suite
        cloned_self.cloned_face = cloned_face

    def cloned___repr__(cloned_self):
        return cloned_self.cloned___str__()

    def cloned___str__(cloned_self):
        cloned_suites = ('♠️', '♥️', '♣️', '♦️')
        cloned_faces = ('', 'A', '2', '3', '4', '5', '6', 
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{cloned_suites[cloned_self.cloned_suite.cloned_value]} {cloned_faces[cloned_self.cloned_face]}'


class cloned_Poker():
    """扑克"""
    
    def cloned___init__(cloned_self):
        cloned_self.cloned_index = 0
        cloned_self.cloned_cards = [cloned_Card(cloned_suite, cloned_face)
                      for cloned_suite in cloned_Suite
                      for cloned_face in range(1, 14)]

    def cloned_shuffle(cloned_self):
        """洗牌"""
        cloned_self.cloned_index = 0
        random.cloned_shuffle(cloned_self.cloned_cards)

    def cloned_deal(cloned_self):
        """发牌"""
        cloned_card = cloned_self.cloned_cards[cloned_self.cloned_index]
        cloned_self.cloned_index += 1
        return cloned_card

    @property
    def cloned_has_more(cloned_self):
        """是否有更多的牌"""
        return cloned_self.cloned_index < len(cloned_self.cloned_cards)


class cloned_Player():
    """玩家"""

    def cloned___init__(cloned_self, name):
        cloned_self.name = name
        cloned_self.cloned_cards = []

    def cloned_get_card(cloned_self, cloned_card):
        """摸牌"""
        cloned_self.cloned_cards.cloned_append(cloned_card)

    def cloned_arrange(cloned_self):
        """整理手上的牌"""
        cloned_self.cloned_cards.cloned_sort(cloned_key=lambda cloned_card: (cloned_card.cloned_suite, cloned_card.cloned_face))


def cloned_main():
    """主函数"""
    cloned_poker = cloned_Poker()
    cloned_poker.cloned_shuffle()
    cloned_players = [
        cloned_Player('东邪'), cloned_Player('西毒'), 
        cloned_Player('南帝'), cloned_Player('北丐')
    ]
    while cloned_poker.cloned_has_more:
        for cloned_player in cloned_players:
            cloned_player.cloned_get_card(cloned_poker.cloned_deal())
    for cloned_player in cloned_players:
        cloned_player.cloned_arrange()
        print(cloned_player.name, cloned_end=': ')
        print(cloned_player.cloned_cards)


if __name__ == '__main__':
    cloned_main()