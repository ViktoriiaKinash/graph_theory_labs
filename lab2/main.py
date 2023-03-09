def is_degree_sequence(sequence):
    while len(sequence) > 0:
        if(all(v == 0 for v in sequence)):
            return True
        
        sequence = sorted(sequence, reverse=True)

        if len(sequence) <= sequence[0] or sequence[0] < 0:
            return False

        for i in range(1, sequence[0] + 1):
            sequence[i] -= 1

        sequence = sequence[1:]
    return True

def zadanie1():
    print('\nZadanie 1')
    print('ok' if not is_degree_sequence([1, 2, 3, 4, 4]) else 'not ok')
    print('ok' if is_degree_sequence([1, 2, 2, 3, 4, 4]) else 'not ok')
    print('ok' if not is_degree_sequence([1, 2, 2, 3, 3, 4]) else 'not ok')
    print('ok' if is_degree_sequence(
        [1, 2, 2, 3, 4, 4, 2, 2, 2, 3, 1, 5, 7, 4]) else 'not ok')
    print('ok' if not is_degree_sequence(
        [1, 2, 2, 3, 4, 4, 2, 2, 2, 3, 1, 5, 7, 5]) else 'not ok')
    print('ok' if not is_degree_sequence(
        [1, 2, 2, 3, 4, 4, 2, 2, 2, 3, 1, 5, 7, 14]) else 'not ok')

    print('ok' if is_degree_sequence([2,2,4,4,4,4,4]) else 'not ok')
    #g = create_graph([2,2,4,4,4,4,4])
    # draw_graph(g)


def main():
    zadanie1()


if __name__ == '__main__':
    main()
