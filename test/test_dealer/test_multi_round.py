import random

import pyker


def test_button_move():

    random.seed(42)

    config = pyker.configs.NOLIMIT_HOLDEM_2P_ENV

    dealer = pyker.Dealer(**config)
    obs = dealer.reset(reset_button=True, reset_stacks=False)

    assert obs['button'] == 0
    assert obs['action'] == 0

    bet = 0
    while True:
        obs, done, reward, _ = dealer.step(bet)
        if all(done):
            break

    obs = dealer.reset(reset_button=False, reset_stacks=True)

    assert obs['button'] == 1
    assert obs['action'] == 1

    random.seed(42)

    config = pyker.configs.NOLIMIT_HOLDEM_6P_ENV

    dealer = pyker.Dealer(**config)
    obs = dealer.reset(reset_button=True, reset_stacks=True)

    assert obs['button'] == 0
    assert obs['action'] == 3

    bet = 0
    while True:
        obs, payout, done, _ = dealer.step(bet)
        if all(done):
            break

    obs = dealer.reset(reset_button=False, reset_stacks=True)

    assert obs['button'] == 1
    assert obs['action'] == 4


def test_inactive_players():

    random.seed(42)

    config = pyker.configs.NOLIMIT_HOLDEM_6P_ENV

    dealer = pyker.Dealer(**config)
    obs = dealer.reset(reset_button=True, reset_stacks=True)

    bet = 200
    _ = dealer.step(bet)
    bet = 200
    _ = dealer.step(bet)
    bet = -1
    while True:
        obs, payout, done, _ = dealer.step(bet)
        if all(done):
            break

    obs = dealer.reset(reset_button=False, reset_stacks=False)

    assert obs['button'] == 1
    assert obs['action'] == 5
