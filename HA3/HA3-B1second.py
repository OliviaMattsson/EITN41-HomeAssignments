from random import randint
import matplotlib.pyplot as plot
import hashlib

X_value = 40


def generate_k_values():
    values_of_k = []
    for i in range(0, 2 ** 16 - 1):
        values_of_k.append(i)
    return values_of_k


def create_k():
    return randint(0, 2 ** 16 - 1)


def create_v():
    return randint(0, 1)


def commit_values(X):
    v = create_v()
    return v, create_commit(v, create_k(), X)


def create_commit(v, k, X):
    m = str(bin(v)[2:] + bin(k)[2:])
    hash_object = hashlib.sha1(m.encode())
    hash_value = hash_object.hexdigest()
    return bin(int(hash_value, 16))[2: X + 2]


def calc_binding(X):
    v, initial_commit = commit_values(X)
    changed_v = 1
    if v == 1:
        changed_v = 0
    value = 0
    for k in generate_k_values():
        commit = create_commit(changed_v, k, X)
        if commit == initial_commit:
            return value + 1
    return value


def calc_concealing(X):
    v, initial_commit = commit_values(X)
    commits0 = []
    commits1 = []
    for k in generate_k_values():
        c0 = create_commit(0, k, X)
        c1 = create_commit(1, k, X)
        if c0 == initial_commit:
            commits0.append(c0)
        if c1 == initial_commit:
            commits1.append(c1)

    if v == 1:
        return len(commits1) / (len(commits0) + len(commits1))

    return len(commits0) / (len(commits0) + len(commits1))


def calc_probabilities():
    calculated_binding_prob = []
    calculated_concealing_prob = []
    x_values = []
    iterations = 100

    for output_length in range(1, X_value):
        binding_values = []
        concealing_values = []
        for k in range(iterations):
            binding_values.append(calc_binding(output_length))
            concealing_values.append(calc_concealing(output_length))

        calculated_binding_prob.append(
            sum(binding_values) / len(binding_values))
        calculated_concealing_prob.append(
            sum(concealing_values) / len(binding_values))
        x_values.append(output_length)
        print("Simulating with hash output length: " + str(output_length))
    return calculated_binding_prob, calculated_concealing_prob, x_values


def stats():
    calculated_binding_prob, calculated_concealing_prob, x_values = calc_probabilities()
    plot.ylabel("Probability of breaking the property")
    plot.xlabel("Length of output")

    plot.plot(x_values, calculated_binding_prob, label="Binding")
    plot.plot(x_values, calculated_concealing_prob, label="Concealing")
    plot.legend(loc='best')
    plot.show()


stats()