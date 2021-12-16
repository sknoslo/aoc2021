from lib import results


class Packet(object):
    pass


def add_version_numbers(packet):
    sum = packet.version

    if packet.type_id != 4:
        for p in packet.packets:
            sum += add_version_numbers(p)

    return sum


def product(values):
    val = 1
    for v in values:
        val *= v
    return val


def eval_packet(packet):
    match packet.type_id:
        case 4:
            return packet.literal_value
        case 0:
            return sum([eval_packet(p) for p in packet.packets])
        case 1:
            return product([eval_packet(p) for p in packet.packets])
        case 2:
            return min([eval_packet(p) for p in packet.packets])
        case 3:
            return max([eval_packet(p) for p in packet.packets])
        case 5:
            [a, b] = packet.packets
            return 1 if eval_packet(a) > eval_packet(b) else 0
        case 6:
            [a, b] = packet.packets
            return 1 if eval_packet(a) < eval_packet(b) else 0
        case 7:
            [a, b] = packet.packets
            return 1 if eval_packet(a) == eval_packet(b) else 0


def parse_literal_value(bits, index):
    literal = ""
    last_group = False
    while not last_group:
        if bits[index] == '0':
            last_group = True
        literal += bits[index+1:index+5]
        index += 5

    return int(literal, 2), index


def parse_int(bits, index, length):
    end = index + length
    return int(bits[index:end], 2), end


def parse_packet(bits, index=0):
    packet = Packet()

    packet.version, index = parse_int(bits, index, 3)
    packet.type_id, index = parse_int(bits, index, 3)

    if packet.type_id == 4:
        literal, index = parse_literal_value(bits, index)
        packet.literal_value = literal
    else:
        packet.packets = []
        packet.length_type_id, index = parse_int(bits, index, 1)
        if packet.length_type_id == 0:
            subpacket_length, index = parse_int(bits, index, 15)
            end = index + subpacket_length
            while index < end:
                subpacket, index = parse_packet(bits, index)
                packet.packets.append(subpacket)
        else:
            subpackets, index = parse_int(bits, index, 11)
            for _ in range(subpackets):
                subpacket, index = parse_packet(bits, index)
                packet.packets.append(subpacket)

    return packet, index


def unpack(hex):
    return "".join([format(int(c, 16), '04b') for c in hex])


def solve_part1(input):
    bits = unpack(input)
    packet, _ = parse_packet(bits)
    return add_version_numbers(packet)


def solve_part2(input):
    bits = unpack(input)
    packet, _ = parse_packet(bits)
    return eval_packet(packet)


def solve(input):
    return (solve_part1(input), solve_part2(input))


if __name__ == '__main__':
    assert unpack("D2FE28") == "110100101111111000101000"
    assert solve_part1("D2FE28") == 6
    assert solve_part1("8A004A801A8002F478") == 16
    assert solve_part1("620080001611562C8802118E34") == 12
    assert solve_part1("C0015000016115A2E0802F182340") == 23
    assert solve_part1("A0016C880162017C3686B18A3D4780") == 31

    assert solve_part2("9C0141080250320F1802104A08") == 1

    input = open("input/day16.txt").read().rstrip()
    (p1, p2) = solve(input)
    results(16, p1, p2)
