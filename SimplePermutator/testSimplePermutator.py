from simplePermutator import SimplePermutator
import time
print()
print()
print()
print()
print()

# - Create a bot:
input_size   = 3
hidden_size  = 2
hidden_count = 0
output_size  = 2
permutator = SimplePermutator(input_size, hidden_size, hidden_count, output_size)
print("Create a permutator:")
print(permutator)



while True:
    print()
    print()
    print()
    print()
    print()

    # - Get input
    bool_vector = [True,False,False]
    permutator.get_input(bool_vector)

    # - propagate_signal:
    permutator.propagate_signal()

    # - read_output_state:
    output_state = permutator.read_output_state()
    print("Output state:", output_state)

    # - read_output_prob:
    output_prob = permutator.read_output_prob()
    print("Output fire probability:", output_prob)

    # - returnOutputPlace:
    output_place = permutator.returnOutputPlace()
    print("Output place:", output_place)

    # - read_output_state:
    output_state = permutator.read_output_state()
    print("Output state new:", output_state)

    # - process_reward:
    if output_state[0] == True:
        reward = 1
    else:
        reward = 0
    permutator.process_reward(reward)

    # - Print:
    permutator.printCells()

    # - Wait:
    print()
    print()
    time.sleep(0.1)