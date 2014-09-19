def changes_for_device(device, charger):
    changes = []
    for d, c in zip(device, charger):
        if d == c:
            changes.append(0)
        else:
            changes.append(1)
    return changes


def turn_switches(charger, changes):
    turned = []
    for bit, change in zip(charger, changes):
        if change:
            turned.append(str((int(bit) + 1) % 2))
        else:
            turned.append(bit)
    turned = "".join(turned)
    return turned


def charging_devices(requirements, chargers):
    requirements.sort()
    device = requirements[0]
    MAX_NUMBER = 1000000
    min_switches = MAX_NUMBER
    for charger in chargers:
        changes = changes_for_device(device, charger)
        new_chargers = [turn_switches(charger, changes) for charger in chargers]
        new_chargers.sort()
        if new_chargers == requirements:
            min_switches = min(min_switches, sum(changes))
    if min_switches == MAX_NUMBER:
        return "NOT POSSIBLE"
    else:
        return min_switches



if __name__ == '__main__':
    print(charging_devices(['01', '11', '10'], ['11', '00', '10']))
    print(charging_devices(['101', '111'], ['010', '001']))
    print(charging_devices(['01', '10'], ['10', '01']))
